"""Claude trade memory.

A self-contained, dependency-free memory layer that lets Claude learn from its
own trades and persist what it learned across sessions. Everything is stored as
plain JSON + Markdown so both the program and Claude (reading the files) can use
it.

Storage layout (under ``memory_dir``, default ``./memory`` next to this file):

    memory/
    ├── memory.json          # consolidated long-term memory (stats + lessons + notes)
    ├── MEMORY.md            # human / Claude readable summary, regenerated on consolidate
    └── sessions/
        └── <session_id>.json  # raw lessons recorded during a single session

Typical flow::

    mem = ClaudeMemory()
    mem.learn_from_trade({"symbol": "AAPL", "strategy": "rsi", "pnl_pct": 0.038,
                          "exit_reason": "take_profit", "hold_days": 12})
    mem.update_memory("rule:max_risk_per_trade", "Never risk more than 2% per trade")
    context = mem.recall(strategy="rsi")     # feed this back to the advisor
    mem.end_session()                        # consolidate into long-term memory

The class is intentionally heuristic and offline: no external services and no
API calls, so it runs anywhere with the standard library only.
"""

from __future__ import annotations

import json
import statistics
import uuid
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Optional


def _now() -> str:
    """UTC timestamp in ISO 8601 (seconds precision)."""
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def _default_memory_dir() -> Path:
    return Path(__file__).resolve().parent / "memory"


class ClaudeMemory:
    """Persistent, self-updating memory of Claude's trading experience."""

    # P&L thresholds (fraction, e.g. 0.001 == 0.1%) used to classify outcomes.
    BREAKEVEN_BAND = 0.001

    def __init__(
        self,
        memory_dir: Optional[str | Path] = None,
        session_id: Optional[str] = None,
    ) -> None:
        self.memory_dir = Path(memory_dir) if memory_dir else _default_memory_dir()
        self.sessions_dir = self.memory_dir / "sessions"
        self.memory_file = self.memory_dir / "memory.json"
        self.markdown_file = self.memory_dir / "MEMORY.md"

        self.sessions_dir.mkdir(parents=True, exist_ok=True)

        self.session_id = session_id or self._new_session_id()
        self.session_file = self.sessions_dir / f"{self.session_id}.json"

        self.memory = self._load_memory()
        self.session = self._load_session()

    # ------------------------------------------------------------------ #
    # Public API
    # ------------------------------------------------------------------ #
    def learn_from_trade(self, trade: dict[str, Any]) -> dict[str, Any]:
        """Learn from one closed trade and update memory.

        ``trade`` should contain at least ``symbol`` and ``pnl_pct`` (a fraction,
        e.g. 0.038 for +3.8%). Recognised optional keys: ``strategy``,
        ``exit_reason``, ``hold_days``, ``confidence``, ``reason``.

        Returns the lesson dict that was recorded.
        """
        symbol = str(trade.get("symbol", "UNKNOWN")).upper()
        strategy = str(trade.get("strategy", "unknown"))
        pnl_pct = float(trade.get("pnl_pct", 0.0))
        outcome = self._classify(pnl_pct)

        # Update aggregate stats (per strategy and per symbol).
        self._bump_stats(self.memory["stats"].setdefault("by_strategy", {}), strategy, pnl_pct, outcome)
        self._bump_stats(self.memory["stats"].setdefault("by_symbol", {}), symbol, pnl_pct, outcome)

        lesson = {
            "id": uuid.uuid4().hex[:8],
            "created_at": _now(),
            "session_id": self.session_id,
            "kind": "trade",
            "symbol": symbol,
            "strategy": strategy,
            "outcome": outcome,
            "pnl_pct": pnl_pct,
            "text": self._lesson_text(symbol, strategy, outcome, pnl_pct, trade),
            "tags": [outcome, strategy, symbol],
            "trade": trade,
        }
        self.session["lessons"].append(lesson)
        self.session["trade_count"] += 1
        self._save_session()
        return lesson

    def record_lesson(
        self,
        text: str,
        tags: Optional[list[str]] = None,
        metadata: Optional[dict[str, Any]] = None,
    ) -> dict[str, Any]:
        """Record a free-form lesson Claude wants to remember."""
        lesson = {
            "id": uuid.uuid4().hex[:8],
            "created_at": _now(),
            "session_id": self.session_id,
            "kind": "note",
            "text": text,
            "tags": tags or [],
            "metadata": metadata or {},
        }
        self.session["lessons"].append(lesson)
        self._save_session()
        return lesson

    def update_memory(self, key: str, value: Any) -> None:
        """Let Claude change its persistent memory (a key/value note).

        Use this for durable convictions, rules or preferences, e.g.
        ``update_memory("rule:no_trades_during_fomc", True)``.
        """
        self.memory.setdefault("notes", {})[key] = {
            "value": value,
            "updated_at": _now(),
            "session_id": self.session_id,
        }
        self._save_memory()

    def recall(
        self,
        symbol: Optional[str] = None,
        strategy: Optional[str] = None,
        tags: Optional[list[str]] = None,
        limit: int = 10,
    ) -> list[dict[str, Any]]:
        """Return the most relevant long-term lessons for the given filters."""
        wanted = {t.lower() for t in (tags or [])}
        if symbol:
            wanted.add(symbol.upper())
        if strategy:
            wanted.add(strategy.lower())

        lessons = self.memory.get("lessons", [])
        if wanted:
            lessons = [
                ls for ls in lessons
                if wanted & {str(t).lower() for t in ls.get("tags", [])}
            ]
        return sorted(lessons, key=lambda ls: ls.get("created_at", ""), reverse=True)[:limit]

    def get_context_for_advisor(self, symbol: str, strategy: str) -> str:
        """One-line textual context for the Claude advisory skill."""
        stats = self.memory.get("stats", {}).get("by_strategy", {}).get(strategy)
        relevant = self.recall(symbol=symbol, strategy=strategy, limit=3)
        if not stats:
            return f"No prior memory for {symbol}/{strategy}."
        win_rate = stats["wins"] / stats["trades"] if stats["trades"] else 0.0
        avg = stats["total_pnl_pct"] / stats["trades"] if stats["trades"] else 0.0
        tips = " | ".join(ls["text"] for ls in relevant)
        return (
            f"Memory for {symbol}/{strategy}: {stats['trades']} trades, "
            f"{stats['wins']}/{stats['trades']} wins ({win_rate:.0%}), "
            f"avg P&L {avg:.2%}. {tips}"
        )

    def end_session(self) -> dict[str, Any]:
        """Alias for :meth:`consolidate` — call when a session is finished."""
        return self.consolidate()

    def consolidate(self) -> dict[str, Any]:
        """Merge the current session's lessons into long-term memory."""
        existing_ids = {ls.get("id") for ls in self.memory.get("lessons", [])}
        new = [ls for ls in self.session["lessons"] if ls.get("id") not in existing_ids]
        self.memory["lessons"].extend(new)
        self.memory["updated_at"] = _now()
        self.memory.setdefault("sessions", {})[self.session_id] = {
            "consolidated_at": _now(),
            "lessons_added": len(new),
            "trade_count": self.session["trade_count"],
        }
        self._save_memory()
        self._write_markdown()
        return {"session_id": self.session_id, "lessons_added": len(new)}

    def get_summary(self) -> dict[str, Any]:
        """High-level snapshot of long-term memory."""
        by_strategy = self.memory.get("stats", {}).get("by_strategy", {})
        trades = sum(s["trades"] for s in by_strategy.values())
        wins = sum(s["wins"] for s in by_strategy.values())
        return {
            "total_trades": trades,
            "win_rate": (wins / trades) if trades else 0.0,
            "lessons": len(self.memory.get("lessons", [])),
            "notes": len(self.memory.get("notes", {})),
            "strategies_tracked": list(by_strategy.keys()),
            "updated_at": self.memory.get("updated_at"),
        }

    # ------------------------------------------------------------------ #
    # Internals
    # ------------------------------------------------------------------ #
    def _classify(self, pnl_pct: float) -> str:
        if pnl_pct > self.BREAKEVEN_BAND:
            return "win"
        if pnl_pct < -self.BREAKEVEN_BAND:
            return "loss"
        return "breakeven"

    @staticmethod
    def _bump_stats(bucket: dict[str, Any], key: str, pnl_pct: float, outcome: str) -> None:
        entry = bucket.setdefault(key, {"trades": 0, "wins": 0, "losses": 0, "total_pnl_pct": 0.0})
        entry["trades"] += 1
        entry["total_pnl_pct"] += pnl_pct
        if outcome == "win":
            entry["wins"] += 1
        elif outcome == "loss":
            entry["losses"] += 1

    def _lesson_text(
        self, symbol: str, strategy: str, outcome: str, pnl_pct: float, trade: dict[str, Any]
    ) -> str:
        reason = trade.get("exit_reason") or trade.get("reason") or "n/a"
        hold = trade.get("hold_days")
        hold_txt = f", held {hold}d" if hold is not None else ""
        verb = {"win": "worked", "loss": "failed", "breakeven": "was flat"}[outcome]
        return (
            f"{strategy} on {symbol} {verb} ({pnl_pct:+.2%}, exit: {reason}{hold_txt}). "
            + self._takeaway(strategy, outcome)
        )

    def _takeaway(self, strategy: str, outcome: str) -> str:
        stats = self.memory["stats"].get("by_strategy", {}).get(strategy, {})
        trades = stats.get("trades", 0)
        if trades < 3:
            return "Not enough samples yet to draw a firm conclusion."
        win_rate = stats.get("wins", 0) / trades
        if outcome == "loss" and win_rate < 0.4:
            return f"{strategy} is underperforming ({win_rate:.0%} win rate) — consider downweighting it."
        if outcome == "win" and win_rate > 0.6:
            return f"{strategy} is reliable so far ({win_rate:.0%} win rate) — keep trusting it."
        return f"Running {strategy} win rate: {win_rate:.0%}."

    def _new_session_id(self) -> str:
        return datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%S") + "-" + uuid.uuid4().hex[:4]

    def _load_memory(self) -> dict[str, Any]:
        if self.memory_file.exists():
            try:
                data = json.loads(self.memory_file.read_text(encoding="utf-8"))
            except (json.JSONDecodeError, OSError):
                data = {}
        else:
            data = {}
        data.setdefault("updated_at", None)
        data.setdefault("stats", {})
        data.setdefault("lessons", [])
        data.setdefault("notes", {})
        data.setdefault("sessions", {})
        return data

    def _load_session(self) -> dict[str, Any]:
        if self.session_file.exists():
            try:
                return json.loads(self.session_file.read_text(encoding="utf-8"))
            except (json.JSONDecodeError, OSError):
                pass
        return {
            "session_id": self.session_id,
            "started_at": _now(),
            "trade_count": 0,
            "lessons": [],
        }

    def _save_memory(self) -> None:
        self.memory_file.write_text(json.dumps(self.memory, indent=2, ensure_ascii=False), encoding="utf-8")

    def _save_session(self) -> None:
        self.session_file.write_text(json.dumps(self.session, indent=2, ensure_ascii=False), encoding="utf-8")

    def _write_markdown(self) -> None:
        s = self.get_summary()
        lines = [
            "# Claude Trading Memory",
            "",
            f"_Last updated: {self.memory.get('updated_at') or 'never'}_",
            "",
            "## Summary",
            "",
            f"- Total trades learned from: **{s['total_trades']}**",
            f"- Overall win rate: **{s['win_rate']:.0%}**",
            f"- Lessons stored: **{s['lessons']}**",
            f"- Persistent notes/rules: **{s['notes']}**",
            "",
        ]

        by_strategy = self.memory.get("stats", {}).get("by_strategy", {})
        if by_strategy:
            lines += ["## Per-strategy performance", "", "| Strategy | Trades | Win rate | Avg P&L |", "|---|---|---|---|"]
            for name, st in sorted(by_strategy.items()):
                wr = st["wins"] / st["trades"] if st["trades"] else 0.0
                avg = st["total_pnl_pct"] / st["trades"] if st["trades"] else 0.0
                lines.append(f"| {name} | {st['trades']} | {wr:.0%} | {avg:+.2%} |")
            lines.append("")

        notes = self.memory.get("notes", {})
        if notes:
            lines += ["## Rules & convictions", ""]
            for key, note in sorted(notes.items()):
                lines.append(f"- **{key}**: {note['value']}")
            lines.append("")

        recent = sorted(self.memory.get("lessons", []), key=lambda ls: ls.get("created_at", ""), reverse=True)[:15]
        if recent:
            lines += ["## Recent lessons", ""]
            for ls in recent:
                lines.append(f"- {ls['text']}")
            lines.append("")

        self.markdown_file.write_text("\n".join(lines), encoding="utf-8")


def _demo() -> None:
    """Tiny offline demo / manual test (no external dependencies)."""
    mem = ClaudeMemory()
    sample_trades = [
        {"symbol": "AAPL", "strategy": "rsi", "pnl_pct": 0.038, "exit_reason": "take_profit", "hold_days": 12},
        {"symbol": "TSLA", "strategy": "rsi", "pnl_pct": -0.021, "exit_reason": "stop_loss", "hold_days": 4},
        {"symbol": "SPY", "strategy": "ma_crossover", "pnl_pct": 0.012, "exit_reason": "signal_flip", "hold_days": 20},
    ]
    for t in sample_trades:
        lesson = mem.learn_from_trade(t)
        print("learned:", lesson["text"])

    mem.update_memory("rule:max_risk_per_trade", "Never risk more than 2% of capital on a single trade")
    result = mem.consolidate()
    print("\nconsolidated:", result)
    print("summary:", json.dumps(mem.get_summary(), indent=2))
    print("\nadvisor context:", mem.get_context_for_advisor("AAPL", "rsi"))


if __name__ == "__main__":
    _demo()

# Claude memory

This folder is **Claude's persistent trading memory**. It is written and read by
[`../claude_memory.py`](../claude_memory.py) (`ClaudeMemory`), and the Markdown
files are meant to be human- and Claude-readable directly.

The idea: after each trade, Claude *learns* a lesson; at the end of each session
those lessons are *consolidated* into long-term memory so the next session starts
with everything learned so far.

## Files

| File | Role |
|---|---|
| `memory.json` | Consolidated long-term memory (machine-readable, source of truth) |
| `MEMORY.md` | Human/Claude-readable summary, **regenerated** on each `consolidate()` |
| `sessions/<id>.json` | Raw lessons recorded during a single session (a journal) |

## `memory.json` structure

```jsonc
{
  "updated_at": "2026-06-18T10:00:00+00:00",
  "stats": {
    "by_strategy": { "rsi": { "trades": 8, "wins": 6, "losses": 2, "total_pnl_pct": 0.17 } },
    "by_symbol":   { "AAPL": { "trades": 3, "wins": 2, "losses": 1, "total_pnl_pct": 0.05 } }
  },
  "lessons": [
    { "id": "a1b2c3d4", "created_at": "...", "session_id": "...",
      "kind": "trade", "symbol": "AAPL", "strategy": "rsi",
      "outcome": "win", "pnl_pct": 0.038, "text": "...", "tags": ["win", "rsi", "AAPL"] }
  ],
  "notes": {
    "rule:max_risk_per_trade": { "value": "Never risk more than 2% per trade", "updated_at": "...", "session_id": "..." }
  },
  "sessions": {
    "20260618T100000-ab12": { "consolidated_at": "...", "lessons_added": 3, "trade_count": 3 }
  }
}
```

## Usage

```python
from claude_memory import ClaudeMemory

mem = ClaudeMemory()                       # opens (or creates) this folder
mem.learn_from_trade({                     # learn from a closed trade
    "symbol": "AAPL", "strategy": "rsi",
    "pnl_pct": 0.038, "exit_reason": "take_profit", "hold_days": 12,
})
mem.update_memory("rule:no_fomc_trades", True)   # Claude edits its own memory
context = mem.recall(strategy="rsi")             # recall to inform new decisions
mem.end_session()                                # consolidate into long-term memory
```

> The committed `memory.json` / `MEMORY.md` are empty starting points. Real
> session data accumulates here as the agent trades.

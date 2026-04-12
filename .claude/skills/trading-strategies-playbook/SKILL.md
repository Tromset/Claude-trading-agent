---
name: trading-strategies-playbook
description: Use when the agent needs to pick a trading strategy for a given situation, match strategy to timeframe and market regime, or route to a specific strategy reference (day, swing, position, mean-reversion, breakout, trend-following).
---

# Trading Strategies Playbook — Master Index

This skill is the **router** for tactical (non-value) strategies. Value investing lives in `fundamental-analysis-and-value-investing`; it is the default lens. Everything here is secondary and must respect the Buffett-first stance: **if a tactical setup conflicts with a value-backed position, emit Z.**

## When to use this skill

- A candidate setup exists and the agent must choose which playbook frames it.
- The timeframe of the opportunity is ambiguous (intraday? swing? weeks?).
- Market regime changed (trend → range, or vice versa) and active strategies must be re-evaluated.
- The agent is flat and scanning, and needs to know which strategy file to pull.

**Anti-triggers:**
- Deep value / 10-K / DCF work — use `fundamental-analysis-and-value-investing` directly.
- Order routing questions — use `order-types-execution`.
- Sizing questions — use `risk-management`.

## Prerequisites

- Current market regime read (trending vs range) — from `technical-indicators` (ADX) and `price-action-and-market-structure`.
- Time-of-day + session context — from `trading-fundamentals`.
- Account type / PDT status — from `regulations-and-tax-awareness`.
- Fresh `risk-management` sizing capability.

## Core concepts

### The five strategy families in this library

| Family | Timeframe | Regime fit | File |
|---|---|---|---|
| Day trading | minutes to hours, flat by close | high intraday range, clear session levels | `references/day-trading.md` |
| Swing trading | 2–10 days | any, but cleanest in trends with pullbacks | `references/swing-trading.md` |
| Position trading | weeks to months | trending HTF with moderate volatility | `references/position-trading.md` |
| Mean reversion | minutes to days | range-bound only (ADX < 20) | `references/mean-reversion.md` |
| Breakout | minutes to weeks | post-consolidation, volume available | `references/breakout.md` |
| Trend following | weeks to months | sustained HTF trends | `references/trend-following.md` |

These are overlapping, not exclusive. A single name can be a breakout on the daily that is also a trend-following add on the weekly. The agent picks the **primary** frame and uses it.

### Strategy–timeframe alignment (must match)

A strategy is valid only if the analysis timeframe, the trigger timeframe, and the holding period agree. Mixing them is the #1 source of losses.

| Strategy | Analysis TF | Trigger TF | Hold |
|---|---|---|---|
| Day trading | 15m / 5m | 1m / tick | minutes–hours |
| Swing | Daily | 4h / 1h | 2–10 days |
| Position | Weekly | Daily | weeks–months |
| Mean reversion | Daily (range) | 1h / 15m | hours–days |
| Breakout | Daily | 1h / 15m | days–weeks |
| Trend following | Weekly | Daily | weeks–months |

If the trigger TF is lower than the analysis TF, you are **looking up**. If the trigger is higher, you are confused — emit Z.

### Regime gate (which strategies are eligible now)

1. Compute ADX(14) on the analysis timeframe.
2. If ADX ≥ 25 and rising → **trending** regime. Eligible: trend-following, swing (pullback), breakout, position. Mean reversion is **disabled**.
3. If ADX < 20 → **range** regime. Eligible: mean reversion, intraday fade at extremes. Breakout and trend-following are **disabled** except on higher TF.
4. If ADX 20–25 → **transitional**. Default: Z. Only breakout setups with strong volume are eligible.

## Decision procedure

1. Read the situation (ticker, chart, intent, account).
2. If the user intent is long-horizon value → exit this skill, go to `fundamental-analysis-and-value-investing`.
3. Determine holding-period intent (day / swing / position / undecided).
4. Compute regime on the matching analysis TF.
5. Filter the strategy family list by regime eligibility.
6. Filter by account constraints (PDT locks out day trading under $25k; options/futures have margin rules).
7. Load the single best-matching reference file. Prefer the most conservative match.
8. Execute that file's decision procedure to produce a candidate X / Y / Z with entry, stop, target, rationale.
9. Hand the candidate to `risk-management` for sizing, then to `buy-sell-hold-decision` for the final action.
10. Log which strategy family was chosen and why, regardless of outcome.

## Heuristics & thresholds

- **One strategy per trade.** Do not blend day-trading entries with swing holding periods.
- **Regime is king.** A good breakout setup in a range-bound market is still a loss more often than not.
- **Default to swing.** When timeframe intent is unclear, swing trading has the best balance of edge and discipline for a conservative agent.
- **Value trumps tactics.** If a tactical Y would exit a value position that is still within its thesis → downgrade to Z.
- **Confluence with HTF only.** Take swing longs only when the weekly trend is up. Take swing shorts only when the weekly is down and HTF is not at a major support.
- **Regime change = flatten tactical book.** When ADX crosses 20 or 25, re-evaluate every tactical position; value positions are untouched.

## Common failure modes

- **Strategy drift.** Opening a trade as a day-trade and converting it to a "swing" because it went against the intended direction. Forbidden — stop-out or scratch.
- **Mean reversion in trends.** Fading strength in a trending market is the single most expensive tactical mistake.
- **Breakout chasing.** Entering >1% above the breakout level. Use `references/breakout.md` entry gate.
- **Mixed timeframes.** 1-minute trigger, daily stop, weekly target. Misaligned — emit Z.
- **Ignoring the account type.** Running day-trades on a sub-$25k cash account in the US violates PDT. Hard block.
- **Pattern without regime.** Seeing a flag and taking it regardless of whether ADX even supports trend continuation.

## Outputs expected

This skill contributes a **strategy-framed candidate action** toward the final X / Y / Z:

```json
{
  "skill": "trading-strategies-playbook",
  "strategy_family": "swing" | "day" | "position" | "mean-reversion" | "breakout" | "trend-following",
  "reference_file": "references/swing-trading.md",
  "candidate_action": "X" | "Y" | "Z",
  "confidence": 0-100,
  "entry_price": 182.05,
  "stop_price": 177.80,
  "target_price": 192.00,
  "timeframe_analysis": "Daily",
  "timeframe_trigger": "1h",
  "regime": "trending",
  "adx_14": 27.3,
  "rationale": "Daily uptrend, ADX 27, pullback to 20EMA with 1h bullish engulfing",
  "eligible_families": ["swing", "trend-following", "breakout"],
  "rejected_families": ["mean-reversion"],
  "notes": "..."
}
```

This feeds into `risk-management` for sizing, then `buy-sell-hold-decision` for the final collapse.

## References (lazy-load)

- `references/day-trading.md` — intraday setups, session structure, PDT.
- `references/swing-trading.md` — 2–10 day holds, pullback and breakout variants.
- `references/position-trading.md` — weeks to months, weekly-chart setups, sector rotation.
- `references/mean-reversion.md` — counter-trend only in ranges.
- `references/breakout.md` — volume-confirmed pattern breakouts.
- `references/trend-following.md` — classic trend-following mechanics.

## Cross-links

- Pairs with: `price-action-and-market-structure`, `chart-patterns`, `technical-indicators`, `volume-analysis`, `support-resistance-and-fibonacci`.
- Feeds: `risk-management` → `buy-sell-hold-decision` → `pre-trade-checklist-playbook`.
- Defers to: `fundamental-analysis-and-value-investing` on any value-vs-tactical conflict.
- Escalates to: `safety-and-kill-switch` on regime-change induced portfolio stress.

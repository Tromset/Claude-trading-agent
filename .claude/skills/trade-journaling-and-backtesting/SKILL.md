---
name: trade-journaling-and-backtesting
description: Use when logging a trade (X, Y, or loud-Z override), reviewing performance metrics, or evaluating strategy health from historical data.
---

# Trade Journaling & Backtesting

The feedback loop. Every trade and every loud-Z override is logged. Metrics are computed. Strategies are evaluated. Without this skill, the agent cannot learn, audit, or improve.

## When to use this skill

- After every X (entry) — log the entry with full context.
- After every Y (exit) — log the exit, compute R-multiple, update metrics.
- After every Z-OVERRIDE (would-be X/Y blocked) — log the override.
- Weekly: compute and review performance metrics.
- Monthly: deep-dive review, strategy comparison, drawdown analysis.
- Before promotion from paper to live: evaluate promotion criteria.

**Anti-triggers:** silent Z (nothing was going to happen) is NOT journaled. Only actions and overrides.

## Prerequisites

- Trade data from `buy-sell-hold-decision` output schema.
- Screenshot references (before/after for entries and exits).
- Account balance history for equity-curve computation.

## Core concepts

### What gets journaled

| Event | Logged? | Key fields |
|---|---|---|
| X (entry) | Always | ticker, side, qty, entry_price, stop, target, strategy, confidence, rationale |
| Y (exit) | Always | position_ref, exit_price, exit_reason, realized_pnl, R_multiple, holding_period |
| Z-OVERRIDE | Always | would_have_been, blocking_skill, blocking_invariant, rationale |
| Silent Z | Never | — |

### R-multiple (the universal metric)

R = risk per trade (stop distance x qty). Every outcome is measured in R:

```
R_multiple = realized_pnl / initial_risk
```

- R = +1.0 → trade won exactly 1R (hit the stop in reverse → bad, but hit target at 1R distance → good)
- R = +2.0 → trade won 2× the risk
- R = -1.0 → trade lost exactly 1R (stopped out as planned)
- R = -0.5 → trade exited at half the planned risk (early thesis-break exit)
- R = +3.5 → trade won 3.5× the risk (excellent)

R normalizes across different position sizes and instruments, making trades comparable.

### Journal entry schema

See `references/journal-schema.md` for the full JSON schema. Key fields:
- Entry record: id, timestamp, ticker, side, qty, entry_price, stop_price, target_price, strategy_source, confidence, skills_invoked, rationale, screenshot_ref
- Exit record: exit_timestamp, exit_price, exit_reason, realized_pnl, R_multiple, holding_period_bars, post_trade_analysis
- Override record: would_have_been, blocking_skill, blocking_invariant

### Performance metrics

Computed weekly from the journal. See `references/metrics-glossary.md` for formulas.

**Core metrics dashboard:**
| Metric | Target | Warning |
|---|---|---|
| Win rate | 40-60% (strategy-dependent) | < 35% or > 70% (review) |
| Average R (winners) | > 1.5R | < 1.0R |
| Average R (losers) | -0.8R to -1.0R (planned stops) | > -1.5R (stops not honored) |
| Expectancy | > 0 | ≤ 0 (strategy is losing money) |
| Profit factor | > 1.5 | < 1.0 |
| Max drawdown | < 15% | > 20% |
| Sharpe ratio | > 1.0 | < 0.5 |
| Consecutive losses | < 5 | ≥ 5 |

### Review cadence

| Frequency | What to review |
|---|---|
| **After each trade** | Log the entry/exit record; quick sanity check |
| **Daily EOD** | Day's P&L summary, any kills or overrides |
| **Weekly** | Metrics dashboard, equity curve, win/loss streaks |
| **Monthly** | Deep-dive: strategy breakdown, drawdown analysis, discipline audit |
| **Quarterly** | Compare paper vs live, evaluate strategy promotion/demotion |

## Decision procedure

1. Receive trade event (X, Y, or Z-OVERRIDE) from `buy-sell-hold-decision`.
2. Construct the journal entry using the schema.
3. For exits: compute R-multiple, holding period, realized P&L.
4. Append to the journal.
5. Update running metrics (incremental: win count, loss count, cumulative R, equity).
6. Check for red flags:
   - 3 consecutive losses → flag for `safety-and-kill-switch` soft kill.
   - Avg loss > -1.5R → stops are not being honored → investigate.
   - Expectancy turned negative over last 10 trades → flag for strategy review.
7. Report any flags to `trading-master`.

## Heuristics & thresholds

- **Minimum 30 trades** for any meaningful metric calculation.
- **Rolling 20-trade window** for trend detection (is the strategy improving or degrading?).
- **R-multiple distribution** should be tight around -1R for losses and spread (1R–3R) for wins. Long left tail (losses > -2R) means risk management is failing.
- **Win rate × avg win vs loss rate × avg loss** = expectancy. Must be positive.
- **Equity curve** should be upward-sloping without long flat periods (drawdown) or spike-dependency.

## Common failure modes

- **Not journaling paper trades.** Paper data is the only pre-live validation data. Journal it.
- **Journaling entries but not exits.** Incomplete records → broken metrics.
- **Not computing R-multiples.** Dollar P&L is meaningless without context. Always use R.
- **Cherry-picking review periods.** Review all trades, not just winners.
- **Ignoring loud-Z overrides in the journal.** These are where discipline lives — review them.
- **Over-optimizing from journal data.** The journal is for diagnosis, not for curve-fitting a strategy to past trades.

## Outputs expected

```json
{
  "skill": "trade-journaling-and-backtesting",
  "event_type": "entry" | "exit" | "override",
  "journal_entry": { "...schema fields..." },
  "running_metrics": {
    "total_trades": 47,
    "win_rate": 0.49,
    "avg_R_winners": 1.8,
    "avg_R_losers": -0.95,
    "expectancy": 0.41,
    "profit_factor": 1.72,
    "max_drawdown": 0.082,
    "sharpe": 1.15,
    "consecutive_losses_current": 1
  },
  "flags": []
}
```

## References (lazy-load)

- `references/metrics-glossary.md` — full glossary of every metric with formula.
- `references/journal-schema.md` — exact JSON schema for journal entries with examples.

## Cross-links

- Pairs with: `buy-sell-hold-decision` (provides trade events), `risk-management` (provides R calculation inputs), `paper-trading-workflow` (paper journals feed promotion criteria), `safety-and-kill-switch` (consecutive-loss flags), `trading-master` (receives red flags).

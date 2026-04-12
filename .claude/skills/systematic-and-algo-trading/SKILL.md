---
name: systematic-and-algo-trading
description: Use when evaluating a rule-based or algorithmic trading strategy for deployment readiness, reviewing backtest results for validity, or assessing whether a systematic approach has passed walk-forward and out-of-sample tests.
---

# Systematic & Algorithmic Trading

The science of replacing discretionary judgment with explicit rules. This skill helps the agent evaluate systematic strategies — whether they are robust, properly tested, and ready for deployment. The agent does not write trading algorithms but evaluates their design, test results, and ongoing performance.

**Disclaimer:** This skill is for educational purposes. Past backtest performance does not guarantee future results. Not financial advice.

## When to use this skill

- When evaluating a rule-based strategy (fully defined entry/exit/sizing rules).
- When reviewing backtest results for validity and robustness.
- When deciding whether a systematic strategy passes the bar for paper → live promotion.
- When comparing systematic vs discretionary approaches for a given market.
- When assessing whether a strategy has degraded and needs re-optimization.

**Anti-triggers:** not for discretionary chart reading (use price-action, chart-patterns). Not for writing code (this agent evaluates, not codes).

## Prerequisites

- `trading-strategies-playbook` — the strategy templates this skill evaluates.
- `trade-journaling-and-backtesting` — where live/paper performance is tracked.
- `risk-management` — sizing rules must be part of the system.
- Understanding of statistical concepts (sample size, significance, overfitting).

## Core concepts

### Systematic vs discretionary

| Aspect | Discretionary | Systematic |
|---|---|---|
| Entry rules | Judgment + pattern recognition | Explicit, codified conditions |
| Exit rules | Judgment + feel | Predefined: stop, target, time-stop |
| Sizing | Varies by conviction | Formula-based (fixed fractional, Kelly, etc.) |
| Emotional influence | High | Minimal (execution follows rules) |
| Reproducibility | Low (different trader, different results) | High (same rules, same results on same data) |
| Backtestable | Partially (subjective elements can't be coded) | Fully (all rules are explicit) |
| Adaptability | High (human can adjust in real-time) | Low (rules are static until re-optimized) |

The agent operates primarily as a discretionary trader with systematic guardrails (checklists, risk rules). But it can evaluate systematic strategies when presented with them.

### The signal → filter → size → execute pipeline

Every systematic strategy follows this pipeline:

```
1. SIGNAL    → Entry condition triggered (e.g., MACD crossover + RSI > 50)
2. FILTER    → Regime/context filter (e.g., only in uptrend, only during RTH)
3. SIZE      → Position sizing (e.g., 1% risk, ATR-based stop)
4. EXECUTE   → Order type + execution (e.g., limit at signal bar close)
5. MANAGE    → Stop/target/trail rules (e.g., trail stop at 2× ATR)
6. EXIT      → Exit condition (e.g., stop hit, target hit, or time-stop at 10 bars)
```

Each step must be explicitly defined with no discretion. If any step requires "judgment," it's not fully systematic.

### Backtesting principles

Backtesting applies the strategy rules to historical data to estimate how it would have performed. Valid backtesting requires:

1. **Clean data.** Adjusted for splits, dividends, delistings. No gaps, no errors.
2. **Realistic fills.** Account for slippage (1 tick for liquid stocks, more for illiquid), commissions, and spread.
3. **No look-ahead bias.** The strategy can only use data available at the time of each decision.
4. **Survivorship-bias-free data.** Include delisted stocks (not just today's survivors).
5. **Out-of-sample holdout.** Never optimize on the same data used for final evaluation.
6. **Sufficient sample size.** Minimum 100 trades for any meaningful statistical conclusion.

See `references/backtest-pitfalls.md` for the complete catalog of what can go wrong.

### Walk-forward analysis (WFA)

The gold standard for strategy validation. Instead of optimizing on one period and hoping it works on the next:

1. Divide data into rolling windows: in-sample (IS) for optimization, out-of-sample (OOS) for testing.
2. Optimize parameters on IS data.
3. Test with those parameters on OOS data (no re-optimization).
4. Roll the window forward and repeat.
5. Concatenate all OOS results → this is the walk-forward performance.

See `references/walk-forward.md` for the full methodology and worked example.

**Walk-forward efficiency (WFE):**
```
WFE = OOS_performance / IS_performance
```

- WFE > 0.5 → strategy retains more than half its in-sample performance out-of-sample → acceptable.
- WFE > 0.7 → robust.
- WFE < 0.3 → likely overfitted — in-sample performance doesn't generalize.

### Out-of-sample (OOS) testing

| Test type | Method | What it validates |
|---|---|---|
| **Holdout** | Reserve last 20–30% of data, never touch during optimization | Does the strategy work on unseen data? |
| **Walk-forward** | Rolling IS/OOS windows | Does the strategy work across multiple unseen periods? |
| **Paper trading** | Forward test on live data, no real money | Does the strategy work in real-time execution? |
| **Live (small)** | 50% size, first 10 trades | Does the strategy survive real fills, slippage, psychology? |

### Monte Carlo simulation

Shuffle the order of trades and/or perturb trade outcomes to estimate the range of possible results:

1. Take the set of actual backtest trades.
2. Randomly reshuffle their order (1000+ iterations).
3. For each shuffle, compute: max drawdown, final equity, Sharpe, etc.
4. Build a distribution of outcomes.

**What it tells you:**
- **Worst-case drawdown** at 95th percentile → is this survivable?
- **Probability of ruin** → what % of simulations result in account depletion?
- **Confidence interval** for expectancy → is the positive expectancy robust or fragile?

### Parameter sensitivity

A robust strategy should work across a **range** of parameter values, not just one magic number.

- If the strategy is profitable with RSI period 12–18 but breaks at 11 or 19 → fragile, likely overfitted.
- If the strategy is profitable with RSI period 8–25 → robust, the edge is in the concept, not the parameter.

Test: vary each parameter ±20% and measure performance degradation. If performance drops > 50% → parameter is too sensitive.

### Regime detection

Markets alternate between regimes (trending, ranging, volatile, quiet). A strategy that works in one regime may fail in another.

| Regime | Characteristics | Strategies that work | Strategies that fail |
|---|---|---|---|
| **Trending** | ADX > 25, clear HH/HL or LL/LH | Trend-following, breakout | Mean-reversion |
| **Ranging** | ADX < 20, price between S/R | Mean-reversion, range-trading | Trend-following |
| **High volatility** | ATR expanding, VIX > 25 | Reduced size, wider stops | Normal-sized positions |
| **Low volatility** | ATR contracting, VIX < 15 | Breakout (volatility expansion coming) | Wide-stop strategies (stopped by noise) |

A robust systematic strategy either: (a) works across multiple regimes, or (b) has a regime filter that disables it in unfavorable regimes.

## Decision procedure

When evaluating a systematic strategy for deployment:

1. **Rule completeness:** Are all 6 pipeline steps (signal, filter, size, execute, manage, exit) fully defined? If any step requires discretion → not ready.
2. **Backtest validity:** Check for all pitfalls in `references/backtest-pitfalls.md`. Flag any violations.
3. **Sample size:** ≥ 100 trades in backtest? If not → insufficient data.
4. **Walk-forward test:** WFE > 0.5? If not → likely overfitted.
5. **Monte Carlo:** 95th-percentile drawdown survivable? Probability of ruin < 1%?
6. **Parameter sensitivity:** Profitable across ±20% parameter range? If not → fragile.
7. **Regime awareness:** Does the strategy have a regime filter, or does it work across regimes?
8. **Risk compliance:** Does the system respect 1% per-trade risk, stops always set, R:R ≥ 2:1?
9. **Paper validation:** ≥ 30 paper trades with positive expectancy?

If ALL pass → recommend promotion to live (50% size first 10 trades).
If any fail → identify the failure and recommend either fixing it or rejecting the strategy.

## Heuristics & thresholds

- **Minimum 100 backtest trades** for statistical significance.
- **WFE > 0.5** for walk-forward acceptance.
- **Parameter robustness:** profitable across ±20% of each parameter.
- **Monte Carlo 95th percentile max drawdown < 25%** of starting equity.
- **Probability of ruin < 1%** in Monte Carlo (defined as account dropping below 50% of start).
- **Degrees of freedom rule:** number of optimizable parameters should be < number of trades / 10. (e.g., 5 parameters requires ≥ 50 trades minimum, ideally 100+).

## Common failure modes

- **Overfitting.** The #1 failure. Too many parameters optimized on too little data. The backtest looks incredible; live performance is terrible. See `references/backtest-pitfalls.md`.
- **Ignoring transaction costs.** Strategy shows 0.3% edge per trade, but commissions + slippage are 0.2% → real edge is only 0.1%, barely positive.
- **Curve fitting to one regime.** Strategy optimized on a trending market fails immediately when the regime changes.
- **Survival bias in strategy selection.** Testing 100 strategies and picking the best one = optimization bias. The best strategy out of 100 random ones will look good by chance.
- **Confusing backtest equity with live equity.** Backtest results are an upper bound, not a prediction.
- **No re-evaluation cadence.** A strategy that worked in 2023 may not work in 2025. Regular WFA re-runs are needed.

## Outputs expected

```json
{
  "skill": "systematic-and-algo-trading",
  "strategy_name": "rsi-mean-reversion-daily",
  "evaluation": {
    "rule_completeness": true,
    "backtest_trades": 187,
    "backtest_valid": true,
    "pitfalls_found": [],
    "walk_forward_efficiency": 0.62,
    "monte_carlo_95th_dd": 0.18,
    "probability_of_ruin": 0.002,
    "parameter_robust": true,
    "regime_filter": "ADX < 25 only",
    "risk_compliant": true,
    "paper_validated": true
  },
  "recommendation": "PROMOTE_TO_LIVE_50PCT" | "CONTINUE_PAPER" | "REJECT" | "FIX_AND_RETEST",
  "issues": []
}
```

## References (lazy-load)

- `references/backtest-pitfalls.md` — complete catalog of backtesting errors with detection and mitigation.
- `references/walk-forward.md` — walk-forward analysis methodology with worked example.

## Cross-links

- Pairs with: `trading-strategies-playbook` (strategies to evaluate), `trade-journaling-and-backtesting` (performance tracking), `risk-management` (sizing rules), `paper-trading-workflow` (paper validation stage).

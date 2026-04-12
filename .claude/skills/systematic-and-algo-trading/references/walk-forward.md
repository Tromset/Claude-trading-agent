# Walk-Forward Analysis (WFA)

## What Is Walk-Forward Analysis

Walk-forward analysis is a rolling backtesting methodology that prevents overfitting by repeatedly optimizing on one period (in-sample) and testing on the next unseen period (out-of-sample). It simulates what a trader would actually do: optimize, trade, re-optimize, trade again.

## Why It Matters

A standard backtest optimizes on all available data, then reports performance on that same data. This is like studying the answer key before taking the test — of course you'll score well.

Walk-forward fixes this by testing on data the optimizer has never seen. If the strategy can't perform on unseen data, it's overfitted.

## The Rolling Window Approach

```
Total data: |========================================|
             2018    2019    2020    2021    2022    2023

Window 1:   |---IS---|--OOS--|
            2018-2019  2020

Window 2:        |---IS---|--OOS--|
                 2019-2020  2021

Window 3:             |---IS---|--OOS--|
                      2020-2021  2022

Window 4:                  |---IS---|--OOS--|
                           2021-2022  2023

Walk-forward equity = OOS(2020) + OOS(2021) + OOS(2022) + OOS(2023)
```

### Steps

1. Define the in-sample (IS) window length (e.g., 2 years).
2. Define the out-of-sample (OOS) window length (e.g., 1 year).
3. Starting from the beginning of the data:
   a. Optimize all strategy parameters on the IS window.
   b. Lock the parameters — no changes.
   c. Run the strategy on the OOS window using those locked parameters.
   d. Record all trades and performance from the OOS window.
4. Roll both windows forward by the OOS length.
5. Repeat until all data is consumed.
6. Concatenate all OOS results → this is the walk-forward performance.

## Anchored vs Rolling

| Method | IS Window | OOS Window | Pros | Cons |
|---|---|---|---|---|
| **Rolling** | Fixed length, slides forward | Fixed length, follows IS | Adapts to regime changes; recent data weighted equally | May discard useful early data |
| **Anchored** | Starts at beginning, grows over time | Fixed length, follows IS | Uses all available history for optimization | Slower to adapt; early data may be irrelevant |

**Rolling example:** IS always 2 years, OOS always 1 year. Each window slides 1 year forward.

**Anchored example:** IS starts at 2018, grows (2018-19, 2018-20, 2018-21...), OOS always 1 year.

**Recommendation:** Use rolling for strategies expected to be regime-sensitive. Use anchored for strategies based on long-term structural edges.

## Choosing Window Sizes

### In-Sample (IS) Length

- Must be long enough to contain a statistically significant number of trades (≥ 50–100).
- Must contain at least one full market cycle (trend + range) if possible.
- Rule of thumb: 2–4× the OOS length.
- Too short → insufficient data for optimization → noisy parameters.
- Too long → stale data dominates → slow to adapt.

### Out-of-Sample (OOS) Length

- Must be long enough to generate ≥ 15–30 trades for meaningful evaluation.
- Must capture enough market conditions to be a fair test.
- Rule of thumb: 25–33% of IS length.
- Too short → too few trades → noisy evaluation.
- Too long → parameters may be stale by end of OOS window.

### Common Configurations

| Strategy Type | IS Length | OOS Length | IS:OOS Ratio |
|---|---|---|---|
| Daily swing | 2 years | 6 months | 4:1 |
| Daily position | 3 years | 1 year | 3:1 |
| Intraday | 6 months | 2 months | 3:1 |
| Weekly | 5 years | 2 years | 2.5:1 |

## Walk-Forward Efficiency (WFE)

The key metric for evaluating walk-forward results:

```
WFE = annualized_OOS_return / annualized_IS_return
```

Or equivalently using any consistent metric (Sharpe, expectancy):

```
WFE = OOS_metric / IS_metric
```

### Interpretation

| WFE | Interpretation | Action |
|---|---|---|
| > 0.70 | Excellent — strategy retains most of its edge OOS | Promote to paper |
| 0.50–0.70 | Good — meaningful edge preserved | Promote to paper with monitoring |
| 0.30–0.50 | Marginal — significant degradation from IS to OOS | Investigate; consider simplifying the strategy |
| < 0.30 | Poor — likely overfitted | Reject; too much edge is lost out-of-sample |
| < 0 | Failing — strategy loses money OOS | Reject outright |

### Why WFE Works

If a strategy is overfitted, it will have a high IS return (fit to noise) but a low or negative OOS return (noise doesn't repeat). WFE captures this gap directly.

A truly robust strategy captures a real market inefficiency that persists forward. Its WFE will be high because the edge is structural, not data-mined.

## Worked Example

### Setup

- **Strategy:** RSI mean-reversion on SPY daily.
- **Rule:** Buy when RSI(14) < 30, sell when RSI(14) > 70. Fixed 1% risk per trade.
- **Parameters to optimize:** RSI period (range 7–21), oversold threshold (25–35), overbought threshold (65–75).
- **Data:** 2016–2023 (8 years of daily data).
- **IS window:** 3 years. OOS window: 1 year.

### Execution

| Window | IS Period | OOS Period | Optimal RSI | Oversold | Overbought | IS Return | OOS Return |
|---|---|---|---|---|---|---|---|
| 1 | 2016–2018 | 2019 | 12 | 28 | 72 | 18.4% | 12.1% |
| 2 | 2017–2019 | 2020 | 14 | 30 | 70 | 16.2% | 8.7% |
| 3 | 2018–2020 | 2021 | 12 | 28 | 68 | 22.1% | 14.3% |
| 4 | 2019–2021 | 2022 | 14 | 32 | 72 | 19.8% | -2.1% |
| 5 | 2020–2022 | 2023 | 10 | 30 | 70 | 21.5% | 11.8% |

### Analysis

- **Average IS return:** 19.6%.
- **Average OOS return:** 8.96%.
- **WFE:** 8.96 / 19.6 = **0.457** (marginal — between 0.30 and 0.50).
- **OOS window 4 (2022):** negative return during a bear market. The mean-reversion strategy struggled when SPY trended down consistently (regime mismatch).
- **Parameter stability:** RSI period stayed between 10–14 across all windows (stable). Thresholds varied ±2–4 (stable). Good sign — parameters are not jumping wildly.

### Verdict

WFE of 0.457 is marginal. The strategy has a real edge but degrades significantly OOS, especially in trending markets (2022). Recommendations:
1. Add a regime filter (e.g., only trade when ADX < 25) to avoid trending markets.
2. Re-run WFA with the regime filter. If WFE improves to > 0.5 → proceed to paper.
3. If WFE doesn't improve → the strategy's edge is too small or inconsistent.

## Common WFA Mistakes

- **Too few windows.** Need ≥ 4 OOS windows for any reliability. Fewer = too much noise.
- **Peeking at OOS.** Adjusting the strategy after seeing OOS results, then re-testing → contaminates the walk-forward.
- **IS too short.** Not enough trades to optimize meaningfully → noisy parameters.
- **OOS too short.** Not enough trades to evaluate → can't distinguish signal from noise.
- **Ignoring regime.** A strategy that works in 4/5 windows but fails catastrophically in 1 may be regime-dependent. The failing window reveals the strategy's weakness, not the successful windows.
- **Cherry-picking WFE.** Calculating WFE only on the good windows. Must use ALL windows.

## When to Re-Run WFA

- **Annually:** as new data accumulates, re-run to confirm the edge persists.
- **After a losing streak:** if live performance diverges significantly from WFA expectations.
- **After a regime change:** if market conditions shift (e.g., from low-rate to high-rate environment).
- **After parameter drift:** if the optimal parameters are shifting significantly between windows, the edge may be unstable.

# Performance Metrics Glossary

Complete reference of every trading performance metric used in the journal system. Each metric includes its formula, interpretation, target range, and warning thresholds.

## Primary Metrics

### Win Rate

- **Formula:** `win_rate = winning_trades / total_trades`
- **Interpretation:** Percentage of trades that closed profitably (R > 0).
- **Target:** 40–60% (strategy-dependent; trend-following may be 35%, mean-reversion 55%).
- **Warning:** < 35% (review entry criteria) or > 70% (likely taking profits too early, R:R may be poor).
- **Note:** Win rate alone is meaningless — a 30% win rate with 5R avg winner beats a 70% win rate with 0.3R avg winner.

### Average R — Winners

- **Formula:** `avg_R_winners = sum(R_multiple for R > 0) / count(R > 0)`
- **Interpretation:** How much the average winning trade earns, measured in R.
- **Target:** > 1.5R (ideally 2R+).
- **Warning:** < 1.0R (winners are too small — likely exiting too early or targets too tight).

### Average R — Losers

- **Formula:** `avg_R_losers = sum(R_multiple for R < 0) / count(R < 0)`
- **Interpretation:** How much the average losing trade costs, in R. Should be close to -1.0R if stops are honored.
- **Target:** -0.8R to -1.0R.
- **Warning:** Worse than -1.5R (stops are not being honored, or slippage is excessive).

### Expectancy

- **Formula:** `expectancy = (win_rate × avg_R_winners) + (loss_rate × avg_R_losers)`
  - Where `loss_rate = 1 - win_rate`, and `avg_R_losers` is negative.
- **Interpretation:** Expected R-multiple per trade. Positive = the system makes money over many trades.
- **Target:** > 0.20R per trade.
- **Warning:** ≤ 0 (the system loses money — stop trading it).
- **Example:** win_rate=0.45, avg_win=2.0R, avg_loss=-0.9R → `(0.45 × 2.0) + (0.55 × -0.9) = 0.90 - 0.495 = 0.405R`

### Profit Factor

- **Formula:** `profit_factor = gross_profit / |gross_loss|`
  - `gross_profit = sum of all positive P&L`
  - `gross_loss = sum of all negative P&L` (absolute value in denominator)
- **Interpretation:** How many dollars won per dollar lost.
- **Target:** > 1.5.
- **Warning:** < 1.0 (losing money), 1.0–1.2 (barely profitable, fragile).

### Max Drawdown

- **Formula:** `max_drawdown = max((peak_equity - trough_equity) / peak_equity)` over all peak-to-trough intervals.
- **Interpretation:** Largest percentage decline from an equity peak before a new peak is made.
- **Target:** < 15%.
- **Warning:** > 20% (strategy or risk management needs review).
- **Calculation:**
  1. Track running peak of equity curve.
  2. At each point, compute `(peak - current) / peak`.
  3. Maximum of all those values = max drawdown.

### Sharpe Ratio

- **Formula:** `sharpe = (mean_return - risk_free_rate) / stdev_return`
  - **Annualized:** `sharpe_annual = sharpe_daily × sqrt(252)`
- **Interpretation:** Risk-adjusted return. Higher = better return per unit of volatility.
- **Target:** > 1.0 (good), > 2.0 (excellent).
- **Warning:** < 0.5 (poor risk-adjusted returns).
- **Note:** Uses total volatility (both up and down); penalizes upside volatility too. See Sortino for downside-only.

### Consecutive Losses (Current Streak)

- **Formula:** Count of sequential trades with R < 0 ending at the most recent trade.
- **Interpretation:** Measures current losing streak.
- **Target:** < 5.
- **Warning:** ≥ 5 (triggers soft kill review in safety-and-kill-switch).
- **Hard kill:** 3 consecutive stop-outs (full -1R losses) → hard kill.

## Secondary Metrics

### Sortino Ratio

- **Formula:** `sortino = (mean_return - risk_free_rate) / downside_deviation`
  - `downside_deviation = sqrt(mean(min(return - target, 0)²))`
- **Interpretation:** Like Sharpe but only penalizes downside volatility. Better for asymmetric return distributions.
- **Target:** > 1.5.
- **Warning:** < 0.7.

### Calmar Ratio

- **Formula:** `calmar = annualized_return / max_drawdown`
- **Interpretation:** Return relative to worst-case drawdown. Higher = better recovery characteristics.
- **Target:** > 1.0.
- **Warning:** < 0.5.

### Payoff Ratio (Win/Loss Ratio)

- **Formula:** `payoff_ratio = |avg_win| / |avg_loss|`
- **Interpretation:** How many times larger the average win is compared to the average loss.
- **Target:** > 2.0 (for trend strategies), > 1.0 (for high win-rate strategies).
- **Warning:** < 1.0 (average loss exceeds average win — only sustainable with very high win rate).

### Recovery Factor

- **Formula:** `recovery_factor = net_profit / |max_drawdown_dollars|`
- **Interpretation:** How many times the net profit exceeds the worst drawdown. Measures system robustness.
- **Target:** > 3.0.
- **Warning:** < 1.0 (system hasn't earned back its worst drawdown).

### Kelly Percentage

- **Formula:** `kelly% = W - (1 - W) / R`
  - Where `W = win_rate`, `R = payoff_ratio (avg_win / avg_loss)`
- **Interpretation:** Theoretically optimal fraction of capital to risk per trade for maximum geometric growth.
- **Target:** Use ¼ Kelly max (full Kelly is too aggressive for real trading).
- **Warning:** Kelly < 0 means the system has negative expectancy — do not trade.
- **Example:** W=0.45, R=2.2 → `0.45 - (0.55/2.2) = 0.45 - 0.25 = 0.20` → risk 20% per trade (full Kelly) → use 5% (¼ Kelly).

### Average Drawdown Duration

- **Formula:** Mean number of bars (or days) spent in drawdown across all drawdown periods.
- **Interpretation:** How long the equity curve typically stays below its peak.
- **Target:** < 15 trading days.
- **Warning:** > 30 trading days (extended flat/declining periods erode confidence and may signal regime mismatch).

### Equity Curve Slope

- **Formula:** Linear regression slope of the equity curve (equity vs trade number or time).
- **Interpretation:** Positive slope = growing equity. Steeper = faster growth. Negative = losing.
- **Target:** Positive and consistent (low R² is concerning even if slope is positive).
- **Warning:** Negative slope, or positive slope with R² < 0.5 (equity growth is noisy/unreliable).

### Ulcer Index

- **Formula:** `ulcer_index = sqrt(mean(drawdown_pct²))` over all observations.
  - Where `drawdown_pct = (peak - current) / peak × 100` at each point.
- **Interpretation:** Measures depth and duration of drawdowns combined. Lower is better.
- **Target:** < 5.
- **Warning:** > 10 (painful, extended drawdowns).

## R-Multiple Distribution Statistics

These describe the shape of the R-multiple distribution across all trades:

| Statistic | Formula | What it tells you |
|---|---|---|
| Mean R | `sum(all R) / count` | Same as expectancy — should be positive |
| Median R | Middle value when sorted | If median < mean, distribution is right-skewed (a few big wins pull the mean up) — fragile |
| Stdev R | Standard deviation of R | Lower = more consistent; target < 1.5R |
| Skew | Third moment | Positive skew = fat right tail (big wins) — desirable. Negative = fat left tail (big losses) — dangerous |
| Min R | Worst single trade | Should be ≥ -1.5R; if worse, stops were violated |
| Max R | Best single trade | If removing the best trade makes expectancy negative → system depends on outliers |
| % within ±1R | Trades between -1R and +1R | High % (>60%) means most trades are small — need the occasional big winner |

## Composite Health Score

A single number (0–100) summarizing overall system health:

```
health_score = (
    20 × normalize(expectancy, 0, 1.0) +
    20 × normalize(profit_factor, 1.0, 3.0) +
    15 × normalize(sharpe, 0, 2.0) +
    15 × (1 - normalize(max_drawdown, 0, 0.25)) +
    15 × normalize(win_rate, 0.3, 0.6) +
    15 × normalize(avg_R_winners, 1.0, 3.0)
)
```

Where `normalize(value, min, max)` clips to [0, 1].

| Score | Interpretation |
|---|---|
| 80–100 | Excellent — promote or maintain |
| 60–79 | Good — continue trading, monitor |
| 40–59 | Mediocre — review and optimize |
| 20–39 | Poor — consider pausing |
| 0–19 | Failing — stop trading, overhaul strategy |

## Metric Calculation Requirements

- **Minimum 30 trades** before any metric is considered meaningful.
- **Rolling 20-trade window** for trend detection (is performance improving or degrading?).
- **Bootstrap confidence intervals** (if enough data): resample trades with replacement, compute metric 1000 times, report 5th–95th percentile range.
- **Separate metrics by strategy** if running multiple strategies simultaneously.
- **Separate paper vs live** — never mix paper metrics with live metrics.

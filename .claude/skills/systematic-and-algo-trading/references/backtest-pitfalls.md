# Backtest Pitfalls

A comprehensive catalog of everything that can make a backtest misleading. For each pitfall: definition, example, how to detect it, and how to mitigate it.

## 1. Look-Ahead Bias

**Definition:** Using information that would not have been available at the time of the trading decision.

**Example:** A strategy that buys based on today's closing price but enters the order at today's open. In reality, you don't know the close until the close.

**How to detect:**
- Check if any indicator or signal uses data from the current bar's close/high/low when the entry is also on the current bar.
- Check if future data (tomorrow's earnings, next week's economic data) is used in today's decision.
- Verify that all data timestamps are strictly <= decision timestamp.

**How to mitigate:**
- Use only data from completed bars (signal on bar N → execute on bar N+1).
- When in doubt, add a 1-bar delay to every signal.

## 2. Survivorship Bias

**Definition:** Testing only on stocks/assets that still exist today, ignoring those that were delisted, went bankrupt, or were acquired.

**Example:** Backtesting a "buy cheap stocks" strategy on today's S&P 500 list. Stocks that were cheap and went bankrupt aren't in today's list, so the backtest only includes the survivors (which outperform by definition).

**How to detect:**
- Is the universe defined by today's membership list or historical membership at each point in time?
- Does the data include delisted stocks?

**How to mitigate:**
- Use survivorship-bias-free databases (e.g., CRSP, point-in-time index membership).
- Include delisted stocks with their actual returns (including -100% for bankruptcies).

## 3. Overfitting (Over-Optimization)

**Definition:** Adding too many parameters or rules until the strategy fits the noise in the historical data rather than capturing a genuine edge.

**Example:** A strategy with 12 parameters optimized on 3 years of daily data (750 bars). With 12 degrees of freedom, almost any random data set can be "profitably" fit.

**How to detect:**
- **Degrees-of-freedom ratio:** parameters / trades. If > 1/10, overfitting risk is high.
- **Equity curve too smooth:** real trading is messy. A backtest equity curve that rises smoothly without drawdowns is likely overfitted.
- **Parameter sensitivity:** if performance collapses when any parameter changes by 10%, the edge is in the noise, not the concept.
- **Walk-forward test:** WFE < 0.3 strongly suggests overfitting.

**How to mitigate:**
- Minimize the number of parameters (fewer = better).
- Use walk-forward analysis.
- Apply out-of-sample holdout.
- Prefer simple rules over complex ones (Occam's razor).

## 4. Curve Fitting

**Definition:** A specific form of overfitting where the strategy rules are tailored to match specific historical price patterns rather than capturing a generalizable edge.

**Example:** "Buy AAPL on the third Monday of March if the RSI(7) is between 42 and 47 and the 13-EMA is above the 37-SMA." These hyper-specific rules will match a handful of historical instances perfectly but have no predictive value.

**How to detect:**
- Do the rules have economic or behavioral logic? ("Buy when momentum confirms a breakout" = logical. "Buy when RSI is exactly 43.7" = curve fit.)
- Would you trust this rule in a market you've never seen before?
- Does the rule match <10 trades? Too few for statistical significance.

**How to mitigate:**
- Every rule must have a theoretical basis (why should this work?).
- Round parameters to sensible values (RSI 50, not 47.3).
- Test the concept, not just the parameters.

## 5. Data Snooping (Multiple Testing Bias)

**Definition:** Testing many strategy variations on the same dataset and selecting the best one, without adjusting for the number of strategies tested.

**Example:** Testing 200 indicator combinations on the same 5-year period. By pure chance, ~10 will appear profitable at the 5% significance level. Picking the best one and declaring it a "winning strategy" is data snooping.

**How to detect:**
- How many strategy variants were tested before arriving at this one?
- Was any adjustment made for multiple comparisons (Bonferroni, etc.)?
- Is there a clean out-of-sample period that was NEVER used during any testing?

**How to mitigate:**
- Reserve a true out-of-sample period that is touched only ONCE (final validation).
- Apply multiple-comparison correction (divide significance by number of strategies tested).
- Start with a hypothesis (why should this work?), then test it — don't mine data for patterns.

## 6. Ignoring Transaction Costs

**Definition:** Running a backtest without accounting for commissions, fees, and bid-ask spread costs.

**Example:** A high-frequency mean-reversion strategy shows 0.15% average profit per trade in backtest. But commissions are $0.005/share (0.05% at $10/share) and the spread costs another 0.05%. Real profit: 0.15% - 0.10% = 0.05% — barely positive and may be negative in practice.

**How to detect:**
- Does the backtest report include a "commissions" or "costs" line item?
- What commission rate was used? Is it realistic for the intended broker?
- For frequent trading (>5 trades/day), are costs a significant fraction of gross profit?

**How to mitigate:**
- Always include commissions at the broker's actual rate.
- Add spread cost: assume entry fill at ask (for buys) and exit fill at bid (for sells).
- If net profit is < 2× total costs → the strategy is fragile to cost changes.

## 7. Ignoring Slippage

**Definition:** Assuming fills at exact signal prices when real-world execution involves slippage (difference between expected and actual fill price).

**Example:** Strategy signals "buy at $100.00 limit." Backtest fills at $100.00. In reality, by the time the order reaches the exchange, the best offer might be $100.05 or $100.10. Over hundreds of trades, this adds up.

**How to detect:**
- Does the backtest use the signal price as the fill price?
- For market orders: what slippage assumption is applied?
- For limit orders: does the backtest assume fills at the limit price immediately when price touches it? (In reality, the order sits in queue and may not fill.)

**How to mitigate:**
- Market orders: add 1 tick of slippage for liquid instruments, 2–3 ticks for illiquid.
- Limit orders: assume fill only when price trades THROUGH the limit (not just touches it).
- Paper trading provides a partial (but still optimistic) slippage estimate.

## 8. Ignoring Market Impact

**Definition:** Assuming that the strategy's orders don't move the market. Valid for small accounts, invalid for large ones.

**Example:** A strategy buying $5M of a small-cap stock with $2M average daily volume. The buy order itself would move the price significantly. The backtest doesn't account for this.

**How to detect:**
- Compare typical position size to the asset's average daily volume.
- If position size > 1% of daily volume → market impact is non-trivial.

**How to mitigate:**
- Size limit: position notional < 0.5% of average daily volume for liquid stocks, < 0.1% for illiquid.
- For this agent (small account, $10k–$100k): market impact is negligible for liquid instruments. Flag only for micro-caps or low-volume crypto.

## 9. In-Sample / Out-of-Sample Confusion

**Definition:** Accidentally using out-of-sample data during optimization, or re-using the out-of-sample period after peeking at its results.

**Example:** You reserve 2024 as OOS. You optimize on 2020–2023. Results on 2024 look mediocre, so you tweak the strategy and test 2024 again. Now 2024 is no longer truly out-of-sample — you've contaminated it.

**How to detect:**
- How many times was the OOS period tested?
- Were any changes made after seeing OOS results?
- Is the OOS period truly untouched?

**How to mitigate:**
- The OOS holdout can be tested **exactly once**. If you need to iterate, use walk-forward analysis instead.
- Document every test run. If you've looked at OOS results → that period is contaminated → need a new OOS period.
- Best practice: use walk-forward (rolling IS/OOS windows) so there's no single sacred OOS period.

## 10. Optimization Bias (Selection Bias)

**Definition:** The best parameter set selected from an optimization is biased upward — it outperformed partly by chance, and that chance component won't repeat.

**Example:** Optimizing EMA crossover with periods 5–50. The best pair (12/34) returned 45% annually. But the median across all pairs was 8%. The 45% includes a large luck component.

**How to detect:**
- How much does the optimal result exceed the average of all parameter combinations?
- Is the optimal result an outlier compared to nearby parameters?

**How to mitigate:**
- Use the **median** of the top quartile of parameters, not the single best.
- Verify that nearby parameters also perform well (parameter stability).
- Apply walk-forward to see if the optimal parameters persist forward.

## Summary: Pitfall Severity Matrix

| Pitfall | Severity | Frequency | Detection Difficulty |
|---|---|---|---|
| Look-ahead bias | Critical | Common | Medium |
| Survivorship bias | High | Common | Easy |
| Overfitting | Critical | Very common | Hard |
| Curve fitting | Critical | Common | Medium |
| Data snooping | High | Very common | Hard |
| Ignoring costs | Medium | Common | Easy |
| Ignoring slippage | Medium | Common | Easy |
| Ignoring market impact | Low (for small accounts) | Rare | Easy |
| IS/OOS confusion | High | Common | Medium |
| Optimization bias | High | Very common | Medium |

## The Minimum Viable Backtest Checklist

Before accepting any backtest result as meaningful:

- [ ] Data is survivorship-bias free
- [ ] No look-ahead bias in signals or indicators
- [ ] Commissions included at realistic rates
- [ ] Slippage included (≥ 1 tick for liquid, more for illiquid)
- [ ] Out-of-sample or walk-forward validation performed
- [ ] Sample size ≥ 100 trades
- [ ] Parameters ≤ trades / 10
- [ ] Parameter sensitivity tested (±20%)
- [ ] Number of strategy variants tested is documented
- [ ] Results have economic/behavioral rationale (not just data-mined)

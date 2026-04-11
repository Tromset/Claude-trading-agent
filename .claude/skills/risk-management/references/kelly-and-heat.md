# Kelly, Portfolio Heat, and Drawdown Math

## Kelly derivation (short form)

Given:
- `p` = probability of winning a bet
- `q = 1 − p` = probability of losing
- `b` = payoff on a win per unit staked (so a $1 bet wins `b` dollars)
- `a` = loss on a loss per unit staked (typically `a = 1` — you lose your whole stake)

Kelly's fraction `f*` that maximizes the expected log-growth rate is:

```
f* = (p × b − q × a) / (a × b)     [general form]
   = (p × b − q) / b               [when a = 1]
```

**Example:** p = 0.55, b = 2, a = 1
```
f* = (0.55 × 2 − 0.45) / 2 = (1.10 − 0.45) / 2 = 0.325
```

Full Kelly says 32.5% per bet.

## Why full Kelly is dangerous

1. **Parameter sensitivity.** A 0.55 win-rate estimate might actually be 0.50; full Kelly is extremely sensitive to p. Overestimating p by 5% can flip the bet from positive to negative expectancy.

2. **Drawdown tolerance.** Full Kelly mathematically minimizes long-run expected log-wealth but routinely produces 50%+ peak-to-trough drawdowns. Humans (and risk committees) cannot tolerate this emotionally.

3. **Non-stationarity.** Market regimes change; Kelly assumes stationary distributions. They aren't.

4. **Sequencing risk.** A few bad draws early can cripple compounding, even in a positive-expectancy game.

## Fractional Kelly — the practical approach

Use **fractional Kelly** — ¼ to ½ of full Kelly — and cap at 2% per trade regardless.

In the example above:
- ¼ Kelly = 8.1%
- ½ Kelly = 16.3%

Still aggressive by retail standards. Most systematic funds operate at ½ Kelly or less and cap at 2% per trade.

**Recommended for this library:** fixed 1% per trade. This is approximately ⅛ Kelly for the example — highly conservative, resilient to parameter error, and survivable through long losing streaks.

## Risk of ruin (why 1% is the sweet spot)

Rough approximation of the probability of losing X% of the account after N consecutive losses at risk-per-trade `r`:

```
account after N losses ≈ account × (1 − r)^N
```

At `r = 0.01`:
- 10 losses in a row: 90.4% of account remaining
- 20 losses in a row: 81.8%
- 30 losses in a row: 73.9%

At `r = 0.05`:
- 10 losses: 59.9%
- 20 losses: 35.8%
- 30 losses: 21.5%

At `r = 0.10`:
- 10 losses: 34.9%
- 20 losses: 12.2%
- 30 losses: 4.2%

The difference between 1% and 10% is the difference between "bad streak" and "account destroyed." 1% also leaves psychological room to keep trading — the worst 10-loss streak still leaves >90% of capital intact, which is recoverable.

## Portfolio heat — formal model

Heat is the sum of per-trade risks as a fraction of equity:

```
heat = Σ (|entry_i − stop_i| × qty_i) / account_equity
```

**Default cap:** heat ≤ 6%.

With 1% per trade, that's 6 concurrent positions at maximum.

### Correlation adjustment (naive but useful)

Markets don't respect diversification when it matters most. Adjust heat for correlated positions:

```
effective_heat = heat_uncorrelated + 1.5 × heat_correlated
```

Treat as correlated:
- Multiple stocks in the same sector (e.g., two tech megacaps).
- Multiple FX pairs sharing a common currency (EURUSD and GBPUSD both have USD).
- Crypto pairs to the same reference (BTC + ETH both correlate).
- Index ETF + its largest components.

**Example:** 5 positions at 1% each, all uncorrelated → heat = 5%. OK.
Same 5 positions but all are tech megacaps → effective heat = 1.5 × 5% = 7.5%. Over cap. Reduce.

### Drawdown-adjusted heat

When the account is in drawdown, reduce the heat cap proportionally:

- Account at high-water mark → heat cap 6%
- Account 3% below HWM → heat cap 4%
- Account 6% below HWM → heat cap 2%
- Account 10%+ below HWM → heat cap 1%, serious review required

This "de-leveraging in drawdown" protocol prevents tilt-driven acceleration of losses.

## Session-level caps

| Metric | Hard cap | Soft cap |
|---|---|---|
| Daily loss | 3% | 2% |
| Weekly loss | 6% | 4% |
| Monthly loss | 12% | 8% |
| Consecutive stop-outs | 3 | 2 |

Hard caps trigger `safety-and-kill-switch` hard kill.
Soft caps trigger soft kill (no new X, existing positions held).

## Heat math — worked example

Account: $100,000. Current positions:

| # | Ticker | Qty | Entry | Stop | Per-trade risk | Correlated? |
|---|---|---|---|---|---|---|
| 1 | AAPL | 50 | 180 | 175 | $250 | (tech) |
| 2 | MSFT | 20 | 400 | 390 | $200 | (tech, corr to #1) |
| 3 | KO | 100 | 62 | 60 | $200 | (consumer) |
| 4 | JNJ | 30 | 150 | 147 | $90 | (healthcare) |

Raw heat = (250 + 200 + 200 + 90) / 100,000 = 0.74%.

Correlation adjustment: #1 and #2 are correlated → combined risk = (250 + 200) × 1.5 = $675
Effective risk = 675 + 200 + 90 = $965
Effective heat = 0.965%.

Both well under cap. Room for another ~5% of heat.

Now consider adding a 5th position, a tech stock:
Position 5: NVDA, qty 10, entry 900, stop 880 → per-trade risk $200.
New tech combined risk = (250 + 200 + 200) × 1.5 = $975
Effective risk = 975 + 200 + 90 = $1,265
Effective heat = 1.265% — still OK.

But notice: the marginal tech position cost 1.5× its raw risk in "effective heat" because it increased the correlated bucket. This is why the correlation adjustment matters — it disincentivizes over-concentration.

## Takeaways

1. **Use fixed 1% per trade by default.**
2. **Kelly is a reference, not a daily tool.**
3. **Heat cap 6%, with correlation adjustment.**
4. **De-leverage in drawdown.**
5. **Session caps are hard; kill-switch is the enforcement mechanism.**

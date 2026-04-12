# Momentum Indicators Reference

Momentum indicators measure the RATE of price change — how fast price is moving, whether it is accelerating or decelerating, and whether it is reaching exhaustion levels. They excel at identifying divergences (price vs. momentum disagreement) and overbought/oversold conditions.

---

## Relative Strength Index (RSI)

### Formula intuition
RSI compares the magnitude of recent gains to recent losses over N periods, normalized to a 0-100 scale. RSI = 100 - (100 / (1 + RS)), where RS = average gain / average loss over N periods. High RSI = gains dominating; low RSI = losses dominating.

### Default settings
- Period: 14 (Wilder standard).
- Overbought threshold: 70.
- Oversold threshold: 30.
- Alternative settings: RSI(7) or RSI(9) for day trading; RSI(21) for position trading.

### Interpretation
- RSI > 70: overbought — momentum stretched to upside. NOT an automatic sell signal in trends.
- RSI < 30: oversold — momentum stretched to downside. NOT an automatic buy signal in downtrends.
- RSI 40-60: neutral zone — no directional momentum edge.
- Centerline (50): in uptrends, RSI tends to stay above 40 and bounce from 40-50. In downtrends, RSI tends to stay below 60 and reject from 50-60.

### Divergence rules
- **Bullish divergence:** price makes a lower low, RSI makes a higher low. Interpretation: downward momentum is weakening. Supports X consideration.
- **Bearish divergence:** price makes a higher high, RSI makes a lower high. Interpretation: upward momentum is weakening. Supports Y consideration.
- **Hidden bullish divergence:** price makes a higher low, RSI makes a lower low. Interpretation: trend continuation (bullish).
- **Hidden bearish divergence:** price makes a lower high, RSI makes a higher high. Interpretation: trend continuation (bearish).

Divergence is a WARNING, not an immediate entry signal. Wait for price confirmation (break of structure, candle pattern) before acting.

### When to use
- Mean-reversion: buy oversold (< 30) in uptrends, sell overbought (> 70) in downtrends.
- Divergence detection: highest-probability momentum signal.
- Trend strength filtering: in a strong uptrend, RSI rarely drops below 40.

### Failure modes
- **Overbought does not mean sell.** In strong uptrends, RSI can remain above 70 for extended periods. Selling solely because RSI > 70 in a bull trend is a losing strategy.
- **Oversold does not mean buy.** In strong downtrends, RSI can remain below 30.
- **Divergence can persist.** Multiple divergences can form before price reverses. Divergence indicates weakening momentum, not an immediate reversal.
- **Period sensitivity.** RSI(7) gives more signals but more noise; RSI(21) gives fewer but more reliable.

---

## MACD (Moving Average Convergence Divergence)

### Formula intuition
MACD measures the relationship between two EMAs of different lengths. The MACD line is the difference between the fast EMA and the slow EMA. When the fast EMA pulls away from the slow EMA, momentum is increasing. The signal line smooths the MACD line; the histogram shows the gap between them.

### Components
- **MACD Line:** EMA(12) - EMA(26).
- **Signal Line:** EMA(9) of the MACD Line.
- **Histogram:** MACD Line - Signal Line.

### Default settings
- Fast EMA: 12, Slow EMA: 26, Signal EMA: 9.
- Alternative: (5, 35, 5) for slower signals; (8, 17, 9) for faster.

### Interpretation
- **MACD Line > 0:** fast EMA above slow EMA = bullish momentum.
- **MACD Line < 0:** fast EMA below slow EMA = bearish momentum.
- **Signal cross bullish:** MACD Line crosses above Signal Line = buy signal.
- **Signal cross bearish:** MACD Line crosses below Signal Line = sell signal.
- **Zero-line cross:** MACD crossing above zero = trend turning bullish; below zero = turning bearish. This is equivalent to a 12/26 EMA cross.
- **Histogram expanding:** momentum accelerating in the current direction.
- **Histogram contracting:** momentum decelerating — early sign of crossover coming.

### Divergence rules
- **Bullish divergence:** price lower low, MACD higher low. Often best seen on histogram.
- **Bearish divergence:** price higher high, MACD lower high.
- MACD histogram divergence (the histogram makes a shallower peak while price makes a higher high) is often earlier than MACD line divergence.

### When to use
- Trend-following: zero-line crosses confirm trend direction.
- Entry timing: signal line crosses within the context of a larger trend.
- Divergence: particularly effective on daily timeframe.

### Failure modes
- **Whipsaw in ranges.** The MACD will oscillate around zero with frequent signal crosses that go nowhere.
- **Lag.** MACD is derived from EMAs — it is inherently lagging. By the time a zero-line cross fires, significant price movement has already occurred.
- **No bounded range.** MACD is unbounded; you cannot compare "overbought" levels across different instruments or timeframes.
- **Histogram does not measure volume.** The histogram shows momentum gap speed, not participation.

---

## Stochastic Oscillator

### Formula intuition
Measures where the current close sits relative to the high-low range over N periods. %K = (Close - Lowest Low) / (Highest High - Lowest Low) × 100. If close is at the top of the range, stochastic is near 100; at the bottom, near 0.

### Components
- **%K (fast line):** raw stochastic over N periods.
- **%D (signal line):** SMA(3) of %K.

### Default settings
- %K period: 14, %D smoothing: 3, slowing: 3.
- Fast stochastic: %K = 5, %D = 3 (more responsive, more noise).
- Slow stochastic: applies additional smoothing to %K.

### Interpretation
- %K > 80: overbought zone.
- %K < 20: oversold zone.
- %K crossing above %D in oversold zone: bullish signal.
- %K crossing below %D in overbought zone: bearish signal.
- Stochastic cycles faster than RSI — more signals, more noise.

### Divergence rules
Same structure as RSI divergence:
- Bullish: price lower low, stochastic higher low.
- Bearish: price higher high, stochastic lower high.

### When to use
- Ranging markets: excellent for timing entries/exits in defined ranges.
- Short-term swing trades where you need faster cycle signals than RSI provides.
- Confirmation of oversold/overbought alongside RSI (only if documented as an exception to the redundancy rule).

### Failure modes
- **Embeds in trends.** In a strong uptrend, stochastic will peg above 80 for extended periods. Selling because stochastic > 80 in a trend is premature.
- **Too many signals.** The fast cycling means many crosses that do not follow through.
- **Sensitive to the lookback period.** A 5-period stochastic is radically different from a 14-period.
- **Not meaningful in low-volatility compressions** where the high-low range is narrow.

---

## Commodity Channel Index (CCI)

### Formula intuition
CCI measures how far the current typical price (H+L+C)/3 deviates from its SMA, normalized by the mean deviation. CCI = (Typical Price - SMA of Typical Price) / (0.015 × Mean Deviation). The 0.015 constant scales so that roughly 75% of values fall between -100 and +100.

### Default settings
- Period: 20.
- Overbought: +100.
- Oversold: -100.

### Interpretation
- CCI > +100: price is above normal range — overbought or strong trend.
- CCI < -100: price is below normal range — oversold or strong downtrend.
- Zero-line crosses: similar to MACD zero-line, indicates shift in bias.
- CCI > +200 or < -200: extreme momentum — possible exhaustion.

### When to use
- Identifying momentum extremes in commodity and equity markets.
- Mean-reversion signals when CCI reverts from extreme to normal range.
- Trend-following: CCI rising above +100 can signal trend initiation.

### Failure modes
- Unbounded: extreme values in strong trends do not imply reversal.
- Less commonly used than RSI/MACD — less community validation and fewer tested strategies.
- The 0.015 constant is arbitrary (designed by Donald Lambert for a specific statistical property) and may not generalize.

---

## Williams %R

### Formula intuition
Mathematically identical to an inverted stochastic %K. Williams %R = (Highest High - Close) / (Highest High - Lowest Low) × -100. Ranges from -100 (oversold) to 0 (overbought). Note the inverted scale.

### Default settings
- Period: 14.
- Overbought: -20 (close near the top of range).
- Oversold: -80 (close near the bottom of range).

### Interpretation
- %R > -20: overbought.
- %R < -80: oversold.
- Movement from oversold toward -50: early bullish momentum.
- Movement from overbought toward -50: early bearish momentum.

### When to use
- Quick-cycling overbought/oversold for short-term trades.
- Failure swings: %R failing to reach the prior extreme on the next cycle is a divergence signal.

### Failure modes
- Nearly identical to Stochastic in information content. Using both violates the redundancy rule.
- Inverted scale is counterintuitive and causes interpretation errors.
- Same trend-embedding problem as Stochastic — pegs at extremes in strong trends.

---

## Rate of Change (ROC)

### Formula intuition
The simplest momentum measure: percentage change over N periods. ROC = ((Close - Close_N_periods_ago) / Close_N_periods_ago) × 100. Positive ROC = price higher than N bars ago; negative = lower.

### Default settings
- Period: 12 or 14.
- Some systems use ROC(1) as a momentum filter (1-bar rate of change).

### Interpretation
- ROC > 0: bullish momentum over the lookback.
- ROC < 0: bearish momentum.
- ROC rising: momentum accelerating.
- ROC falling from high levels: momentum decelerating (not necessarily reversing).
- Extreme ROC readings (>2 standard deviations from mean): possible exhaustion.

### When to use
- Simplest possible momentum read — useful for screening.
- Comparing momentum across instruments (normalize by historical ROC range).
- Mean-reversion: extremely negative ROC in an uptrend = potential oversold bounce.

### Failure modes
- Unbounded and context-dependent — what is "extreme" varies by instrument and regime.
- Highly sensitive to the base bar (N periods ago). A single outlier bar distorts the reading.
- Does not account for path — the same 5% ROC could result from steady drift or a spike-and-retrace.

---

## General guidelines for momentum indicator usage

1. **Divergence is the highest-value signal** momentum indicators produce. Levels (overbought/oversold) are secondary.
2. **Respect the regime.** Overbought/oversold levels work in ranges; in trends, momentum can embed at extremes for prolonged periods.
3. **Combine with price action.** A momentum signal without a corresponding price structure confirmation (e.g., break of swing low) is incomplete.
4. **One momentum indicator per decision.** RSI and MACD measure different aspects (bounded levels vs. unbounded momentum shift), which justifies occasional dual use. But RSI + Stochastic + Williams %R is pure redundancy.
5. **Divergence confirmation:** wait for the oscillator to actually turn (e.g., RSI trough above the prior trough AND rising) before acting. Divergence can extend with multiple occurrences before price responds.
6. **Histogram watching:** MACD histogram contracting toward zero is an early warning of a signal cross — this precedes the actual cross and can aid timing.

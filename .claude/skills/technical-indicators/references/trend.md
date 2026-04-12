# Trend Indicators Reference

Trend indicators answer two questions: (1) What direction is price moving? (2) How strong is the trend? They work best in trending regimes and produce whipsaws in ranges.

---

## Simple Moving Average (SMA)

### Formula intuition
The arithmetic mean of the last N closing prices. Each bar carries equal weight. SMA(20) = sum of last 20 closes / 20.

### Default settings
- Short-term: SMA(10), SMA(20)
- Medium-term: SMA(50)
- Long-term: SMA(100), SMA(200)

### When to use
- Identifying the trend direction: price above SMA = bullish bias, price below = bearish bias.
- Dynamic support/resistance: price often bounces off the 20 or 50 SMA in trends.
- Cross signals (see Moving Average Crosses below).

### Failure modes
- Lags significantly on fast moves; the longer the period, the more lag.
- Whipsaws in ranging markets — price crosses the SMA repeatedly with no follow-through.
- Equal weighting means a large bar N periods ago affects today's value just as much as yesterday's bar (the "drop-off effect").

---

## Exponential Moving Average (EMA)

### Formula intuition
A weighted moving average where recent bars carry exponentially more weight. The smoothing factor = 2 / (N + 1). EMA(20) weights yesterday's close more than 10 days ago.

### Default settings
- Day trading: EMA(9), EMA(21)
- Swing: EMA(20), EMA(50)
- Position: EMA(50), EMA(200)

### When to use
- When you need faster response to price changes than SMA provides.
- Crossover systems where speed matters more than smoothness.
- Dynamic trailing stops (price closing below the EMA triggers exit consideration).

### Failure modes
- More responsive means more false signals in choppy markets.
- Still lags — just less than SMA.
- Does not eliminate whipsaw, only reduces lag.

---

## Weighted Moving Average (WMA)

### Formula intuition
Each bar is weighted linearly: the most recent bar gets weight N, the second most recent gets N-1, etc. The denominator is the sum of weights (N×(N+1)/2). More emphasis on recent data than SMA but less than EMA.

### Default settings
- WMA(10), WMA(20) — less commonly used than SMA/EMA.

### When to use
- When you want a middle ground between SMA and EMA responsiveness.
- Some volume-price weighted systems use WMA internally.

### Failure modes
- Rarely used in practice; community and strategy literature predominantly reference SMA/EMA.
- Marginal improvement over EMA does not justify the added complexity for most traders.

---

## Moving Average Crosses

### Golden Cross
- Definition: 50-period MA crosses ABOVE the 200-period MA.
- Interpretation: major bullish trend shift. Institutional benchmark signal.
- Lag: extremely lagging (by the time it fires, price has moved significantly). Best used as trend confirmation rather than entry timing.

### Death Cross
- Definition: 50-period MA crosses BELOW the 200-period MA.
- Interpretation: major bearish trend shift.
- Lag: same as golden cross — confirms what price action already showed.

### Short-term crosses
- EMA(9)/EMA(21): faster signals for swing/day trading.
- EMA(12)/EMA(26): the MACD default — see momentum reference.

### When to use
- Trend confirmation after a structural break.
- Filtering: only take longs when fast MA > slow MA; only take shorts when fast MA < slow MA.

### Failure modes
- Catastrophic in ranges: rapid alternation of golden/death crosses = whipsaw losses.
- The signal fires AFTER the move starts; never front-run a cross that has not occurred.
- Works best on daily and weekly timeframes; lower timeframes produce excessive noise.

---

## Average Directional Index (ADX)

### Formula intuition
ADX measures the STRENGTH of a trend regardless of direction. It is derived from the smoothed difference between +DI and -DI (Directional Indicators). ADX is always positive; it tells you how trendy the market is, not which way it trends.

### Default settings
- ADX(14) — the Wilder standard.

### Interpretation thresholds
| ADX Value | Market condition |
|---|---|
| < 20 | No meaningful trend (range-bound) |
| 20 - 25 | Trend emerging |
| 25 - 40 | Healthy trending market |
| 40 - 50 | Strong trend |
| > 50 | Extremely strong trend (exhaustion risk) |

### When to use
- **Regime detection:** ADX < 20 → apply range strategies; ADX > 25 → apply trend strategies.
- **Filter:** only take trend-following signals when ADX > 20 and rising.
- **Exhaustion warning:** ADX > 50 and turning down may indicate trend is decelerating.

### Failure modes
- ADX measures strength, NOT direction. A falling ADX does not mean price is falling — it means the trend is weakening (could be consolidation before continuation).
- Lags: ADX uses 14-period smoothing of an already-smoothed calculation. It is slow to react.
- ADX can remain elevated during pullbacks within a strong trend, giving false comfort.

---

## Directional Movement Index (DMI): +DI / -DI

### Formula intuition
+DI measures upward directional movement (today's high minus yesterday's high, if positive and greater than downward movement). -DI measures downward directional movement. Both are normalized by ATR and smoothed over N periods.

### Default settings
- DMI(14) — typically paired with ADX(14).

### Interpretation
- +DI > -DI → bullish pressure dominates.
- -DI > +DI → bearish pressure dominates.
- +DI crossing above -DI = bullish signal (when confirmed by ADX > 20).
- -DI crossing above +DI = bearish signal.

### When to use
- Directional confirmation alongside ADX.
- Entry timing: DI cross with ADX > 25 and rising.

### Failure modes
- DI crosses whipsaw when ADX < 20. Always check ADX first.
- The extreme point rule (Wilder's original): on the day of a +DI/-DI cross, note the extreme price. Only act if price breaks that extreme. This reduces false signals but is often ignored.

---

## Ichimoku Cloud (Ichimoku Kinko Hyo)

### Components and formula intuition
| Component | Calculation | Purpose |
|---|---|---|
| Tenkan-sen (Conversion) | (9-period high + 9-period low) / 2 | Short-term equilibrium |
| Kijun-sen (Base) | (26-period high + 26-period low) / 2 | Medium-term equilibrium |
| Senkou Span A (Leading A) | (Tenkan + Kijun) / 2, plotted 26 periods ahead | Cloud boundary (faster) |
| Senkou Span B (Leading B) | (52-period high + 52-period low) / 2, plotted 26 periods ahead | Cloud boundary (slower) |
| Chikou Span (Lagging) | Close plotted 26 periods behind | Confirmation |

### Default settings
- 9, 26, 52 (designed for a 6-day trading week; some adapt to 10, 30, 60 for 5-day weeks).

### Interpretation
- Price above cloud: bullish trend. Price below cloud: bearish trend. Price inside cloud: no clear trend.
- Cloud color: Senkou A > Senkou B = bullish cloud (green). Senkou A < Senkou B = bearish cloud (red).
- Tenkan/Kijun cross: similar to fast/slow MA cross but within the Ichimoku framework.
- Cloud thickness: thick cloud = strong support/resistance; thin cloud = weak, breakout likely.
- Chikou above price (from 26 bars ago) = bullish confirmation.

### When to use
- Multi-factor trend analysis in a single indicator (replaces separate MA + support/resistance work).
- Best on daily and weekly charts.
- Strong at identifying support/resistance zones (the cloud itself).

### Failure modes
- Extremely cluttered on lower timeframes (< 1 hour). Not designed for scalping.
- Default parameters were built for Japanese equity markets in the 1960s. Crypto and forex may need adjustment.
- The cloud "looks ahead" 26 periods — this is a projection, not a prediction.
- In ranging markets, all five lines converge and produce conflicting signals.

---

## Parabolic SAR (Stop And Reverse)

### Formula intuition
Plots dots above (bearish) or below (bullish) price. The dots accelerate toward price as the trend continues (via an acceleration factor that starts at 0.02 and increases by 0.02 on each new extreme, capped at 0.20). When price touches the dot, the trend "reverses" and dots flip.

### Default settings
- AF start: 0.02, AF increment: 0.02, AF max: 0.20.

### When to use
- Trailing stop placement: use the SAR dot as a dynamic trailing stop.
- Trend reversal signal: dots flipping from above to below = bullish; below to above = bearish.
- Works well in strong trends with clear directional moves.

### Failure modes
- Whipsaws badly in ranges — dots flip constantly, generating false reversal signals.
- The acceleration factor makes the SAR "chase" price; in a consolidation after a strong move, it catches up and falsely triggers a reversal.
- Not useful for entry timing — better as a stop/exit tool.
- Must be combined with a regime filter (ADX > 20) to avoid range whipsaws.

---

## General guidelines for trend indicator usage

1. Use ADX first to determine if a trend exists. If ADX < 20, trend indicators will whipsaw.
2. Use MAs for direction (above/below, cross). Use ADX/DMI for strength.
3. Ichimoku is a standalone system — do not redundantly combine it with MAs and ADX.
4. Parabolic SAR is a stop tool, not a standalone entry signal.
5. On higher timeframes (daily+), trend indicators are more reliable. On lower timeframes, expect more noise.
6. A moving average cross is a lagging confirmation, not a leading signal. The actual signal was the price action break; the cross confirms.

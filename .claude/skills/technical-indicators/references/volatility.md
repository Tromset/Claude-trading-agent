# Volatility Indicators Reference

Volatility indicators measure the WIDTH of price movement — how much price oscillates within a given period. They do not indicate direction. Their primary uses: regime detection (trending vs. ranging), stop/target placement, and identifying breakout potential from compression.

---

## Average True Range (ATR)

### Formula intuition
ATR is the smoothed average of the True Range over N periods. True Range = max(High - Low, |High - Previous Close|, |Low - Previous Close|). It captures gaps and the full bar range. ATR(14) is the 14-period average of this value, giving a measure of how much the instrument moves per bar in absolute price terms.

### Default settings
- Period: 14 (Wilder standard).
- Alternative: ATR(10) for day trading, ATR(20) for position trading.

### Interpretation
- ATR is measured in the instrument's price units (dollars, pips, etc.).
- Rising ATR: volatility expanding — larger bars, more movement per unit time.
- Falling ATR: volatility contracting — smaller bars, consolidation.
- ATR does NOT indicate direction. A rising ATR in a downtrend means volatility is increasing to the downside.

### Use cases

#### Stop placement
The primary use of ATR in a trading system is stop distance calibration.
- Standard ATR stop: 1.5 x ATR(14) from entry.
- Tight: 1.0 x ATR (higher risk of noise stop-out).
- Wide: 2.0 x ATR (lower risk of noise, more capital at risk per share).
- Chandelier Exit: highest high minus N x ATR (trailing stop for trends).

#### Target placement
- Minimum target: 2 x stop distance (which is already ATR-derived).
- ATR-based targets: 2-3 x ATR(14) for intraday targets; 4-6 x ATR(14) for swing targets.

#### Position sizing
ATR normalizes position sizes across instruments of different volatility. A $500 stock with ATR $2 is less volatile (percentage-wise) than a $20 stock with ATR $1.50. The risk-management skill uses ATR directly in its sizing formula.

#### Regime detection
- ATR at 6-month lows: low volatility regime — expect breakout setup.
- ATR at 6-month highs: high volatility regime — widen stops, reduce size.

### Failure modes
- ATR spikes on gap days (earnings, news) and may not represent ongoing volatility.
- ATR is backward-looking — it cannot predict future volatility, only summarize recent volatility.
- Using a fixed ATR multiple without adjusting for regime change leads to stops that are too tight in expanding vol and too wide in contracting vol.
- ATR does not distinguish between bullish and bearish volatility.

---

## Bollinger Bands

### Formula
- Middle Band: SMA(20) of close.
- Upper Band: SMA(20) + (2 x standard deviation of close over 20 periods).
- Lower Band: SMA(20) - (2 x standard deviation of close over 20 periods).

### Default settings
- Period: 20, Standard deviations: 2.
- Alternatives: (20, 1.5) for tighter bands; (20, 2.5) for wider; (50, 2) for longer-term.

### Interpretation
- Statistically, ~95% of price action should occur within 2 standard deviation bands.
- Price touching the upper band: not inherently bearish — in trends, price "walks the band."
- Price touching the lower band: not inherently bullish — in downtrends, price walks the lower band.
- **Bandwidth** = (Upper - Lower) / Middle. Measures relative band width.

### Key patterns

#### Bollinger Squeeze
- Bands contract to a narrow width (bandwidth at multi-period low).
- Interpretation: low volatility precedes high volatility. A breakout is building.
- Direction is NOT predicted by the squeeze — the breakout can go either way.
- Confirm direction with price action (break of structure) or volume.

#### Bollinger Expansion
- Bands widen rapidly after a squeeze.
- The first thrust out of a squeeze is typically the tradable move.
- Once bands reach maximum width and begin contracting, the trend is losing steam.

#### Bollinger Bounce (mean-reversion)
- In a ranging market, price tends to bounce from the lower band toward the middle and from the upper band toward the middle.
- Only valid in ranges (ADX < 20). In trends, price walks the band and does not mean-revert.

#### Squeeze breakout strategy
1. Identify bands at narrowest width in 120+ bars.
2. Wait for price to close outside the band.
3. Confirm with volume expansion.
4. Enter in breakout direction with stop at the opposite band or at the pre-squeeze low/high.

### Failure modes
- **Band-walking in trends.** Price can hug the upper band for weeks in a strong uptrend. Fading the upper band in this context is a losing trade.
- **Squeeze duration uncertainty.** A squeeze can last much longer than expected — there is no time limit on low-vol consolidation.
- **Standard deviation assumption.** Bollinger Bands assume normally distributed returns, which financial markets violate (fat tails).
- **Not a standalone system.** Band touches are conditions, not signals. Combine with momentum or volume.

---

## Keltner Channels

### Formula
- Middle Line: EMA(20) of close.
- Upper Channel: EMA(20) + (1.5 x ATR(10)).
- Lower Channel: EMA(20) - (1.5 x ATR(10)).

### Default settings
- EMA period: 20, ATR period: 10, ATR multiplier: 1.5.
- Alternative: EMA(20), ATR(14), multiplier 2.0 for wider channels.

### Interpretation
- Similar concept to Bollinger Bands but uses ATR instead of standard deviation.
- ATR-based bands are smoother and less reactive to single outlier bars.
- Price above upper channel: strong bullish momentum.
- Price below lower channel: strong bearish momentum.
- Price within channels: normal trading range.

### Keltner + Bollinger Squeeze confirmation
- When Bollinger Bands move INSIDE Keltner Channels, volatility is extremely compressed.
- This "squeeze within a squeeze" (TTM Squeeze concept) is a high-probability setup for a directional breakout.
- Bollinger Bands expanding back outside Keltner = squeeze "fired."

### When to use
- Trend-following: trade in the direction of price when it closes beyond the channel.
- Squeeze detection: combine with Bollinger Bands for higher-confidence squeeze signals.
- Stop placement: use the channel boundary as a dynamic trailing stop.

### Failure modes
- Less popular than Bollinger Bands — fewer community-tested strategies.
- In extremely low ATR environments, channels become too narrow and produce false breakout signals.
- Does not distinguish between organic volatility and gap-driven volatility (same issue as ATR).

---

## Donchian Channels

### Formula
- Upper Channel: highest high of the last N periods.
- Lower Channel: lowest low of the last N periods.
- Middle Line: (Upper + Lower) / 2.

### Default settings
- Period: 20 (the "Turtle Trading" breakout system used 20/55).
- Alternative: 10 for shorter-term breakout; 55 for longer-term trend.

### Interpretation
- Price breaking above the upper channel (20-period high): bullish breakout signal.
- Price breaking below the lower channel (20-period low): bearish breakout signal.
- Channel width = volatility. Narrow channels = low vol, wide = high vol.
- The 20-period Donchian breakout is one of the oldest systematic trend-following methods (Turtle Traders).

### When to use
- Breakout trading: buy new 20-period highs, sell new 20-period lows.
- Trend-following systems: entry on 20-period breakout, exit on 10-period opposite breakout.
- Stop placement: the opposite channel boundary as a natural stop level.

### Failure modes
- **False breakouts in ranges.** Price can briefly poke above a 20-period high and immediately reverse. The solution: require a full bar close beyond the channel, not just an intrabar wick.
- **Late entries.** By definition, you are buying at the highest price of the last 20 periods — psychologically difficult and often late.
- **No built-in exit optimization.** The exit channel (e.g., 10-period) may give back significant profits in a trend before triggering.

---

## Standard Deviation

### Formula intuition
Standard deviation of closing prices over N periods measures dispersion — how spread out recent prices are from their mean. It is the building block of Bollinger Bands and many volatility metrics.

### Default settings
- Typically computed over 20 periods (same as Bollinger Bands).

### Interpretation
- Low standard deviation: prices clustered tightly — low vol, potential breakout building.
- High standard deviation: prices dispersed — high vol, trending or chaotic.
- Standard deviation can be normalized by dividing by the mean (coefficient of variation) for cross-instrument comparison.

### When to use
- Raw volatility measurement for quantitative models.
- Input to other indicators (Bollinger Bands, z-scores).
- Regime classification: compare current StdDev to its own historical percentile.

### Failure modes
- Assumes normal distribution — financial returns have fat tails (extreme moves are more common than a normal distribution predicts).
- Backward-looking — past volatility may not predict future volatility, especially around events (earnings, FOMC).
- Sensitive to outliers — a single extreme bar inflates the standard deviation and may not represent the "average" volatility.

---

## Historical vs. Implied Volatility

### Historical volatility (HV)
- Computed from actual past price data (annualized standard deviation of log returns).
- Default: HV(20) = 20-day historical vol, annualized.
- Tells you what volatility WAS.

### Implied volatility (IV)
- Derived from option prices via Black-Scholes or similar models.
- Tells you what the market EXPECTS volatility to be over the option's life.
- IV > HV: the market is pricing in more volatility than recent history — fear premium or expected event.
- IV < HV: the market is pricing in less volatility — complacency or post-event normalization.

### IV Rank and IV Percentile
- **IV Rank:** (Current IV - 52-week IV Low) / (52-week IV High - 52-week IV Low). Shows where current IV sits in its annual range.
- **IV Percentile:** percentage of days in the past year that IV was below the current level.
- IV Rank > 50% or IV Percentile > 80%: volatility is elevated — potential for premium selling strategies.

### When to use
- Options strategies: high IV = sell premium (iron condors, credit spreads); low IV = buy premium (long straddles).
- Equity trading context: elevated IV often coincides with fear/uncertainty — mean-reversion strategies may find opportunity.
- Pre-earnings: IV spikes before earnings and crushes after. This "vol crush" is a core options concept.

### Failure modes
- IV is a market consensus, not a prediction — the market can be wrong.
- IV smile/skew: IV is not uniform across strikes. OTM puts often have higher IV than ATM options (skew).
- HV is purely backward-looking and provides no edge on future volatility if the regime has changed.
- Comparing HV to IV across different instruments without normalization is meaningless.

---

## General guidelines for volatility indicator usage

1. **Volatility is regime, not signal.** Use volatility indicators to DETERMINE which strategy to apply, not to generate buy/sell signals directly.
2. **Low vol precedes high vol.** The most important volatility pattern: prolonged compression leads to expansion. Trade the direction of the breakout, not the compression itself.
3. **ATR is your stop tool.** Every stop should be validated against ATR. A stop tighter than 1.0 x ATR is likely to be noise-stopped.
4. **Bollinger + Keltner for squeeze.** When Bollinger Bands contract inside Keltner Channels, a high-energy breakout is building.
5. **Normalize across instruments.** Use ATR as a percentage of price (ATR / Price) to compare volatility across instruments of different price levels.
6. **Vol expansion = widen stops and reduce size.** Never keep the same position size when volatility doubles.
7. **Vol contraction = opportunity.** Tight ranges resolve into trends. Patience during the squeeze is rewarded by the breakout.

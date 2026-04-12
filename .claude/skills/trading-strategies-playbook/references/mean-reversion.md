# Mean Reversion — Reference

Counter-trend trading in range-bound markets. Mean reversion bets that price will return to its average (VWAP, moving average, or midline of a range) after an extreme extension. Only valid when the market is NOT trending.

## Core rule

**Mean reversion is ONLY valid when ADX(14) < 20 on the analysis timeframe.** Trading mean reversion in a trending market is the single most expensive tactical mistake. If ADX >= 20, this strategy is disabled — route to swing or trend-following instead.

## Prerequisites

- ADX(14) on the analysis timeframe < 20 (confirmed range-bound).
- A defined range: at least 3 tests of support and 3 tests of resistance over the lookback period.
- Identified mean (center of the range): VWAP anchored to range start, 20 EMA, or the arithmetic midpoint.
- RSI(14) at an extreme (<=30 or >=70) at the proposed entry.
- ATR(14) for stop calibration.
- Fresh `risk-management` sizing run.

## When to use mean reversion

- ADX < 20 and price is at the range extreme (upper or lower Bollinger Band, range high/low).
- RSI(14) is oversold (<= 30) or overbought (>= 70).
- Volume is showing a climax (spike) at the extreme — suggests exhaustion.
- Multiple oscillators confirm the extreme (RSI + Stochastic + CCI at extremes simultaneously).

## When NOT to use mean reversion

- ADX >= 20 (trending — disabled).
- Price just broke out of the range with volume (potential new trend — disabled).
- A major catalyst is imminent (earnings, FOMC) that could establish a new trend.
- The "range" is actually a descending channel (lower highs, lower lows = trend, not range).
- Less than 3 touches of both support and resistance (insufficient range definition).

## The three core setups

### 1. RSI extreme reversal

Price reaches an RSI extreme at a range boundary with a reversal candle.

**Long setup (buy at range low):**
- RSI(14) <= 30 on the analysis timeframe.
- Price at or below the lower Bollinger Band (20,2).
- Reversal candle: hammer, bullish engulfing, or morning star on the trigger timeframe.
- Volume on the reversal bar >= 1.2x average (buyers stepping in).

**Short setup (sell at range high):**
- RSI(14) >= 70 on the analysis timeframe.
- Price at or above the upper Bollinger Band (20,2).
- Reversal candle: shooting star, bearish engulfing, or evening star on the trigger timeframe.
- Volume on the reversal bar >= 1.2x average (sellers stepping in).

**Entry:** On the close of the reversal candle, or the open of the next bar.

**Stop:** Beyond the range extreme by 1.0 x ATR(analysis TF). This is tight by design — mean reversion uses tight stops because the thesis is immediately invalidated if price continues through the extreme.

**Target:** The mean (VWAP or 20 EMA). Take full profit at the mean — do not hold for the opposite extreme.

### 2. Bollinger Band touch with squeeze release

Price touches the outer band after a Bollinger squeeze (band width at 6-month low).

**Conditions:**
- Bollinger Band Width (BBW) was recently at a 120-day low (squeeze).
- Price touched the outer band (upper or lower) and reversed.
- ADX < 20 confirms range (the squeeze has not produced a trend breakout).
- Keltner Channel is inside the Bollinger Bands (confirms the squeeze).

**Entry:** Fade the band touch. Long on lower band touch, short on upper band touch.

**Stop:** Beyond the band by 0.5 x ATR.

**Target:** The 20 SMA (Bollinger midline). This is typically 1.5-2R.

**Invalidation:** If the band walk begins (3+ consecutive closes outside the band), exit immediately — a trend is starting.

### 3. Volume climax reversal

A volume spike at a range extreme signals exhaustion and imminent reversal.

**Conditions:**
- Volume on the current bar >= 2x the 20-bar average (a true climax).
- Price is at a defined range boundary (support or resistance).
- The climax bar has a long wick rejecting the extreme (buying/selling pressure exhausting).
- RSI(14) at an extreme (confirming alignment).

**Entry:** On the close of the climax bar (aggressive) or the open of the next bar if confirmation candle is bullish/bearish (conservative).

**Stop:** Beyond the climax bar's extreme wick by 0.3 x ATR. Very tight — the climax IS the extreme.

**Target:** The mean (VWAP or 20 EMA). Expect fast moves — volume climax reversals often reach the mean within 2-5 bars.

## Sizing and risk

- Per-trade risk: standard 1% (stops are tight, so share count will be larger).
- Maximum concurrent mean-reversion trades: 2. Range-bound markets produce many signals; discipline is taking only the best.
- Because stops are tight, the R:R often reaches 2:1 or better even with a conservative mean target.

## Tight stops, fast targets

Mean reversion is characterized by:
- **Tight stops:** 0.5-1.0 x ATR beyond the extreme. If price keeps going, the thesis is dead.
- **Fast targets:** the mean (VWAP or MA), not the opposite extreme. Taking half the range is the goal.
- **Quick resolution:** most valid mean-reversion trades resolve within 1-5 bars. If it's not working quickly, something is wrong.

**Time stop:** If price hasn't reached the mean within 7 bars of the analysis TF, exit at market. Range trades that stall often break out.

## Common failure modes

- **Mean reversion in trends (the fatal error).** ADX >= 20 = disabled. No exceptions.
- **Holding for the opposite extreme.** Greed. Take profit at the mean.
- **Widening stops.** If the stop is hit, the range broke. Accept it.
- **Trading every touch.** Not every range boundary touch produces a reversal. Require RSI extreme + reversal candle + volume confirmation.
- **Ignoring the squeeze breakout.** A Bollinger squeeze that resolves with a trend (ADX rising above 20) invalidates all mean-reversion setups. Exit immediately.
- **Averaging down at the extreme.** Price went through your stop — it's trending now. Do not add.

## The ADX re-check protocol

Because mean reversion is disabled in trends, the agent must re-check ADX before every entry:
1. Compute ADX(14) on the analysis TF.
2. If ADX < 20 and falling: ideal conditions (range deepening).
3. If ADX < 20 but rising: acceptable but caution — range may be ending. Reduce size to 50%.
4. If ADX >= 20: STOP. Do not enter. Emit Z. Route to trend-following or swing.

## Outputs contribution

Mean reversion emits a candidate X (at range extremes) or Y (at the mean, or on thesis invalidation) with tight stop, mean target, and time stop. Per-trade risk at standard 1%. Feeds into `risk-management` then `buy-sell-hold-decision`.

## Cross-links

- `technical-indicators` (ADX, RSI, Bollinger Bands, Stochastic)
- `volume-analysis` (climax identification, VWAP as mean)
- `support-resistance-and-fibonacci` (range boundaries)
- `price-action-and-market-structure` (range identification, swing points)
- `risk-management` (tight stops produce larger share counts — verify position value caps)
- `trading-strategies-playbook` (regime gate routes here when ADX < 20)

# Candlestick Pattern Catalogue

This reference lists every candlestick pattern the agent should recognize, with description, bias, reliability, context, and confirmation requirements. Reliability is graded **High / Medium / Low** based on empirical performance in liquid markets when the pattern appears at a meaningful level (S/R, trendline, supply/demand zone) — not in isolation.

A pattern by itself is never a signal. It is a *context modifier*. Always combine with structure, level, and volume.

## Single-candle patterns

### Standard Doji
- **Shape:** open ≈ close, body < 10% of range, wicks on both sides.
- **Bias:** neutral — indecision.
- **Reliability:** Low standalone; Medium at an S/R level.
- **Context:** reversal warning after a strong trend, especially at resistance/support.
- **Confirmation:** next candle must close in the reversal direction beyond the doji's body.

### Dragonfly Doji
- **Shape:** open ≈ close near the high, long lower wick, no upper wick.
- **Bias:** bullish (rejection of lower prices).
- **Reliability:** Medium at support.
- **Context:** bottoming signal after a downtrend.
- **Confirmation:** next candle closes above the dragonfly's high.

### Gravestone Doji
- **Shape:** open ≈ close near the low, long upper wick, no lower wick.
- **Bias:** bearish (rejection of higher prices).
- **Reliability:** Medium at resistance.
- **Context:** topping signal after an uptrend.
- **Confirmation:** next candle closes below the gravestone's low.

### Long-Legged Doji
- **Shape:** tiny body, long wicks on both sides, body near the midpoint.
- **Bias:** strong indecision.
- **Reliability:** Low alone; Medium if volume spikes.
- **Context:** often precedes trend change or consolidation.
- **Confirmation:** directional break of the doji's range.

### Hammer
- **Shape:** small body at the top, lower wick ≥ 2× body, minimal upper wick.
- **Bias:** bullish reversal.
- **Reliability:** High at support after a downtrend; Low in a range.
- **Context:** must appear after a clear downtrend.
- **Confirmation:** next candle closes above the hammer's close; volume on the hammer > 20-bar average.

### Inverted Hammer
- **Shape:** small body at the bottom, upper wick ≥ 2× body, minimal lower wick.
- **Bias:** bullish reversal (weaker than hammer).
- **Reliability:** Medium at support after a downtrend.
- **Context:** post-downtrend, at demand zone.
- **Confirmation:** strong bullish close on the next candle; without follow-through, ignore.

### Shooting Star
- **Shape:** small body at the bottom, upper wick ≥ 2× body, minimal lower wick.
- **Bias:** bearish reversal.
- **Reliability:** High at resistance after an uptrend.
- **Context:** must appear after a clear uptrend into resistance.
- **Confirmation:** next candle closes below the star's low.

### Hanging Man
- **Shape:** identical to hammer but appears at the top of an uptrend.
- **Bias:** bearish reversal warning.
- **Reliability:** Medium — weaker than shooting star.
- **Context:** late-stage uptrend, at resistance.
- **Confirmation:** mandatory — bearish close on the next candle.

### Marubozu (bullish)
- **Shape:** large body, no wicks, close = high, open = low.
- **Bias:** strong continuation (bullish).
- **Reliability:** High in the direction of the prevailing trend.
- **Context:** breakout confirmation, trend continuation.
- **Confirmation:** none needed; the candle itself is the signal.

### Marubozu (bearish)
- **Shape:** large body, close = low, open = high.
- **Bias:** strong continuation (bearish).
- **Reliability:** High with the trend.
- **Context:** breakdown confirmation.
- **Confirmation:** none needed.

### Spinning Top
- **Shape:** small body, roughly equal upper and lower wicks.
- **Bias:** indecision / momentum pause.
- **Reliability:** Low alone.
- **Context:** pullback within trend, or exhaustion at extremes.
- **Confirmation:** directional break.

## Two-candle patterns

### Bullish Engulfing
- **Shape:** small red candle followed by a large green candle whose body fully engulfs the prior body.
- **Bias:** bullish reversal.
- **Reliability:** High at support after a downtrend.
- **Context:** post-downtrend, at demand zone or prior support.
- **Confirmation:** volume on the engulfing candle > prior candle's volume; follow-through next bar.

### Bearish Engulfing
- **Shape:** small green candle followed by a large red candle whose body fully engulfs the prior body.
- **Bias:** bearish reversal.
- **Reliability:** High at resistance after an uptrend.
- **Context:** post-uptrend, at supply zone or prior resistance.
- **Confirmation:** volume confirmation; follow-through next bar.

### Bullish Harami
- **Shape:** large red candle followed by a small green candle whose body fits entirely within the prior body.
- **Bias:** bullish reversal (weaker than engulfing).
- **Reliability:** Medium at support.
- **Context:** downtrend decelerating at a level.
- **Confirmation:** required — bullish close beyond the prior red candle's open.

### Bearish Harami
- **Shape:** mirror of bullish harami.
- **Bias:** bearish reversal.
- **Reliability:** Medium at resistance.
- **Context:** uptrend decelerating at a level.
- **Confirmation:** required.

### Piercing Line
- **Shape:** red candle followed by a green candle that opens below the red's low and closes above the red's midpoint.
- **Bias:** bullish reversal.
- **Reliability:** Medium at support.
- **Context:** downtrend at demand zone.
- **Confirmation:** follow-through with a bullish close.

### Dark Cloud Cover
- **Shape:** green candle followed by a red candle that opens above the green's high and closes below the green's midpoint.
- **Bias:** bearish reversal.
- **Reliability:** Medium at resistance.
- **Context:** uptrend at supply zone.
- **Confirmation:** follow-through with a bearish close.

### Tweezer Top
- **Shape:** two consecutive candles with matching (or near-matching) highs.
- **Bias:** bearish reversal.
- **Reliability:** Medium at resistance.
- **Context:** double-rejection of the same level.
- **Confirmation:** bearish close on the third candle.

### Tweezer Bottom
- **Shape:** two consecutive candles with matching lows.
- **Bias:** bullish reversal.
- **Reliability:** Medium at support.
- **Context:** double-rejection of the same level.
- **Confirmation:** bullish close on the third candle.

### Inside Bar
- **Shape:** a candle whose entire range (including wicks) fits inside the prior candle's range.
- **Bias:** consolidation / continuation.
- **Reliability:** Medium — directional break signal.
- **Context:** trend pause; often precedes a breakout in the prior direction.
- **Confirmation:** directional close beyond the mother bar's high or low.

### Outside Bar
- **Shape:** a candle whose range fully engulfs the prior candle's range.
- **Bias:** direction of close (bullish if green, bearish if red).
- **Reliability:** Medium to High if appearing at a level.
- **Context:** reversal or strong continuation.
- **Confirmation:** volume > 1.5× 20-bar average.

## Three-candle patterns

### Morning Star
- **Shape:** long red candle, then a small-bodied candle (doji or spinning top) that gaps down, then a long green candle closing above the first candle's midpoint.
- **Bias:** bullish reversal.
- **Reliability:** High at support.
- **Context:** mature downtrend.
- **Confirmation:** the third candle's close is the confirmation. Volume ideally increases on the third candle.

### Evening Star
- **Shape:** long green, small-bodied gap-up, long red closing below the first candle's midpoint.
- **Bias:** bearish reversal.
- **Reliability:** High at resistance.
- **Context:** mature uptrend.
- **Confirmation:** third candle close is the signal.

### Three White Soldiers
- **Shape:** three consecutive large green candles, each opening within the prior body and closing near its high.
- **Bias:** strong bullish reversal/continuation.
- **Reliability:** High after a downtrend bottoming or early uptrend.
- **Context:** confirmation of trend reversal.
- **Confirmation:** none needed; the third candle is the signal. Beware exhaustion if it appears extended from an MA.

### Three Black Crows
- **Shape:** mirror of three white soldiers.
- **Bias:** strong bearish reversal/continuation.
- **Reliability:** High after topping.
- **Context:** confirmation of reversal.
- **Confirmation:** none needed; beware oversold bounce.

## Reliability quick table

| Pattern | Reliability | Trend Context | Level Required | Volume Conf. |
|---|---|---|---|---|
| Hammer | High | Post-downtrend | Yes (support) | Yes |
| Shooting Star | High | Post-uptrend | Yes (resistance) | Yes |
| Bullish Engulfing | High | Post-downtrend | Yes | Yes |
| Bearish Engulfing | High | Post-uptrend | Yes | Yes |
| Morning Star | High | Mature downtrend | Yes | Yes |
| Evening Star | High | Mature uptrend | Yes | Yes |
| Three White Soldiers | High | Reversal bottom | No | Preferred |
| Three Black Crows | High | Reversal top | No | Preferred |
| Marubozu | High | Trend continuation | No | Preferred |
| Piercing Line | Medium | Downtrend at support | Yes | Yes |
| Dark Cloud Cover | Medium | Uptrend at resistance | Yes | Yes |
| Harami (bull/bear) | Medium | Decelerating trend | Yes | Yes |
| Tweezer Top/Bottom | Medium | Double rejection | Yes | Yes |
| Dragonfly Doji | Medium | Post-downtrend at support | Yes | Yes |
| Gravestone Doji | Medium | Post-uptrend at resistance | Yes | Yes |
| Inside Bar | Medium | Consolidation | No | Yes |
| Outside Bar | Medium–High | Any | Preferred | Yes |
| Inverted Hammer | Medium | Post-downtrend | Yes | Mandatory |
| Hanging Man | Medium | Post-uptrend | Yes | Mandatory |
| Standard Doji | Low | Any (weak alone) | Yes | Yes |
| Long-Legged Doji | Low | Any | Yes | Yes |
| Spinning Top | Low | Any | Yes | Yes |

## Universal rules

- A pattern outside a level is noise. A pattern at a level is a signal.
- A pattern against the HTF trend is a reversal *candidate*, not a reversal *signal*. Wait for structure confirmation.
- Volume on the pattern bar matters — patterns on below-average volume are weak.
- Reliability is conditional on liquidity. In illiquid names, all reliabilities drop one grade.
- No candlestick pattern, on its own, is sufficient to emit `X` or `Y`. It must be combined with structure (`price-action-and-market-structure`) and risk (`risk-management`).

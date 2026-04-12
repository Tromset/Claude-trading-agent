# Chart Pattern Reliability Table

| Pattern | Direction | Reliability | Typical TF | False-break rate | Vol confirm? | Typical R:R | Best context | Notes |
|---|---|---|---|---|---|---|---|---|
| Head & Shoulders | Bearish reversal | 75% | Daily, 4H | 15% | Yes (declining on right shoulder) | 2:1–3:1 | End of uptrend | Most reliable classic reversal |
| Inverse H&S | Bullish reversal | 76% | Daily, 4H | 14% | Yes (expanding on breakout) | 2:1–3:1 | End of downtrend | Slightly better than bearish H&S |
| Double Top | Bearish reversal | 70% | Daily, 1H | 20% | Yes (lower on 2nd peak) | 2:1 | End of uptrend | Wait for decisive close below support |
| Double Bottom | Bullish reversal | 72% | Daily, 1H | 18% | Yes | 2:1 | End of downtrend | "W" shape — very recognizable |
| Triple Top | Bearish reversal | 78% | Daily | 12% | Yes | 2:1–3:1 | End of extended uptrend | Rarer; 3 tests = strong resistance |
| Triple Bottom | Bullish reversal | 79% | Daily | 11% | Yes | 2:1–3:1 | End of extended downtrend | Rarer but reliable |
| Bull Flag | Bullish continuation | 70% | 1H, 4H, Daily | 20% | Yes (contract then expand) | 2:1–4:1 | Mid-uptrend | Best when pole is impulsive |
| Bear Flag | Bearish continuation | 68% | 1H, 4H, Daily | 22% | Yes | 2:1–3:1 | Mid-downtrend | Declines less orderly |
| Bull Pennant | Bullish continuation | 65% | 1H, 4H | 25% | Yes | 2:1–3:1 | Mid-uptrend | Symmetrical triangle shape — can go either way |
| Ascending Triangle | Bullish | 70% | All | 18% | Yes | 2:1 | Uptrend or range breakout | Flat top + higher lows |
| Descending Triangle | Bearish | 68% | All | 20% | Yes | 2:1 | Downtrend or range breakdown | Flat bottom + lower highs |
| Symmetrical Triangle | Neutral (trend bias) | 55% | All | 30% | Yes | 1.5:1–2:1 | Either; follow HTF trend | Lower reliability; needs extra confirmation |
| Rectangle | Neutral (trend bias) | 60% | Daily, 4H | 25% | Yes | 2:1 | Range consolidation | Breakout direction matches prior trend ~60% |
| Cup & Handle | Bullish | 70% | Daily, Weekly | 15% | Yes (handle low vol) | 2:1–4:1 | Uptrend base | O'Neil CANSLIM classic |
| Rising Wedge | Bearish (counter-intuitive) | 65% | Daily, 4H | 25% | Yes (declining) | 2:1 | End of uptrend or bearish continuation | Converging upward |
| Falling Wedge | Bullish (counter-intuitive) | 68% | Daily, 4H | 22% | Yes | 2:1 | End of downtrend or bullish continuation | Converging downward |
| Rounded Bottom | Bullish reversal | 80% | Daily, Weekly | 10% | Yes (U-shaped) | 3:1+ | End of extended downtrend | Very reliable but slow to form |
| V-Reversal | Either | 60% | All | 30% | Yes (climax) | 2:1–5:1 | Capitulation / euphoria | Hard to trade in real-time |

## How to use this table

1. **Identify the pattern** on the chart using `chart-patterns/SKILL.md`.
2. **Check reliability.** Patterns < 65% reliability require additional confluence (HTF trend alignment, indicator confirmation, S/R level) before emitting `X`.
3. **Check false-break rate.** > 25% false-break rate → wait for close confirmation + retest before entry.
4. **Volume confirmation mandatory** for all patterns marked "Yes" in the Vol column.
5. **R:R must be ≥ 2:1.** If measured target doesn't give 2:1 at the natural stop → skip (`Z`).
6. **Best context matters.** A bull flag in a downtrend is unreliable. Only trade patterns in their natural context.

## Combining patterns with other analysis

- **Pattern + S/R confluence:** breakout at a major S/R level increases reliability by ~10%.
- **Pattern + volume spike:** breakout with volume > 2× average increases reliability by ~5-10%.
- **Pattern + indicator confirmation (non-redundant):** RSI confirming direction adds ~5% to reliability.
- **Pattern + HTF trend alignment:** trading with the higher-timeframe trend adds ~10%.

Never double-count reliability bonuses. Maximum adjusted reliability should be capped at 85% (no pattern is guaranteed).

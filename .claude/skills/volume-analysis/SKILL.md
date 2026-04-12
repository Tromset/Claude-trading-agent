---
name: volume-analysis
description: Use when confirming or denying a price move with volume evidence — breakout validation, divergence detection, VWAP bias, and volume profile analysis.
---

# Volume Analysis

Volume is the fuel behind price movement. Price tells you *what* happened; volume tells you *who showed up*. Moves on high volume are more meaningful; moves on low volume are suspect.

## When to use this skill

- Confirming a breakout (is volume supporting the move?).
- Detecting divergence (price makes new highs but volume declines → weakness).
- Establishing intraday bias using VWAP.
- Identifying high-volume nodes (HVN) and low-volume nodes (LVN) for S/R.
- Assessing whether a selloff is capitulation (climax) or orderly (continuation).

**Anti-triggers:** volume analysis is less useful for low-liquidity instruments (penny stocks, exotic FX pairs) where volume data is unreliable or fragmented.

## Prerequisites

- Volume data available on the chart (most platforms include this by default).
- For VWAP: intraday chart with session volume data.
- For volume profile: platform supports VP histogram (TradingView, TOS, etc.).

## Core concepts

### Raw volume bars

The simplest volume tool. Look at:
- **Relative volume:** current bar volume vs 20-day average volume. Express as a multiple (e.g., 1.8× = 80% above average).
- **Breakout confirmation:** volume on breakout bar should be ≥ 1.5× 20-day average.
- **Declining volume in consolidation:** healthy pre-breakout behavior. Volume should contract as a flag/triangle forms.
- **Volume climax:** extremely high volume (> 3× average) on a reversal bar → possible exhaustion / capitulation.

### Volume-Price Relationships

| Price | Volume | Interpretation |
|---|---|---|
| Rising | Rising | Strong uptrend — buy pressure dominant |
| Rising | Declining | Weak rally — running out of buyers |
| Falling | Rising | Strong downtrend — sell pressure dominant |
| Falling | Declining | Weak decline — sellers exhausted |
| Flat | High | Accumulation or distribution (depends on context) |
| Breakout | High | Genuine breakout — follow it |
| Breakout | Low | False breakout — fade or avoid |

### On-Balance Volume (OBV)

Cumulative volume indicator: adds volume on up days, subtracts on down days.
- **OBV rising while price flat/falling:** accumulation → bullish divergence.
- **OBV falling while price flat/rising:** distribution → bearish divergence.
- OBV divergence often leads price by 3-10 bars.

### VWAP (Volume Weighted Average Price)

The average price weighted by volume, reset each session.
- **Institutional benchmark:** large orders are measured against VWAP. Good fill = at or below VWAP for buys.
- **Intraday bias:** price above VWAP = bullish; below = bearish. Simple and effective.
- **Anchored VWAP:** anchored to a significant event (earnings, IPO, gap) rather than session start. Useful for swing timeframes.

**Trading rules:**
- Day-trade long bias only when price > VWAP.
- Day-trade short bias only when price < VWAP.
- Mean-reversion setups expect price to return to VWAP from extremes.

### Volume Profile

A histogram showing volume traded at each price level (horizontal, not vertical like raw volume).

**Key concepts:**
- **Point of Control (POC):** the price level with the most volume traded — acts as a magnet.
- **High Volume Node (HVN):** price levels with significant volume — act as S/R (price tends to stick here).
- **Low Volume Node (LVN):** price levels with little volume — price moves quickly through these (acceptance vs rejection zones).
- **Value Area (VA):** the range containing 70% of the volume — defines the "fair value" zone.
- **Value Area High (VAH) / Value Area Low (VAL):** upper/lower bounds of the value area — act as S/R.

**Trading with VP:**
- Long entries: at VAL or HVN below current price (support).
- Short entries: at VAH or HVN above current price (resistance).
- Targets: next HVN in the trade direction.
- Stops: beyond the next LVN (quick move zone) past the entry level.

### Accumulation/Distribution (A/D Line)

Like OBV but weighted by where the close falls in the high-low range. Close near the high = accumulation; near the low = distribution.

**Use:** same as OBV — divergence with price is the signal.

### Volume Divergence Rules

**Bullish volume divergence:** price makes lower low, but volume on the lower low is less than volume on the prior low → selling pressure is waning → potential reversal.

**Bearish volume divergence:** price makes higher high, but volume on the higher high is less than volume on the prior high → buying pressure is waning → potential reversal.

**Divergence ≠ trade signal by itself.** It raises a flag that the current trend may be weakening. Combine with reversal candle + S/R level for an actionable setup.

## Decision procedure

1. Measure relative volume: `current_vol / sma(vol, 20)`. If < 0.5× → low volume → any signal is weak.
2. Check volume-price relationship table (above) for the current move.
3. If evaluating a breakout: volume ≥ 1.5× average? If no → likely false break → `Z`.
4. Check OBV / A/D for divergence with price. If divergence → flag it (lowers confidence for continuation, raises it for reversal).
5. If intraday: check VWAP. Price above = bullish bias; below = bearish.
6. If volume profile available: identify POC, VAH, VAL, nearby HVN/LVN.
7. Report findings to the strategy skill as a volume_assessment object.

## Heuristics & thresholds

- **Breakout volume:** ≥ 1.5× 20-day average = confirmed. < 1.5× = suspect.
- **Climax volume:** > 3× average on a reversal bar = possible exhaustion.
- **Volume contraction in consolidation:** declining volume over 5+ bars before breakout = healthy.
- **VWAP deviation:** price > 2 standard deviations from VWAP = extended; mean-reversion likely.
- **VP POC proximity:** price within 0.5% of POC → likely to chop; wait for a move away from POC before entering.

## Common failure modes

- **Ignoring volume on breakouts.** Low-volume breakouts fail most of the time. Always check.
- **Over-reliance on OBV in choppy markets.** OBV accumulates noise in ranges — only useful in trends.
- **Using VWAP on swing timeframes.** Session VWAP resets daily; use anchored VWAP for multi-day.
- **Treating VP as static.** Developing VP changes as new volume is traded. Use completed sessions.
- **Volume data fragmentation.** Different exchanges show different volume. Use consolidated volume when available.

## Outputs expected

```json
{
  "skill": "volume-analysis",
  "relative_volume": 1.8,
  "volume_price_assessment": "rising_price_rising_volume",
  "breakout_confirmed": true,
  "obv_divergence": "none" | "bullish" | "bearish",
  "vwap_bias": "bullish" | "bearish" | "neutral",
  "vwap_price": 181.50,
  "volume_profile": {
    "poc": 180.00,
    "vah": 183.50,
    "val": 177.00
  },
  "confidence_adjustment": "+10 (volume confirms)" | "-15 (volume diverges)"
}
```

## References (lazy-load)

None — this skill is self-contained.

## Cross-links

- Pairs with: `price-action-and-market-structure` (volume confirms structure), `chart-patterns` (breakout volume confirmation), `support-resistance-and-fibonacci` (VP levels as S/R), `technical-indicators/references/volume-indicators.md` (indicator formulas).

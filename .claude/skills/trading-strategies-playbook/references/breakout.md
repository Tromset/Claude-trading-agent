# Breakout Trading — Reference

Pattern and consolidation breakouts confirmed by volume. Breakout trading captures the initial impulse when price escapes a defined range, pattern, or base. Volume confirmation is mandatory — without it, the breakout is suspect.

## Core rule

**Volume >= 1.5x the 20-bar average on the breakout bar is mandatory.** No volume, no trade. A breakout without volume is a false breakout until proven otherwise. This single filter eliminates the majority of failed breakouts.

## Prerequisites

- A clearly defined consolidation or chart pattern with measurable boundaries.
- Volume data (cannot trade breakouts without volume confirmation).
- ADX(14) on the analysis TF in transitional or trending zone (>= 20). Breakouts in deep ranges (ADX < 15) rarely follow through.
- ATR(14) for stop calibration.
- The breakout level identified before the breakout occurs (not after — that is chasing).
- Fresh `risk-management` sizing run.

## When to use breakout trading

- A chart pattern (triangle, flag, rectangle, cup & handle) is completing near its apex or boundary.
- A multi-day/week consolidation is narrowing (contracting volatility precedes expansion).
- ADX is rising from below 20 toward 25+ (regime transitioning from range to trend).
- Bollinger Band Width is at a 6-month low (squeeze about to release).
- The HTF trend supports the breakout direction (weekly uptrend + daily breakout long = aligned).

## When NOT to use breakout trading

- ADX < 15 (deep range — breakouts fail more often than they follow through).
- No volume on the breakout bar (< 1.5x average). Emit Z.
- Entry would be > 1% beyond the breakout level (chasing). Wait for a retest or skip.
- The breakout opposes the HTF trend (daily breakout long against a weekly downtrend = low probability).
- Late in a move (price already 3+ ATR above the last consolidation). The next breakout is more likely to fail.

## Entry rules (strict)

### The 1% rule

Entry must be within 1% of the breakout level. If price has already moved > 1% beyond the breakout when detected, the agent does NOT chase. Options:

1. **Wait for a retest:** Many valid breakouts pull back to test the breakout level (old resistance = new support). Enter on the retest if it holds.
2. **Skip (Z):** If no retest occurs within 3 bars, the move is gone. There will be other setups.

### Volume confirmation gates

| Volume condition | Action |
|---|---|
| Breakout bar volume >= 2.0x average | Strong confirmation — full size entry |
| Breakout bar volume 1.5x - 2.0x average | Adequate — full size entry |
| Breakout bar volume 1.0x - 1.5x average | Weak — Z (do not enter) |
| Breakout bar volume < 1.0x average | Failed breakout likely — Z, watch for reversal |

### Candle quality on the breakout bar

- **Strong:** full-body close beyond the level, minimal upper wick (for longs). Ideal.
- **Acceptable:** close beyond the level, some wick but body > 60% of range.
- **Weak:** long wick beyond the level with close near the level (doji-like). Z — this is a poke, not a breakout.
- **Failed:** wick beyond but close back inside the pattern. Potential reversal signal (see false-breakout handling below).

## Stop placement

**Below the pattern.** The stop goes below the pattern boundary that was broken through:
- **Rectangle breakout:** stop below the consolidation low (for longs).
- **Triangle breakout:** stop below the lower trendline at the breakout bar's x-coordinate.
- **Flag breakout:** stop below the flag low.
- **Cup & handle:** stop below the handle low.
- **Generic:** stop below the last swing low inside the pattern.

**ATR minimum:** If the pattern-based stop is tighter than 1.0 x ATR(analysis TF), widen to 1.0 x ATR. Noise will take out stops that are too tight.

**ATR maximum:** If the pattern-based stop is wider than 3.0 x ATR, the pattern is too large for the current volatility. Either wait for a tighter setup or trade only a partial breakout (enter at the retest with a tighter stop).

## Target (measured move)

The classic breakout target is the **measured move**: the height of the pattern projected from the breakout level.

- **Rectangle:** height of the range added to the breakout level.
- **Triangle:** widest part of the triangle added to the breakout point.
- **Flag:** the flagpole length projected from the flag breakout.
- **Cup & handle:** depth of the cup added to the rim breakout.
- **Head & shoulders (inverse for longs):** head-to-neckline distance projected from the neckline breakout.

**Minimum R:R:** If the measured move target does not produce at least 2:1 R:R (target distance >= 2x stop distance), emit Z. The risk is not justified.

### Partial targets

- T1: 1R (stop distance added to entry). Take 25-50% off here.
- T2: Measured move. Take remaining position.
- Trail: After T1, trail stop to breakeven. After 1.5R, trail using 10 EMA or 1.5x ATR chandelier.

## False-breakout handling (the reverse protocol)

False breakouts are common (30-50% of all breakouts fail). The agent must have a plan:

### Detection

A false breakout is confirmed when **price closes back inside the pattern within 2 bars** of the breakout.

### Response

1. **Exit immediately (Y).** Do not wait for the original stop. The close back inside the pattern IS the invalidation.
2. **Consider the reverse:** A false breakout long that closes back inside the pattern is a potential short signal (trapped longs). If:
   - The false breakout bar had weak volume (< 1.5x — it was suspicious from the start).
   - The re-entry bar has strong volume (sellers/buyers taking control).
   - RSI divergence exists at the breakout level.
   Then: reverse the trade (short entry below the pattern low with stop above the false breakout high). This is the "failed breakout reversal" setup and often produces fast 2-3R moves.
3. **If unsure:** exit and go flat (Z). Do not hold hoping it will re-break.

## Breakout types ranked by reliability

| Type | Reliability | Notes |
|---|---|---|
| Breakout from long base (12+ weeks) | Highest | Large institutions accumulated — strong follow-through |
| Bull flag in strong trend | High | Continuation pattern with trend support |
| Symmetrical triangle at HTF support | Moderate-High | Depends on volume confirmation |
| Rectangle/range breakout | Moderate | Works best with contracting volume in range |
| Ascending triangle | Moderate-High for longs | Multiple tests of resistance + higher lows |
| Descending triangle | Moderate-High for shorts | Multiple tests of support + lower highs |
| Wedge breakout (counter-trend) | Lower | Counter-trend patterns fail more often |

## Common failure modes

- **No volume = no trade.** The single most important filter. Ignoring it leads to trapped positions.
- **Chasing (entry > 1% beyond breakout).** Discipline. Wait for retest or skip.
- **Holding a false breakout hoping for recovery.** Exit on close back inside. Do not hope.
- **Fighting the HTF.** Breakout long on daily, but weekly is in a downtrend = low probability.
- **Ignoring the measured target.** Taking profits at 1R and missing the 3R measured move. Use partials — do not exit everything at 1R.
- **Breaking out on news without reading the volume.** Earnings gaps look like breakouts but often reverse. Require volume + daily close above the level (not just intraday).

## Outputs contribution

Breakout trading emits a candidate X with: breakout level, entry price (within 1% of level), pattern-based stop, measured-move target, volume confirmation status, and false-breakout exit plan. Per-trade risk at standard 1%. Feeds into `risk-management` then `buy-sell-hold-decision`.

## Cross-links

- `chart-patterns` (pattern identification and measurement)
- `volume-analysis` (breakout confirmation, climax detection)
- `price-action-and-market-structure` (structure levels that form pattern boundaries)
- `technical-indicators` (ADX for regime, Bollinger for squeeze)
- `support-resistance-and-fibonacci` (breakout levels, retest zones)
- `risk-management` (stop sizing, R:R validation)
- `trading-strategies-playbook` (routes here in transitional regimes with consolidation)

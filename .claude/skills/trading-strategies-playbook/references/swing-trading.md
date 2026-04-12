# Swing Trading — Reference

2-10 day holds. The default tactical strategy for this agent when timeframe intent is ambiguous. Swing trading captures multi-day directional moves by entering at high-probability pullback or breakout points on the daily chart, triggered on the 4h/1h.

## Core rule

**The weekly trend is the filter; the daily is the setup; the 1h/4h is the trigger.** Never take a swing long when the weekly is in a confirmed downtrend. Never take a swing short when the weekly is in a confirmed uptrend.

## Prerequisites

- Weekly trend direction confirmed (higher highs and higher lows, or price above 20W EMA).
- Daily chart with at least 50 bars of context for structure.
- ADX(14) on daily >= 20 (otherwise route to mean-reversion).
- ATR(14) on daily computed for stop calibration.
- Fresh `risk-management` sizing run.
- No earnings within 2 days (unless the trade thesis explicitly accounts for it).

## The three core setups

### 1. Trend pullback to support (MA / S-R / Fib)

The highest-probability swing setup. Price is in a daily uptrend and pulls back to a confluence zone.

**Confluence zone candidates (need 2+ overlapping):**
- 20 EMA or 50 SMA on daily
- Prior swing high (old resistance now support)
- 38.2% or 50% Fibonacci retracement of the last impulse leg
- Rising trendline (3+ touches)
- VWAP anchored to the impulse start

**Entry trigger (on 1h/4h):**
- Bullish engulfing, hammer, or morning star at the zone
- RSI(14) 1h divergence (lower low price, higher low RSI)
- Volume declining into the pullback, then expanding on the trigger bar

**Stop:** Below the confluence zone by 0.5 x ATR(daily). The structural level is the nearest swing low beneath the zone. Use the wider of these two.

**Target:**
- T1: Prior swing high (the high before the pullback) = approx 1R-1.5R
- T2: Measured move (length of impulse projected from pullback low) = approx 2R-3R
- Default: take half at T1, trail remainder to T2

### 2. Breakout from multi-day consolidation

Price consolidates 5-15 days in a tight range (<3x ATR wide) within a larger uptrend. Breakout above the range high triggers entry.

**Entry trigger:**
- Daily close above the consolidation high (not just a wick)
- Volume on breakout day >= 1.5x 20-day average
- Entry within 1% of the breakout level (no chasing)

**Stop:** Below the consolidation low, or below the midpoint of the range if the range is wide relative to ATR.

**Target:** Measured move = range height projected above the breakout level. Minimum 2R required or skip the trade (Z).

**False breakout handling:** If price closes back inside the range within 2 days, exit immediately (Y). Do not wait for the stop.

### 3. Failed-breakdown long (spring / bear trap)

Price breaks below a well-defined support level, holds for 1-3 bars, then reverses back above the level with strong volume. This traps shorts and produces a powerful long move.

**Conditions:**
- Support level tested 2+ times prior
- Breakdown holds for 1-3 bars maximum (extended breakdowns are real, not traps)
- Reclaim of the support level on volume >= 1.5x average
- RSI(14) was oversold (<30) during the breakdown

**Entry:** On the daily close back above the support level.

**Stop:** Below the false-breakdown low minus 0.5x ATR(daily).

**Target:** T1 at the nearest resistance above (prior swing high), T2 at 2R minimum.

## Holding rules

- **Maximum hold: 10 trading days.** If neither target nor stop is hit in 10 days, exit at market (time stop). Log as TIME_STOP.
- **Partial exits:** Take 50% at T1 (1R profit), move stop to breakeven on the remainder. Trail remainder using the 10 EMA on the daily or a chandelier stop (2x ATR from the highest close).
- **No averaging down.** Adding to a losing swing is forbidden.
- **Add only on strength.** May add 50% of original size if price breaks to new highs beyond T1 with volume confirmation. New add gets its own stop at the prior swing low.

## Overnight risk awareness

Swing trades carry overnight gap risk. Mitigations:
- Per-trade risk capped at 1% accounts for normal gaps (ATR stop already absorbs most).
- Before earnings, FOMC, CPI, or NFP days: either exit or reduce to 50% size the day before.
- If a stock gaps beyond the stop, exit at open. Do not hope for a fill at the stop price.
- Weekend holds: acceptable for stocks in strong trends. Reduce size by 25% for Friday entries.

## Stops: structural + ATR hybrid

The agent uses two stop methods and takes the **wider** one:

1. **Structural:** below the nearest swing low that would invalidate the thesis.
2. **ATR-based:** entry minus 1.5 x ATR(14) daily.

A stop tighter than 1.0 x ATR is too tight for swing trading and will be wicked out by noise. If the structural stop requires more than 2.5 x ATR, the entry is suboptimal — wait for a tighter setup or skip (Z).

## Regime gate

- ADX(14) daily >= 25 and rising: ideal for pullback and breakout setups.
- ADX(14) daily 20-25: acceptable but reduce confidence; prefer only pullback setups.
- ADX(14) daily < 20: swing trading disabled. Route to `references/mean-reversion.md`.

## Common failure modes

- **Converting day trades into swings.** A day trade that went against you is not a swing setup.
- **Entering mid-impulse (chasing).** If price is already 3+ ATR above the last pullback, wait.
- **Ignoring the weekly.** Daily looks good but weekly is at resistance — Z.
- **Holding through earnings.** Unless the position is value-backed and sized for it.
- **No partial exits.** Taking profits at 1R on half the position protects the trade psychologically and financially.
- **Trailing too tight.** The 10 EMA trail should use the daily close, not intrabar wicks.

## Outputs contribution

Swing trading emits a candidate X or Y with daily-bar entry/stop/target, partial exit levels, maximum hold duration, and overnight risk notes. Feeds into `risk-management` at standard 1% per-trade risk, then to `buy-sell-hold-decision`.

## Cross-links

- `price-action-and-market-structure` (trend, structure, swing points)
- `support-resistance-and-fibonacci` (zones, fibs)
- `technical-indicators` (ADX, RSI, EMA)
- `volume-analysis` (breakout confirmation, pullback drying up)
- `risk-management` (sizing, ATR stop)
- `safety-and-kill-switch` (overnight gaps beyond stop)

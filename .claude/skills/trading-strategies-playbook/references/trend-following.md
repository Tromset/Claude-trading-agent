# Trend Following — Reference

Classic trend following adapted for discretionary use. Weeks to months of holding, riding sustained moves with trailing stops. The philosophy: capture the middle 60% of major trends; miss the first 20% (confirmation cost) and the last 20% (exit cost). The edge is in the outlier wins.

## Core rule

**The trend is your only edge. Never predict reversals, never fight the tape, and never exit a winning trend early because "it's gone too far."** Trend following accepts many small losses and occasional large wins. The large wins must be allowed to run — cutting winners is the cardinal sin.

## Prerequisites

- HTF (weekly or monthly) trend confirmed: price above 20W EMA AND ADX(14) weekly >= 25.
- Daily chart showing higher highs and higher lows (longs) or lower highs and lower lows (shorts).
- Volatility measure: ATR(14) on both weekly and daily.
- No mean-reversion regime on the analysis TF (ADX must be >= 25).
- Portfolio-level sector/asset diversification (trend following works best across many uncorrelated instruments).
- Fresh `risk-management` sizing run at standard 1% per trade.

## Philosophy: Turtle/Covel mechanics adapted

Original Turtle rules (Richard Dennis / William Eckhardt):
- Enter on N-day high breakout (typically 20 or 55 days).
- Size by volatility (ATR-based).
- Trail stop at 2x ATR from the highest close.
- Add on strength (pyramid) at each 0.5 ATR of favorable movement.

This agent adapts these rules for **discretionary use with a conservative overlay:**
- Entry: pullback to EMA or structure within a confirmed trend (not raw N-day breakout, which has worse risk:reward for single-name equity trading).
- Sizing: same 1% risk, ATR-based stop.
- Trail: 2x ATR chandelier from highest close, or 10/20 EMA, whichever is tighter after 1R of profit.
- Pyramid: allowed but capped (see adding rules below).

## The two core entry methods

### 1. Pullback to structure/EMA in confirmed trend

The lower-risk entry. Wait for the trend to confirm, then buy the dip.

**Conditions:**
- Weekly ADX >= 25 and trending (DI+ > DI- for longs, DI- > DI+ for shorts).
- Price above 20W EMA and 50W SMA.
- Daily pullback touches 20D EMA or prior breakout level (support).
- Volume contracts during the pullback (not distribution).
- Reversal candle on daily or 4h at the EMA/support level.

**Entry:** On the daily close above the prior bar's high after the pullback touch.

**Stop:** Below the pullback low minus 0.5x ATR(daily). This is structural.

**Target:** None — trend followers do not set targets. They trail stops. The target is "wherever the trend eventually ends."

### 2. Breakout entry with trend confirmation

Higher-risk entry (worse initial R:R) but catches trends earlier.

**Conditions:**
- Price makes a new 20-day high (Turtle-style short-term breakout) or new 55-day high (Turtle-style long-term breakout).
- Weekly trend already confirmed (not a range breakout — the weekly must already be trending).
- Volume on breakout >= 1.5x average.
- ADX(14) daily >= 25.

**Entry:** On the daily close above the 20-day or 55-day high.

**Stop:** 2x ATR(daily) below the entry price. This is wider than pullback entries but accounts for breakout volatility.

**Target:** None — trail.

## Trailing stop mechanics (the profit engine)

Trend following profits come from trailing, not from targets. Rules:

### Phase 1: Initial risk (entry to 1R)

- Stop remains at the original structural/ATR level.
- No trailing. Allow the trade to breathe.
- If stopped out, accept the 1R loss and move on.

### Phase 2: Breakeven trail (1R to 2R)

- Once profit reaches 1R, move stop to breakeven (entry price).
- This converts the trade to a "free trade" — the worst outcome is now flat.
- Still no aggressive trailing.

### Phase 3: Active trail (beyond 2R)

- Trail using the **tighter** of:
  - 2x ATR(daily) below the highest daily close since entry (chandelier stop).
  - The 20 EMA on the daily chart (close below = exit).
- Re-compute the trail daily at session close. Do not trail intraday.
- Never move the trail backward (tighten only).

### Phase 4: Weekly trail (beyond 5R)

- For extended trends (5R+ of unrealized profit), widen the trail to the weekly timeframe:
  - 2x ATR(weekly) below the highest weekly close.
  - Or close below the 10W EMA for 2 consecutive weeks.
- This allows the trend to make larger pullbacks without shaking the position out.

## Adding on strength (pyramiding)

Trend following allows adding to winners. Rules:

- **First add:** After 1R of profit AND a new pullback that holds above the prior swing low. Add 50% of original qty. New stop for the add: below the new pullback low.
- **Second add:** After 2R of cumulative profit AND a second higher-low pullback. Add 25% of original qty.
- **Maximum adds:** 2 (total position = 175% of original). Do not pyramid beyond this for a single instrument.
- **Combined risk:** After pyramiding, the total risk (if all stops hit simultaneously) must not exceed 2% of account. If it would, reduce the add size.
- **Never add to a loser.** Pyramiding is only for positions already at profit.

## Diversification: the portfolio dimension

Trend following works best across many instruments because any single trend can fail, but a portfolio of trend-following positions captures the outliers statistically.

Recommendations:
- Hold 5-10 trend-following positions across uncorrelated sectors/asset classes.
- No more than 2 positions in the same sector.
- Include non-equity trends when available (futures: commodities, bonds, currencies).
- Expect 40-50% of individual trades to lose. The system is profitable because winners are 3-10x the size of losers.

## Win rate and expectancy

Trend following typically produces:
- Win rate: 35-45% (most trades are small losses from failed setups).
- Average win: 3-5R (outliers at 10R+).
- Average loss: 1R.
- Expectancy: positive over 50+ trades.

**The agent must not be disturbed by losing streaks.** 5-8 consecutive losses are normal. The system works over dozens of trades, not individual ones. See `trading-psychology` for discipline protocols during drawdowns.

## Common failure modes

- **Cutting winners.** The cardinal sin. "It's gone up so much" is not a reason to exit. Only the trail determines exit.
- **Predicting reversals.** "It looks toppy" — irrelevant. Price and trail determine exit.
- **Trading too few instruments.** A single trend-following trade is gambling. A portfolio of them is a system.
- **Averaging down.** Forbidden. Trend following adds to winners, never losers.
- **Tight trailing.** Using 1x ATR trail instead of 2x results in getting shaken out of trends that would have produced 5R+. Accept larger pullbacks.
- **Trading range-bound markets.** ADX < 25 = trend following disabled. Accept the whipsaw losses and wait.
- **Giving up after a losing streak.** The next trade could be the 10R winner. The system requires consistent execution across many trades.

## Outputs contribution

Trend following emits a candidate X with: entry level, ATR-based stop, NO fixed target (trail rules instead), add plan, and diversification notes. It also emits Y when the trailing stop is hit — the only valid exit. Per-trade risk at standard 1%. Feeds into `risk-management` then `buy-sell-hold-decision`.

## Cross-links

- `price-action-and-market-structure` (trend identification, HH/HL, swing points)
- `technical-indicators` (ADX, EMA, ATR)
- `volume-analysis` (pullback drying up, breakout confirmation)
- `risk-management` (ATR-based sizing, pyramid risk calculation)
- `trading-psychology` (handling losing streaks, letting winners run)
- `trading-strategies-playbook` (routes here when ADX >= 25 and weekly trend confirmed)
- `position-trading` (overlapping timeframe — position trades are often trend-following in disguise)

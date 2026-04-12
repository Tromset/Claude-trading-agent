# Position Trading — Reference

Weeks to months. The bridge between tactical swing trading and fundamental value investing. Position trading uses weekly chart setups, sector rotation, and large-cap trend following to capture major moves while limiting decision frequency.

## Core rule

**The monthly trend is the context; the weekly is the setup; the daily is the trigger.** Position trades align with the dominant HTF trend and add on strength, never against the trend. If the monthly chart is choppy or directionless, position trading is disabled — use swing or value instead.

## Prerequisites

- Monthly chart confirms a directional trend (price above 10M EMA, or clear HH/HL structure).
- Weekly chart showing a pullback to support or a breakout from a multi-week base.
- ADX(14) on weekly >= 20.
- Sector/industry group in relative strength vs. the broad market (or relative weakness for shorts).
- No major macro event (FOMC, election, fiscal cliff) within 1 week that could gap the position beyond its stop.
- Fresh `risk-management` sizing run at standard 1% per-trade risk.
- Account type supports multi-week holds (no margin call risk at current heat).

## When to use position trading

- A large-cap stock is breaking out of a multi-month base on the weekly.
- A sector rotation signal indicates money flowing into a new sector.
- The weekly chart shows a clear trend with shallow pullbacks (ADX > 25, trending cleanly).
- The agent has high conviction from multiple timeframes aligning (monthly + weekly + daily all bullish).

## When NOT to use position trading

- Volatile, news-driven names with frequent gaps (biotech pre-FDA, meme stocks).
- ADX(14) weekly < 20 (range-bound — route to mean reversion or stand aside).
- Late-cycle moves where the weekly is extended > 3 ATR from the 20 WMA (chase risk).
- Earnings within 5 days unless the position is already at profit and stop is at breakeven.

## The three core setups

### 1. Weekly breakout from multi-month base

A stock consolidates for 6-26 weeks in a defined range, then breaks out on the weekly close with volume.

**Conditions:**
- Base duration: minimum 6 weeks, ideally 12-26 weeks (longer = more powerful).
- Base depth: < 35% from high to low (deeper bases are riskier).
- Volume on breakout week >= 1.5x 10-week average.
- Weekly close above the base high (not just an intraday poke).
- Relative strength vs. S&P 500 improving during the base.

**Entry:** On the daily, enter within 2% of the weekly breakout level on a pullback to the breakout zone (old resistance now support).

**Stop:** Below the top of the base (the breakout level) minus 1x ATR(weekly). If this is too wide (> 10% from entry), use 2x ATR(daily) from entry instead.

**Target:** Measured move = base depth projected above the breakout. Typically 3-5R for valid setups.

### 2. Sector rotation entry

Capital rotates from overweight sectors into underweight sectors on a multi-week cycle. Position trading rides these rotations.

**Conditions:**
- Sector relative strength (vs. SPY) has turned from negative to positive on a 4-week lookback.
- At least 3 names in the sector showing weekly uptrend (above 10W EMA, ADX > 20).
- Broad market not in a distribution phase (200 DMA still rising on SPY).

**Entry:** Buy the strongest name in the rotating sector (highest relative strength rank) at its weekly pullback to support or daily breakout.

**Stop:** Below the weekly swing low that preceded the rotation signal.

**Target:** Hold until the sector RS rolls over (turns negative on a 4-week basis) or the individual stock's weekly trend breaks (close below 10W EMA for 2 consecutive weeks).

### 3. Large-cap trend following (weekly pullback)

Established large-cap in a strong weekly uptrend pulls back to a support zone.

**Conditions:**
- Weekly HH/HL structure intact (no lower low on weekly).
- Price pulls back to 10W or 20W EMA (within 1% of the MA).
- Weekly RSI(14) pulls back to 40-50 zone (not oversold — healthy trend pullback).
- Volume contracts during the pullback (no distribution).

**Entry:** Daily trigger — bullish reversal bar at or near the weekly MA level. Enter on next daily open.

**Stop:** Below the weekly pullback low minus 0.5x ATR(weekly).

**Target:** T1 at the prior weekly swing high. T2 at 2x the impulse leg (measured move). Trail with the 10W EMA after T1.

## Wider stops, same 1% risk

Position trading uses wider stops because weekly-timeframe noise is larger. The position sizing formula absorbs this:

```
Example:
  Account $100,000, risk 1% = $1,000
  Entry: $150.00
  Stop: $140.00 (weekly swing low)
  Stop distance: $10.00
  Qty: floor(1000 / 10) = 100 shares
  Position value: $15,000 (15% of account in a single name — acceptable for a position trade)
```

Compare to a swing trade with $3 stop distance: qty = 333 shares, position value $50,000. Position trades are naturally smaller in share count but may represent larger capital allocation. This is acceptable because the thesis is higher-conviction and higher-timeframe.

**Hard cap:** No single position > 25% of account value regardless of stop math.

## Monthly review cadence

Position trades require less frequent monitoring but disciplined periodic review:

| Frequency | Action |
|---|---|
| Daily | Glance at price vs. stop. No action unless stop is hit. |
| Weekly (weekend) | Review the weekly bar: is the trend intact? Is volume healthy? |
| Monthly (first weekend) | Full review: re-read the thesis, check sector RS, verify stop level, decide add/hold/trim. |
| Quarterly | Deep review: does the fundamental picture still support the position? Re-read 10-Q if applicable. |

**Between reviews:** Do not touch the position. Do not check intraday. Position trading discipline means accepting daily noise without reacting to it.

## Adding to winners

Position trades allow planned adds:
- First add: when price clears T1 (prior swing high) and pulls back to hold above it. Add 50% of original size with a new stop below T1.
- Second add: when price clears a second weekly resistance level. Add 25% of original size. New stop below the second add's support.
- Maximum position: 2x original risk budget across all adds (still within portfolio heat cap).

## Common failure modes

- **Checking daily price action and panicking.** Position trades will drawdown 1-2 ATR(weekly) routinely. This is normal.
- **Converting a failed swing into a "position trade."** A swing that hit its stop is not a position opportunity.
- **Ignoring sector context.** A great stock in a rotating-out sector will underperform.
- **No review cadence.** Holding a position without periodic thesis validation leads to slow bleed.
- **Over-concentration.** Multiple position trades in the same sector = correlated risk. Apply 1.5x heat multiplier.
- **Late-cycle entries.** Buying after a stock is already 50%+ above its base breakout. Wait for a new base.

## Outputs contribution

Position trading emits a candidate X with weekly-bar entry/stop/target, sector context, review schedule, and add plan. Per-trade risk at standard 1%. Maximum hold duration: until the weekly trend breaks or the thesis is invalidated (no fixed time stop, unlike swing). Feeds into `risk-management` then `buy-sell-hold-decision`.

## Cross-links

- `fundamental-analysis-and-value-investing` (overlaps for large-cap quality names)
- `price-action-and-market-structure` (weekly structure, HH/HL)
- `technical-indicators` (ADX weekly, RSI weekly, sector RS)
- `support-resistance-and-fibonacci` (weekly zones)
- `risk-management` (wider stops, same % risk)
- `trading-strategies-playbook` (routes here when weekly setups dominate)

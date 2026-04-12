# Day Trading — Reference

Intraday only. Every position flat by the session close. Subordinate to value strategies at the portfolio level.

## Core rule

**Flat-by-close is absolute.** Overnight holding converts a day trade into a swing trade on a setup that was not validated on higher timeframes. Convert or hold → Z. Close or stop out → Y.

## Prerequisites

- Account ≥ $25,000 if US equities pattern-day-trader rules apply, otherwise no more than 3 day trades per rolling 5 business days (see `regulations-and-tax-awareness`).
- Live level-1 (bid/ask) data, preferably level-2.
- ATR(14) on 5m and on daily.
- Premarket range already computed.
- A fresh `risk-management` sizing run.

## Session structure (US equities, times in ET)

| Phase | Time | Character | Posture |
|---|---|---|---|
| Premarket | 04:00–09:30 | Thin, news-driven, wide spreads | Watch only; note PMH/PML, gap |
| Opening range | 09:30–09:45 | Highest volume of day, volatility expansion | Primary setup window |
| Morning trend | 09:45–11:30 | Directional moves, continuation | Trend trades |
| Lunch lull | 11:30–13:30 | Lowest volume, choppy, fake moves | Flat or very small size |
| Afternoon | 13:30–15:00 | Returning volume, often reversal or continuation | Second setup window |
| Power hour | 15:00–16:00 | Highest afternoon volume, MOC imbalance | Trend extension only |
| Close | 16:00 | All positions flat | Mandatory exit |

Futures and crypto have different session structure — see their references.

## The four core setups

### 1. Opening Range Breakout (ORB)

- Define opening range as the high/low of the first 5 or 15 minutes after RTH open.
- Long trigger: 1m close above OR high with volume ≥ 1.5× 5-bar average.
- Short trigger: 1m close below OR low, same volume rule.
- Stop: opposite side of the opening range, or 1× ATR(5m), whichever is wider.
- Target: 2× stop distance, or prior day high/low if closer.
- Invalidation: price re-enters the opening range within 2 bars → exit.

### 2. VWAP Reclaim

- Price opens below VWAP, trends down, then reclaims VWAP on volume.
- Long trigger: 5m close above VWAP after at least 30 min below, with 5m volume ≥ average.
- Stop: most recent 5m swing low below VWAP.
- Target: prior swing high or 2R, whichever is closer.
- Anti-trigger: VWAP reclaim inside the lunch lull — Z.

### 3. Gap-and-Go

- Stock gaps ≥ 2% on premarket news with premarket volume ≥ 500k shares (for large caps; scale for others).
- Long if gap up with strong premarket trend and no major overnight resistance within 2× ATR(daily).
- Entry: 1m close above PMH after the RTH open (not before — avoid premarket illiquidity).
- Stop: VWAP or the premarket low of the last 30 min, whichever is tighter but still structural.
- Target: next HTF level up, or 2R.
- Fade the gap only via setup #4 below.

### 4. Fade / Reversion at Key Levels

- Only valid when ADX(5m) < 20 — intraday range regime.
- Long at daily S1 pivot or prior-day low with a 1m bullish rejection candle + volume climax.
- Stop: 1× ATR(5m) below the level.
- Target: VWAP or the opposite side of the range.
- Never fade a gap-and-go in the first 30 minutes. Never fade into major news.

## Sizing

- Per-trade risk ≤ 0.5% of account on day trades (half the normal 1% cap) because the sample size is larger and the daily-loss cap is easier to hit.
- Max 4 losing trades per session → stop for the day (kill switch input).
- Max 2 open intraday positions simultaneously unless they are hedges.

## Common failure modes

- **Trading the lunch lull.** Low volume, false signals, whipsaws.
- **Holding past close.** Breaks the whole strategy contract.
- **Averaging down intraday.** Forbidden.
- **Chasing premarket breakouts into the open.** Wait for the RTH open + confirmation.
- **Ignoring the daily chart.** A daily-level resistance overhead invalidates a 5m long.
- **Overtrading.** If no setup qualifies, Z. Doing nothing is a valid outcome.

## Outputs contribution

Day-trading emits a candidate X or Y with 5m-granularity entry/stop/target and an explicit `flat_by` timestamp. `risk-management` halves the usual per-trade risk. Final X / Y / Z flows via `buy-sell-hold-decision`.

## Cross-links

- `price-action-and-market-structure` (1m/5m structure)
- `volume-analysis` (VWAP, relative volume)
- `technical-indicators` (ADX for regime)
- `regulations-and-tax-awareness` (PDT)
- `safety-and-kill-switch` (daily loss)

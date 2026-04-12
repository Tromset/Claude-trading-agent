---
name: price-action-and-market-structure
description: Use when reading a chart with only price and volume, to identify trend direction, swing points, break of structure, change of character, supply/demand zones, and multi-timeframe alignment. Produces a directional bias and invalidation level that feed into the X/Y/Z action.
---

# Price Action & Market Structure

Price action is the ground truth. Every other analysis skill — indicators, patterns, Fib — is derived from price. Before touching a single indicator, the agent must be able to describe what price is *doing* in terms of structure.

## When to use this skill

- Scanning a chart for the first time — always read structure before indicators.
- Defining the higher-timeframe (HTF) bias before a lower-timeframe (LTF) entry.
- Deciding whether the current move is a trend continuation or a reversal.
- Picking a structural stop level for `risk-management`.
- Validating that a chart pattern or indicator signal actually aligns with the dominant trend.

**Anti-triggers:** do NOT use this skill for sizing (that is `risk-management`), for final action output (that is `buy-sell-hold-decision`), or for deep pattern names (that is `chart-patterns`).

## Prerequisites

- A clean chart of the instrument on at least two timeframes (HTF for bias, LTF for entry).
- Visible swing highs and lows over the last 50+ bars on each timeframe.
- Volume pane available (used lightly here, deeply in `volume-analysis`).

## Core concepts

### Candle anatomy

A candle encodes four numbers: open, high, low, close. Body = |open - close|. Upper wick = high - max(open, close). Lower wick = min(open, close) - low. Body-to-range ratio above 70% = conviction; below 30% = indecision. Long lower wick into support = rejection of lower prices (bullish context). Long upper wick into resistance = rejection of higher prices (bearish context).

For the full catalogue of named candles and their reliability, see `references/candlesticks.md`.

### Trend definition (HH/HL/LH/LL)

- **Uptrend:** sequence of higher highs (HH) and higher lows (HL).
- **Downtrend:** sequence of lower highs (LH) and lower lows (LL).
- **Range:** neither pattern holds; price oscillates between a horizontal high and low.

A trend is only "confirmed" after two HH+HL pairs (or two LH+LL pairs). A single HH does not make an uptrend.

### Swing points

A swing high = a bar whose high is greater than the N bars to its left and right (typical N = 2 or 3). A swing low = the mirror. Mark swings with dots on the chart. Structure is the *line connecting consecutive swings of the same type*.

### Break of Structure (BOS)

A BOS is when price closes beyond the most recent swing high (in an uptrend continuation) or swing low (in a downtrend continuation). It confirms the trend is still alive. Key rule: **use the close, not the wick.** A wick through a swing level that closes back inside is a liquidity sweep, not a BOS.

### Change of Character (CHOCH)

A CHOCH is when an uptrend posts its first LH+LL, or a downtrend posts its first HH+HL. It is the *first* sign of a possible reversal. A CHOCH by itself is not a reversal — it is an alert. A reversal is confirmed only when a second BOS in the new direction follows.

See `references/market-structure-bos-choch.md` for worked examples.

### Supply and demand zones

A demand zone = the last down-close candle before an impulsive up move (the origin of the rally). A supply zone = the mirror. Zones are rectangular, not lines. They hold on the first retest, get weaker on each subsequent touch, and break when a candle closes through the far edge.

### Liquidity sweeps (stop hunts)

Price frequently wicks just beyond an obvious swing high or low to trigger resting stop orders, then reverses. Identified by: a wick ≥ 1.2× the average wick of the last 20 bars, piercing a prior swing, and closing back inside. These are often the *entry trigger* for a reversal trade, not a BOS.

### Timeframe alignment

- **HTF** (daily/weekly for swing; 1h/4h for intraday): defines the bias.
- **LTF** (1h/4h for swing; 1m/5m for intraday): times the entry.
- Trade only in the direction of the HTF bias unless the setup is explicitly a counter-trend reversal with a CHOCH + BOS confirmation on the HTF itself.

## Decision procedure

1. Open the HTF chart first. Mark the last 5 swing highs and swing lows.
2. Classify: uptrend / downtrend / range, based on HH/HL or LH/LL.
3. Locate the most recent BOS or CHOCH. Note the timestamp and price.
4. Identify the nearest untested supply (above) and demand (below) zone.
5. Drop to the LTF chart. Repeat structure classification on the LTF.
6. Check alignment: HTF bias = LTF bias?
   - If yes → continuation setup, bias = HTF direction.
   - If no → wait for LTF to align (emit `Z`) or treat as a CHOCH in progress.
7. Pick the structural stop: the swing low (for long) or swing high (for short) that would invalidate the structure if broken.
8. Output the bias, the key levels, and the invalidation level to `risk-management` + the strategy skill.

## Heuristics & thresholds

- **Two confirmations, not one.** Single HH ≠ uptrend. Two HH + two HL ≠ uptrend. Two consecutive HH + HL pairs = uptrend.
- **Close beats wick.** A BOS requires a candle *close* beyond the level. Wicks are noise.
- **First retest is strongest.** Supply/demand zones hold best on the first touch. After the third touch, the zone is "weak" and likely to break.
- **Sweep then reverse.** Price often wicks a swing before the real move. If the wick is long and closes back inside, look for reversal, not continuation.
- **HTF > LTF always.** Never trade against the HTF trend on signals derived from LTF alone.
- **Round numbers matter.** $100, $50, ETH at $3000 — price reacts to these because participants anchor orders to them.
- **Consolidation breakouts.** After 8+ bars in a tight range, the break has directional conviction; fade-the-range setups lose their edge.

## Common failure modes

- **Trading against HTF.** Seeing a bullish LTF setup inside a HTF downtrend and entering long.
- **Confusing CHOCH with reversal.** A CHOCH is a *warning*, not a signal. Wait for the follow-up BOS.
- **Marking fake swings.** Using N=1 for swing identification produces noise. Use N ≥ 2.
- **Ignoring liquidity sweeps.** Entering on a BOS that is actually a sweep that closed back inside — instant loss.
- **Zone instead of line, but still ignoring the edge.** Drawing a zone and then treating the midpoint as the level. Use the *far edge* (protective) or *near edge* (aggressive) deliberately.
- **Forcing structure in a range.** Ranges do not have trend structure. Don't pretend HH/HL exists where it doesn't.
- **One-timeframe analysis.** Never emit an action from a single timeframe.

## Outputs expected

```json
{
  "skill": "price-action-and-market-structure",
  "ticker": "NASDAQ:AAPL",
  "htf": "1D",
  "ltf": "1H",
  "htf_bias": "UP" | "DOWN" | "RANGE",
  "ltf_bias": "UP" | "DOWN" | "RANGE",
  "alignment": true,
  "last_structure_event": {
    "type": "BOS" | "CHOCH",
    "direction": "UP" | "DOWN",
    "price": 182.40,
    "bar_timestamp": "2026-04-10T19:00Z"
  },
  "nearest_demand_zone": [179.50, 180.20],
  "nearest_supply_zone": [186.10, 187.00],
  "invalidation_level": 177.80,
  "direction_suggested": "LONG" | "SHORT" | "NONE",
  "confidence_contribution": 0-20,
  "notes": "HTF uptrend, LTF just posted BOS above prior swing high at 182.40. Demand zone at 179.50-180.20 is untested."
}
```

**Feeding the X/Y/Z decision:**
- `direction_suggested` sets the trade side.
- `invalidation_level` becomes the `stop_loss` input to `risk-management`.
- `confidence_contribution` flows into the `buy-sell-hold-decision` rubric (up to 20 points for "Trend / structure agreement").
- If `htf_bias` and `ltf_bias` disagree → emit `Z` unless the strategy is explicitly a reversal setup.
- If no clear structure (range, no BOS, no CHOCH) → direction_suggested = NONE → upstream emits `Z`.

## References (lazy-load)

- `references/candlesticks.md` — full candlestick pattern catalogue with reliability scores.
- `references/market-structure-bos-choch.md` — worked examples of BOS/CHOCH on real charts.

## Cross-links

- Pairs with: `chart-patterns` (named patterns built on top of structure), `support-resistance-and-fibonacci` (horizontal levels that interact with structure), `volume-analysis` (confirms BOS with volume), `technical-indicators` (used only *after* structure is read), `risk-management` (consumes invalidation level), `buy-sell-hold-decision` (consumes direction + confidence).

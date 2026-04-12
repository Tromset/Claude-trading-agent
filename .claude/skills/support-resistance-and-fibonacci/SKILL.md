---
name: support-resistance-and-fibonacci
description: Use when identifying key price levels (horizontal S/R, pivot points, Fibonacci retracement/extension) to define entry, stop, and target zones for any trade setup.
---

# Support, Resistance & Fibonacci

Price levels where buying or selling pressure concentrates. Every entry, stop, and target should be at or near a defined level — never in empty space.

## When to use this skill

- Defining entry levels for pullback or breakout trades.
- Placing stops at structural invalidation levels.
- Setting targets at the next significant resistance (longs) or support (shorts).
- Confirming confluence between multiple analysis tools.
- Identifying "decision zones" where price must choose a direction.

**Anti-triggers:** do not use this skill in isolation — combine with `price-action-and-market-structure` and/or `chart-patterns` for context.

## Prerequisites

- A chart with at least 100 bars of visible history on the strategy timeframe.
- HTF chart available for major levels.

## Core concepts

### Horizontal Support & Resistance

**Support:** price level where buying pressure historically absorbed selling. Identified by:
- Prior swing lows (price bounced from this level at least 2×).
- High-volume nodes on volume profile.
- Round numbers ($50, $100, $200) — psychological.
- Prior breakout levels that may be retested as support.

**Resistance:** price level where selling pressure historically absorbed buying. Mirror of support:
- Prior swing highs (price rejected at least 2×).
- High-volume nodes above current price.
- Round numbers, prior breakdown levels.

**Strength of a level** increases with:
- Number of touches (2 = minimum, 3+ = strong).
- Timeframe (weekly S/R > daily > hourly).
- Volume transacted at the level.
- Recency (levels from last 6 months > old levels, but major multi-year levels are "forever").

### S/R Flip

When support breaks, it becomes resistance (and vice versa). This is one of the most reliable concepts in technical analysis.

**Trading the flip:**
- Price breaks below support → wait for retest of that level from below → now it's resistance → entry short (or confirm it holds as resistance before shorting).
- Price breaks above resistance → retest from above → now support → entry long.

### Pivot Points

Calculated from prior session's high, low, close. Three systems:

**Classic pivot:**
- P = (H + L + C) / 3
- R1 = 2P − L, S1 = 2P − H
- R2 = P + (H − L), S2 = P − (H − L)

**Camarilla:** tighter levels, better for intraday.
**Woodie:** weighted toward close.

Primarily used for day-trading as intraday S/R.

### Fibonacci Retracement

Based on the Fibonacci sequence ratios. Applied to a swing (low→high for uptrends, high→low for downtrends).

**Key retracement levels:**
| Level | Use |
|---|---|
| 23.6% | Shallow pullback in strong trends |
| 38.2% | Most common pullback in healthy trends |
| 50.0% | Not Fibonacci but widely watched (half-way) |
| 61.8% | "Golden ratio" — deep pullback, last defense before trend break |
| 78.6% | Very deep; trend validity questionable beyond this |

**Decision rule:** In an uptrend, a pullback to 38.2–61.8% with a reversal candle at a level that also has horizontal S/R = high-confluence entry zone.

### Fibonacci Extension

Used for targets beyond the prior swing high/low.

**Key extension levels:**
| Level | Use |
|---|---|
| 100% | Equal move (measured move) |
| 127.2% | Conservative target |
| 161.8% | Standard target |
| 200% | Aggressive target |
| 261.8% | Extended target (strong trends only) |

**Decision rule:** Place the primary target at 127.2% or 161.8% extension. Use partial profit-taking: 1/2 at 127.2%, trail the rest toward 161.8%.

### Confluence

A level where multiple S/R types converge is far stronger than a single one.

**Strong confluence example:** horizontal prior swing low + 61.8% Fib retracement + 200 EMA + round number ($200) all at the same price zone (within 1% of each other).

**Minimum confluence for a trade:** at least 2 independent S/R types should agree at the entry/stop/target level. "Independent" means different methods — two Fib levels from the same swing are NOT independent.

## Decision procedure

1. Identify the most significant S/R levels on the HTF (weekly/daily).
2. Zoom to the strategy timeframe and mark levels visible there.
3. Draw Fibonacci retracement from the most recent significant swing.
4. Look for confluence: where do horizontal S/R, Fib levels, MAs, and pivot points cluster?
5. Mark the 2–3 strongest zones (price ranges, not exact lines — S/R is a zone ±0.5%).
6. Feed the identified levels to the strategy skill for entry/stop/target placement:
   - Entry: at or near a strong support zone (for longs) or resistance zone (for shorts).
   - Stop: beyond the next S/R level outside the trade direction (invalidation).
   - Target: at the next strong S/R level in the trade direction.
7. If no clear levels exist (price in open space) → emit `Z` (no trade without a defined level).

## Heuristics & thresholds

- S/R is a **zone** (±0.3–0.5% of the level), not an exact price.
- A level tested 3+ times without breaking is strong; tested 5+ times it may be exhausted and ready to break.
- HTF levels trump LTF levels in a conflict.
- Fib levels only work when the swing is clean and significant (at least 20 bars and 5% move).
- When price is between levels with no nearby S/R → no trade setup. Wait.
- Confluence score: 1 type = weak (Z), 2 types = moderate, 3+ types = strong (X candidate).

## Common failure modes

- **Drawing Fib from insignificant swings.** Use major swing points visible on the HTF, not micro-wiggles.
- **Treating lines as exact.** S/R is a zone; expecting a bounce at $100.00 exactly is naive.
- **Ignoring broken levels.** Once support breaks, it's resistance. Don't keep hoping it's still support.
- **Too many levels on the chart.** If every $1 has a "level," none of them matter. Mark only the 3–5 most significant.
- **Fib worship.** Fib levels are guidelines, not physics. They work because many traders watch them — self-fulfilling to a degree, but they fail regularly.

## Outputs expected

```json
{
  "skill": "support-resistance-and-fibonacci",
  "levels": [
    {"price": 177.50, "type": "horizontal_support", "strength": "strong", "touches": 3, "timeframe": "daily"},
    {"price": 179.00, "type": "fib_618", "swing": "170→185", "confluence": ["ema_50"]},
    {"price": 192.00, "type": "horizontal_resistance", "strength": "moderate", "touches": 2}
  ],
  "confluence_zones": [
    {"range": [177.00, 178.00], "types": ["horizontal_support", "fib_618", "ema_50"], "score": 3}
  ],
  "suggested_entry_zone": [177.50, 178.50],
  "suggested_stop_zone": [175.00, 175.50],
  "suggested_target_zone": [191.50, 192.50]
}
```

## References (lazy-load)

None — this skill is self-contained.

## Cross-links

- Pairs with: `price-action-and-market-structure` (swing points define Fib anchors), `chart-patterns` (pattern targets often align with Fib extensions), `risk-management` (levels define stop/target → R:R), `volume-analysis` (HVN/LVN confluence with S/R).

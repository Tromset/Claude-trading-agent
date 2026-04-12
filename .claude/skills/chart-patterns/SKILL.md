---
name: chart-patterns
description: Use when the agent has already read raw market structure and needs to classify the current price formation into a named chart pattern (H&S, triangles, flags, wedges, double tops, cup & handle, etc.) to derive an entry trigger, measured target, and invalidation level.
---

# Chart Patterns

Chart patterns are structural *shapes* that tend to resolve in a statistically reliable direction. They are derived from price action (`price-action-and-market-structure`) and refined by volume (`volume-analysis`). A pattern alone is never sufficient for an action — it is the *geometry* around which an entry, stop, and target are built.

## When to use this skill

- Price structure has been read (HH/HL/LH/LL classification is done) and the agent can see a recognizable formation.
- The agent needs a measured target (not just a direction) for the R:R calculation in `risk-management`.
- A breakout or breakdown is suspected and the agent needs criteria for "is this a real breakout?"
- Evaluating whether a formation is a reversal or continuation pattern in context.

**Anti-triggers:** do NOT use this skill to identify trend itself (that is `price-action-and-market-structure`), to size the trade (that is `risk-management`), or as a substitute for structure (a pattern drawn in a choppy range is not a pattern).

## Prerequisites

- HTF trend bias already established.
- Visible swing highs and lows marked.
- Volume pane visible for breakout confirmation.
- Minimum chart history: the pattern plus at least 2× its duration before the pattern, for context.

## Core concepts

### Pattern taxonomy

Patterns split cleanly into two families:

- **Reversal patterns:** signal the end of the prevailing trend. Covered in `references/reversal-patterns.md`. Examples: head & shoulders, inverse H&S, double/triple tops, double/triple bottoms, rounded bottom, V-reversal.
- **Continuation patterns:** signal a pause inside an existing trend before resumption. Covered in `references/continuation-patterns.md`. Examples: bull/bear flags, pennants, symmetrical/ascending/descending triangles, rectangles, cup & handle.

Some patterns (wedges, symmetrical triangles) can resolve in either direction and require breakout confirmation before classification.

### Pattern validity checklist

A pattern is only tradeable if all of the following hold:
1. **Context:** the pattern appears after a clear prior trend (for continuation) or at an exhaustion extreme (for reversal).
2. **Touches:** the pattern boundaries are defined by at least two touches per side (three is stronger).
3. **Duration:** the pattern spans enough bars that it isn't a coincidence — typically ≥ 15 bars for intraday patterns, ≥ 8 weeks for weekly patterns.
4. **Clean shape:** the boundaries form a coherent geometry without excessive noise.
5. **Volume profile:** volume behaves in the characteristic way for the pattern (declining inside a triangle, spiking on breakout, etc.).
6. **Not yet broken:** the breakout is imminent or just happened; old patterns have no edge.

If any check fails → do not trade the pattern → emit `Z`.

### Breakout rules (universal)

A breakout is valid only when:
- A candle *closes* beyond the pattern boundary (not a wick).
- Volume on the breakout candle ≥ 1.5× the 20-bar average.
- The close is ideally > 1% beyond the boundary (for equities) or ≥ 0.3× ATR beyond (for any instrument).
- The first retest of the broken boundary holds (post-breakout).

False breakouts (pattern breaks, then closes back inside within 1–3 bars) are common and signal a likely move in the opposite direction. See "failure modes" below.

### Measured target

Every pattern has a **measured target** — a projection derived from the pattern's own geometry.

- **H&S:** target = neckline − (head height) measured from the breakdown point.
- **Double top:** target = breakdown level − (top height above neckline).
- **Flag:** target = breakout level + (length of the flagpole preceding the flag).
- **Triangle:** target = breakout level + (height of the triangle's widest part).
- **Cup & handle:** target = breakout level + (depth of the cup).

The measured target is a *first* target, not an absolute. Real trades scale out at measured target and trail the remainder.

See `references/reversal-patterns.md` and `references/continuation-patterns.md` for exact formulas.

## Decision procedure

1. Confirm HTF bias from `price-action-and-market-structure`.
2. Scan the recent 30–60 bars for a geometric shape matching a known pattern.
3. Run the validity checklist. If any criterion fails → `Z`.
4. Classify as reversal or continuation. Cross-check: does the classification align with HTF bias?
   - Continuation pattern in direction of HTF bias → preferred.
   - Reversal pattern against HTF bias → treat as low-confidence unless HTF has already CHOCH'd.
5. Mark the breakout level, stop level, and measured target.
6. Compute R:R = (target − entry) / (entry − stop). If R:R < 2 → `Z` or revise to a 2R target.
7. Wait for breakout confirmation (close + volume). No anticipation entries.
8. On breakout, optionally wait for a retest that holds (higher-quality but sometimes never retests).
9. Pass the entry, stop, and target to `risk-management`.
10. Output pattern identification, R:R, and confidence contribution to `buy-sell-hold-decision`.

## Heuristics & thresholds

- **Pattern + level > pattern alone.** A double top right at a HTF resistance is much stronger than one in mid-air.
- **Volume is the tell.** Volume should decline during a triangle/flag and expand on the breakout. If volume expands *before* the breakout, the pattern is often front-run and the breakout fails.
- **Measured target is a floor, not a ceiling.** Real trends go further; scale out at MT and trail the rest.
- **Symmetrical triangles are direction-agnostic.** Never guess the direction — wait for the break.
- **Long bases = big moves.** The longer the consolidation, the bigger the post-breakout move.
- **First breakout, not retest, is the cleanest entry.** Retests are higher quality but you can miss the trade entirely.
- **Wedges against the trend are reversal signals;** wedges with the trend are often continuation failures.
- **Pattern maturity matters.** A pattern should resolve within 2× its formation time. Patterns that drag on lose their edge.

## Common failure modes

- **Pareidolia.** Seeing patterns where none exist. If you have to squint, it isn't a pattern.
- **Trading before breakout.** Anticipation entries. Wait for confirmation.
- **Ignoring volume.** A breakout on low volume is likely a fake-out.
- **Wrong reference trend.** Continuation patterns require a prior trend. No trend = no flag.
- **Unreasonable targets.** Measured target that places the stop inside a prior zone invalidates the trade.
- **Missing the retest.** Sometimes the retest never comes — if you demand one, you miss the move. Have a rule in advance.
- **Holding through fake-outs.** A break that closes back inside the pattern within 3 bars is a failed break → exit immediately.
- **Stacking pattern names.** A shape is either a flag OR a pennant, not both. Pick the cleaner fit.

## Outputs expected

```json
{
  "skill": "chart-patterns",
  "ticker": "NASDAQ:AAPL",
  "timeframe": "1D",
  "pattern_name": "bull_flag" | "head_and_shoulders" | "ascending_triangle" | "...",
  "pattern_class": "continuation" | "reversal",
  "htf_alignment": true,
  "breakout_level": 186.40,
  "breakout_confirmed": true,
  "breakout_volume_ratio": 1.72,
  "stop_level": 182.10,
  "measured_target": 196.80,
  "risk_reward_ratio": 2.42,
  "pattern_reliability": "High" | "Medium" | "Low",
  "direction_suggested": "LONG" | "SHORT" | "NONE",
  "confidence_contribution": 0-20,
  "notes": "Bull flag on 1D, flagpole = $8.20, flag duration 11 bars, breakout close 186.50 on 1.72x volume."
}
```

**Feeding the X/Y/Z decision:**
- `direction_suggested` sets the side for `risk-management`.
- `breakout_level` becomes the entry (or a limit just above it).
- `stop_level` becomes the stop input (cross-checked with structural stop).
- `measured_target` becomes the target input.
- `confidence_contribution` feeds the "Entry trigger clarity" dimension (up to 20 points) in `buy-sell-hold-decision`.
- If pattern is reversal against HTF and HTF has not CHOCH'd → downgrade confidence, likely `Z`.

## References (lazy-load)

- `references/reversal-patterns.md` — H&S, inverse H&S, double/triple tops & bottoms, rounded bottoms, V-reversals.
- `references/continuation-patterns.md` — flags, pennants, triangles, rectangles, cup & handle.
- `references/pattern-reliability-table.md` — empirical reliability, R:R, timeframes.

## Cross-links

- Pairs with: `price-action-and-market-structure` (supplies HTF bias and swings), `volume-analysis` (confirms breakouts), `support-resistance-and-fibonacci` (pattern edges often coincide with levels), `risk-management` (consumes stop and target), `buy-sell-hold-decision` (consumes direction and confidence).

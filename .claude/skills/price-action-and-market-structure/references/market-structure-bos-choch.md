# Market Structure: BOS and CHOCH Deep Dive

This reference expands on Break of Structure (BOS) and Change of Character (CHOCH) with explicit rules, edge cases, and worked examples.

## Definitions (precise)

### Swing high
A bar whose high is strictly greater than the highs of the N bars on each side, where N ∈ {2, 3}. N=2 is the default for intraday (1m–1h); N=3 for swing (4h–1D).

### Swing low
Mirror of swing high.

### Break of Structure (BOS)
- **Bullish BOS:** in an uptrend, a candle *closes* above the most recent (unbroken) swing high. Confirms continuation.
- **Bearish BOS:** in a downtrend, a candle *closes* below the most recent swing low. Confirms continuation.
- The relevant swing high/low is the most recent one that has *not yet been broken* — not any older swing.

### Change of Character (CHOCH)
- **Bullish CHOCH:** in an existing downtrend, price closes above the most recent swing high — the first one in the downtrend. This is the first evidence that the downtrend may be over.
- **Bearish CHOCH:** in an existing uptrend, price closes below the most recent swing low.
- A CHOCH does NOT confirm a reversal. It only opens the possibility. Reversal is confirmed when a *new* swing forms in the opposite direction AND a BOS follows in that new direction.

## Close vs. wick — the decisive rule

A BOS or CHOCH requires the candle *body to close* beyond the level. A wick that pierces and closes back inside is NOT a structure break — it is a **liquidity sweep**.

Formal:
- Bullish BOS: `candle.close > swing_high.price` (not `candle.high > swing_high.price`).
- Bearish BOS: `candle.close < swing_low.price`.

On intraday timeframes, also require that the next candle does not immediately reverse (i.e., don't chase a BOS on the breaking candle's open — wait one bar).

## Worked example 1: Clean bullish continuation

```
Uptrend has been running.
Bars: ... SL1 (low=100) ... SH1 (high=110) ... SL2 (low=104) ... SH2 (high=115) ... SL3 (low=108) ...

New candle: close = 116.

Is this a BOS?
- Most recent unbroken swing high = SH2 at 115.
- Candle close 116 > 115 → YES, bullish BOS.
- Structure: SL1 (100), SL2 (104), SL3 (108) → higher lows.
- Structure: SH1 (110), SH2 (115), new high → higher highs.
- Uptrend confirmed and continuing.

Action implication: direction = LONG. Stop at SL3 (108) or at the zone below SL3.
```

## Worked example 2: Liquidity sweep misread as BOS

```
Downtrend running. Swing low SL_last = 200.
Bar N: low = 198.50, close = 200.80 (wicked through SL, closed back above).

Is this a BOS?
- Candle low pierced 200 (to 198.50).
- Candle close 200.80 > 200 → NOT a bearish BOS.
- This is a liquidity sweep — stops resting below 200 were triggered, but the candle closed back inside.

Action implication: this is NOT bearish. It is often the *start* of a bullish reversal. If followed by a bullish CHOCH (close above recent swing high), the reversal case strengthens.
```

## Worked example 3: CHOCH leading to reversal

```
Downtrend: ... SH_a (210) ... SL_a (205) ... SH_b (208) ... SL_b (200) ... SH_c (204) ... SL_c (195) ...

New candle closes at 206.
- Most recent swing high in downtrend = SH_c at 204.
- Close 206 > 204 → bullish CHOCH.
- This is the first LH+LL break — warning, not confirmation.

Next: wait for a pullback that forms a new swing low (e.g., SL_new at 201) without breaking below SL_c (195).

If the pullback holds and the next candle breaks above 206 → bullish BOS in the new direction.
Now we have CHOCH + BOS → reversal confirmed.

Only now is it safe to trade long with HTF bias shift.
```

## Worked example 4: CHOCH that fails (trap)

```
Same downtrend, CHOCH prints at 206 as above.
But the pullback breaks below SL_c (195) without forming a new HH.
That means: CHOCH failed, downtrend resumed.

Action implication: do not trade the CHOCH as a reversal signal unless BOS follows. This is why CHOCH alone ≠ X.
```

## Multi-timeframe alignment

A reliable setup aligns structure across at least two timeframes.

| HTF structure | LTF structure | Interpretation | Action class |
|---|---|---|---|
| Uptrend + recent BOS up | Uptrend + BOS up | Full alignment, high confidence | X candidate |
| Uptrend | LTF CHOCH down | HTF pullback beginning | Wait / Z |
| Uptrend | LTF BOS down | HTF pullback confirmed | Wait for LTF CHOCH up, then entry |
| Downtrend | LTF CHOCH up + BOS up | Possible HTF reversal starting | Z until HTF CHOCH too |
| Range | Range | No trade on trend logic | Mean-reversion only |

**Rule:** never enter with the LTF structure against the HTF structure unless the strategy is explicitly a counter-trend reversal *and* HTF has itself printed a CHOCH.

## Edge cases

### Equal highs / equal lows
Two swings at the same exact price are treated as a single level, not two. The break level is that price, and the sweep risk is high (equal highs are classic liquidity targets).

### Gap opens
If the session gap causes a candle to *open* beyond a swing level, wait for the first 15 minutes of price action. A gap that fills within 30 minutes is not a BOS; a gap that holds through the first hour is.

### Inside bars
Inside bars do not create new swings. A swing forms only when a bar's high (or low) actually exceeds the neighbors'. Skip inside bars when marking swings.

### Very large single candles
If a single candle sweeps through multiple prior swings at once, only the *most recent* swing counts as the structural break. Do not claim multiple BOS events from one candle.

## Scoring BOS/CHOCH for the confidence rubric

The `price-action-and-market-structure` skill contributes up to **20 points** to the confidence rubric under "Trend / structure agreement." Score as:

| Condition | Points |
|---|---|
| HTF BOS in trade direction + LTF BOS in trade direction | 20 |
| HTF bias in trade direction + LTF BOS in trade direction | 15 |
| HTF bias in trade direction + LTF CHOCH (no BOS yet) | 10 |
| HTF bias neutral (range) + LTF BOS | 5 |
| HTF bias against trade direction | 0 (downgrade toward Z) |

Below 10 points → generally emit `Z` unless another high-conviction skill (e.g., fundamentals) dominates.

## Minimum requirements to pass structure to the decision

Before handing off to `buy-sell-hold-decision`, the structure output must include:
1. HTF bias (UP/DOWN/RANGE).
2. LTF bias (UP/DOWN/RANGE).
3. Alignment flag.
4. Most recent BOS or CHOCH with price and bar timestamp.
5. Invalidation level (the swing that must hold).

Missing any → emit `Z` upstream.

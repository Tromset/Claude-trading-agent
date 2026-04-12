# X / Y / Z Action Vocabulary — Formal Definitions

## Formal definitions

### X — BUY
Any action that *increases* long exposure or *decreases* short exposure.

Sub-cases:
- `X-OPEN-LONG` — new long position
- `X-ADD-LONG` — add to an existing long (scale-in)
- `X-COVER-SHORT` — close an existing short
- `X-COVER-SHORT-PARTIAL` — reduce an existing short

All sub-cases emit action = `X` in the JSON schema; the `sub_action` field in the payload distinguishes them.

### Y — SELL
Any action that *decreases* long exposure or *increases* short exposure.

Sub-cases:
- `Y-CLOSE-LONG` — exit an existing long
- `Y-REDUCE-LONG` — partial exit / scale-out
- `Y-OPEN-SHORT` — new short position (only for strategies that permit shorting)
- `Y-ADD-SHORT` — add to an existing short

All sub-cases emit action = `Y`; `sub_action` distinguishes.

### Z — HOLD / DO NOTHING
Any state in which no order is placed and no existing order is modified.

Sub-cases:
- `Z-WAIT` — flat, waiting for a clearer setup
- `Z-HOLD` — holding an existing position with no action
- `Z-CANCEL` — cancelling a pending order that no longer makes sense (technically an order action, but from the agent's perspective it's "undo my prior intent" and is emitted as `Z` with a `sub_action: Z-CANCEL`)
- `Z-OVERRIDE` — would have been X/Y but a gate blocked it (the only Z variant that MUST be journaled)
- `Z-WATCH` — same setup has yielded Z three times; add to watch list and stop re-evaluating for N bars

## Edge cases

### Short selling

Short selling is treated as a first-class citizen. `Y-OPEN-SHORT` is a sell (bearish direction) and `X-COVER-SHORT` is a buy (closes the bearish position). The direction of the action matches the trade direction, not the final position sign.

**Only strategies that explicitly permit shorting** may emit `Y-OPEN-SHORT`. Value investing does not short. Day trading, swing momentum, and systematic strategies may.

### Partial fills

If an order is partially filled and then cancelled, the remaining qty is a separate "residual" event logged but not re-emitted as X/Y/Z. The residual is handled by `trade-journaling-and-backtesting`.

### Scale-ins and scale-outs

Strategy skills may specify a scale-in ladder (e.g., 1/3 at entry, 1/3 on confirmation, 1/3 on re-test). Each leg is a separate X decision, gated independently by the pre-trade checklist. Do NOT fire all three as one X — they are sequential decisions.

### Stop and target as "passive Y"

When the agent places an `X` it also typically places a resting stop-loss (another Y) and a resting target (another Y). These are **preplaced passive Y's**, tied to the X entry, logged as a bundle. They are not re-decided on each bar — the bar-by-bar decision is `Z-HOLD` until one of the resting Y's is triggered by the market.

If a resting stop/target fires, the agent journals a Y for `STOP_OUT` / `TARGET_HIT`, even though no new order was placed — the exit was automatic.

### Rolling / adjusting options

Rolling an option (closing one leg and opening another) is two actions: `Y` (close the old) + `X` (open the new). They are paired via a `roll_id` in the journal but are two distinct X/Y emissions.

### Adjusting a stop

Tightening a stop in profit (trailing) is NOT an X/Y — it's a position-management action logged as `Z-TRAIL-TIGHTENED`. The agent is not changing side; it's updating a protective level. This is still a `Z` from the X/Y/Z vocabulary, but with a specific sub_action to make the journal audit clean.

## Disallowed "actions" that must never appear

- **W** — there is no fourth action. Anything not X or Y is Z.
- **"wait and see"** — that is `Z-WAIT`. Use the formal label.
- **"maybe"** — confidence < 60 always downgrades to Z.
- **"average down"** — averaging down on a losing position is an X-ADD-LONG, which is allowed, but only if the *original thesis* still holds and sizing still fits the risk cap. Strategies that explicitly forbid averaging down (most short-term strategies) must reject this X.

## The vocabulary is total

Every clock tick, every screenshot, every decision point the agent faces → resolves to exactly one of `X`, `Y`, or `Z`. There is no fourth state. Indecision = `Z`.

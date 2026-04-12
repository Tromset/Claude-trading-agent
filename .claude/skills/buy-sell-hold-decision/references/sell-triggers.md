# Sell Triggers — When Y is Justified

`Y` has a lower bar than `X`: exit discipline is more valuable than entry discipline. When in doubt about an exit, lean toward `Y` (taking the exit) rather than holding.

## Canonical Y reasons (one must apply)

| Reason | Description | Order type |
|---|---|---|
| `STOP_OUT` | Price has hit the predefined stop-loss level | `MARKET` (usually automatic via resting stop order) |
| `TARGET_HIT` | Price has reached the predefined target | `LIMIT` (usually automatic via resting target order) |
| `THESIS_BREAK` | The original reason for the trade is no longer valid | `MARKET` or `LIMIT` depending on urgency |
| `TIME_STOP` | Position has exceeded its maximum planned holding period | `LIMIT` preferred, `MARKET` if urgent |
| `RISK_REDUCTION` | Portfolio heat forces reducing position due to other trades | `LIMIT` or `MARKET` |
| `TRAIL_TIGHTENED` | Trailing stop has been tightened and is now being hit | usually automatic |
| `KILL_SWITCH` | `safety-and-kill-switch` has triggered a forced flatten | `MARKET` always |

**Non-canonical Y is forbidden.** Exits driven by boredom, tilt, FOMO on *other* setups, or social-media sentiment are not in this list and must not emit Y.

## Mandatory conditions (ALL must be true)

1. **One of the canonical reasons applies.**
2. **A valid open position exists** in the agent's state AND on the screen (state consistency check).
3. **The exit qty is specified** — full or partial.
4. **An order type has been chosen.**
5. **No invariant is blocked** (e.g., don't sell during a trading halt).
6. **Pre-trade checklist (exit-mode) is runnable.**

## STOP_OUT — the sacred rule

Stops are **binary**. Hit = exit, no discussion, no "let me give it one more bar."

- If the stop has been hit, emit `Y` with `reason: STOP_OUT` immediately.
- If a resting stop order was already in place, the exit is automatic — the agent journals the Y but does not need to "decide" anything.
- **Never widen a stop.** Widening is not trade management — it's adding risk. Forbidden by risk-management.
- **Tightening a stop (in profit)** is allowed and logged as `Z-TRAIL-TIGHTENED`, not Y.

## TARGET_HIT

- If the full target was taken, emit Y for the full qty.
- If a partial-target ladder was planned (e.g., 1/2 at 1R, 1/2 at 2R), emit Y for each leg as it triggers.
- After partial target hit, remaining qty may have its stop moved to breakeven — that's a `Z-TRAIL-TIGHTENED`, not a Y.

## THESIS_BREAK

The original *reason* the trade was entered no longer applies. Examples:
- Value trade: the company reports earnings that invalidate the intrinsic-value calculation (e.g., moat erosion, FCF collapse).
- Breakout trade: price closes back below the breakout level on volume (failed breakout).
- Trend trade: HTF structure flips (HH/HL → LH/LL).
- Mean-reversion trade: range breaks out of its prior boundaries.
- Macro trade: the macro catalyst resolves contrary to expectation.

Thesis-break exits are discretionary but **must** cite what specifically invalidated the thesis. "Just doesn't feel right" is not a thesis break.

## TIME_STOP

Every trade has a planned maximum holding period documented at entry:
- Day trade: same session close.
- Swing trade: default 10 sessions, override allowed per setup.
- Position trade: default 90 sessions, override per setup.
- Value investment: no time stop (but thesis review every 90 days).

When the time stop is reached and the trade is neither near its target nor near its stop, exit. The assumption is: if it hasn't worked by now, the setup was wrong.

## RISK_REDUCTION

Triggered by `risk-management` when:
- Portfolio heat has crept above 6% due to volatility expansion in other positions.
- A newer, higher-conviction opportunity requires making room.
- Correlated positions have all moved against the agent simultaneously.

Reduction exits are partial by design — enough to bring heat back within cap.

## TRAIL_TIGHTENED

Not a separate Y reason — this is `Z-TRAIL-TIGHTENED`. The agent tightens the stop to lock in profit without fully exiting. The tightened stop may later trigger a `STOP_OUT` Y.

Canonical trail rules:
- Move stop to breakeven once price has moved 1R in favor.
- Move stop to 1R locked-in once price has moved 2R in favor.
- Trail by 1× ATR(14) below each new higher low (for longs).

## KILL_SWITCH

Forced flatten. The agent's discretion is removed. All positions close at market. Triggered by:
- Daily loss cap hit
- Anomaly detected (platform disconnect, 3× consecutive stop-outs, unexpected ticker behavior)
- Human operator manual kill

See `safety-and-kill-switch/SKILL.md` for the full list.

## Y is the easier action

An unwritten rule: the bar to emit `Y` is *lower* than the bar to emit `X`. If an exit condition is 75% met, take the exit. If an entry condition is 75% met, wait. Losses compound faster than gains recover.

## Anti-triggers (never emit Y)

- Fear on an untouched stop. The stop is the stop.
- Boredom. "Nothing is happening." → `Z`.
- FOMO on another setup — do not rob Peter to pay Paul without a real `RISK_REDUCTION` need.
- Social media sentiment change that does not match the agent's own thesis check.
- Breaking even "just to breathe" after a paper-profit scare. Trail the stop, don't panic-exit.

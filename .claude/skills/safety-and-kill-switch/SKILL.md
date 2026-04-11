---
name: safety-and-kill-switch
description: Use when anomalies, caps, or unexpected screen states demand that the agent stop trading and flatten. Defines all kill conditions, the abort protocol, and how to resume safely.
---

# Safety & Kill Switch

The safety layer. Every skill defers to this one. When any kill condition triggers, the agent stops trading, flattens if necessary, and emits `Z` until a human intervenes or the reset criteria are met.

## When to use this skill

- On every clock tick as a passive monitor.
- When a strategy skill proposes an X or Y — this skill runs *after* the proposal and can veto.
- When `screenshot-vision-protocol` detects an unexpected screen state.
- When `risk-management` detects a cap breach.
- When the human operator manually triggers a kill.

**Anti-triggers:** this skill does not analyze opportunities. It only enforces safety. For analysis, use the relevant analytical skill.

## Prerequisites

None — safety is unconditional.

## Kill conditions (any ONE triggers)

### Hard kills (automatic flatten, session lockout)

| Condition | Threshold | Action |
|---|---|---|
| Daily loss cap hit | −3% of account equity (default) | Flatten all, lock session |
| Weekly loss cap hit | −6% of account equity | Lock session until next week |
| Monthly loss cap hit | −12% of account equity | Lock session until next month |
| Consecutive stop-outs | 3 in a session | Flatten all, 1-hour cooldown minimum |
| Platform disconnect > 30s | continuous | Attempt reconnect; flatten if positions open and reconnect fails |
| State mismatch | agent state ≠ screen state | Flatten on screen state, investigate, lock |
| Trading halt on a held instrument | exchange notice | Do not attempt to trade halted instrument |
| Circuit breaker (market-wide) | SPX −7%/−13%/−20% | Stop all new entries until breaker clears |
| Margin call on screen | any | Flatten all, lock session, escalate |
| Unknown popup or 2FA prompt | any | Do not click; emit Z until popup resolved |
| Wrong account displayed | account name mismatch | Stop immediately, do not trade |

### Soft kills (no new X allowed, existing positions held)

| Condition | Threshold | Action |
|---|---|---|
| Intraday drawdown | −2% of account | Pause new X for 30 min |
| Session P&L volatility | > 2× normal stdev | Pause new X for 30 min |
| Three consecutive losses | any size | 30 min cooldown for new X |
| Unusually wide spreads | spread > 3× 20-day average | Pause X on that instrument |
| Liquidity drop | quoted size < 1/3 of normal | Pause X on that instrument |
| News blackout | ±5 min around high-impact | Pause X on the affected instrument |
| Low confidence streak | 5 consecutive Z in 10 min | Take a human check-in |

Soft kills do not force an exit — existing positions continue to run under their original stops/targets. They only block *new* entries.

## Decision procedure

1. Every clock tick / every skill call: check all hard-kill conditions.
2. If ANY hard kill fires:
   a. Immediately emit `Y` for all open positions with `reason: KILL_SWITCH`, `order_type: MARKET`.
   b. Wait for fill confirmation via `screenshot-vision-protocol`.
   c. Verify flat state on screen.
   d. Lock the session (no new X, no new Y initiated by strategy; only kill-switch-initiated Y allowed).
   e. Log to journal with full context.
   f. Escalate to human operator via the configured notification channel (if any).
   g. Remain locked until the reset protocol is completed.
3. If only soft kills fire: return `Z-OVERRIDE` for any new X proposed this tick. Existing positions run.
4. If no kill conditions are active: return `ok`, allow the calling skill to proceed.

## Reset protocol (after a hard kill)

The session is locked. Reset requires **all** of:
- Time gate: at least the minimum cooldown has passed (default 1h for consecutive stop-outs; full day for loss cap).
- Flat check: screen confirms no open positions, no working orders.
- State sync: agent internal state matches screen state.
- Human confirmation (if the hard kill was a state mismatch, margin call, or unknown popup).
- Journal entry: the kill event and the reset both logged with full context.
- Post-mortem: a short written analysis of what caused the kill, added to the journal.

Only after all of the above → unlock the session and return to normal operation.

## Interaction with buy-sell-hold-decision

- `safety-and-kill-switch` runs BEFORE `buy-sell-hold-decision`.
- If a hard kill fires, `safety-and-kill-switch` directly emits `Y` for all open positions (bypassing normal `buy-sell-hold-decision` aggregation).
- If a soft kill fires, `buy-sell-hold-decision` MUST downgrade any proposed X to `Z-OVERRIDE`.

## Heuristics & thresholds

- **Be paranoid.** False positive kills are cheap; false negatives are expensive.
- **Trust the screen.** If the screen says margin call and the agent "knows" there's no margin call — trust the screen.
- **Cooldown > re-entry.** Post-kill, the default is "wait," not "re-enter."
- **Flatten with market orders.** Kill-switch exits use `MARKET` to guarantee fill, accepting slippage.
- **Never trust internal state alone.** Screen state is authoritative during a kill event.

## Common failure modes

- **Disabling the kill switch "just this once."** Forbidden. Never skip the check.
- **Widening a cap to avoid a kill.** Forbidden. Caps are hard by design.
- **Auto-reset after a cooldown without human confirmation** (for mismatch-class kills). Forbidden.
- **Re-entering the same trade** that caused a 3-stop-out chain. Forbidden until the strategy is re-evaluated.
- **Flattening partial** during a hard kill. Hard kills flatten fully; partial is a soft kill.

## Outputs expected

```json
{
  "skill": "safety-and-kill-switch",
  "kill_state": "none" | "soft" | "hard",
  "triggered_conditions": ["daily-loss-cap", "three-consecutive-losses", "..."],
  "action": "allow" | "block-new-X" | "flatten-all" | "lock-session",
  "positions_to_flatten": ["AAPL-2026-03-14-entry", "..."],
  "reset_criteria_remaining": ["time-gate", "human-confirmation", "..."],
  "journal_refs": ["..."]
}
```

If `kill_state` = `hard`, the downstream `buy-sell-hold-decision` MUST emit `Y` for all positions and then `Z` for everything else until reset.

## References (lazy-load)

None by default — this skill is self-contained. Add `references/escalation-protocols.md` if the deployment has specific human-notification channels (Slack, email, SMS).

## Cross-links

- Pairs with: `risk-management` (caps), `screenshot-vision-protocol` (screen anomaly detection), `trade-journaling-and-backtesting` (logs all kill events), `buy-sell-hold-decision` (enforced via Z-OVERRIDE).
- Overrides: every other skill. Safety is absolute.

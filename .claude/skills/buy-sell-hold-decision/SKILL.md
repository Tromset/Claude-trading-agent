---
name: buy-sell-hold-decision
description: Use when any analysis or strategy skill has produced a conclusion and the agent needs to collapse it into a canonical X (buy), Y (sell), or Z (hold/do-nothing) action. This is the final output vocabulary for every decision.
---

# Buy / Sell / Hold Decision — The X / Y / Z Action Primitive

Every single decision the trading agent makes collapses to **exactly one** of three actions. This skill defines the vocabulary, the gates, the confidence rubric, and the JSON output schema.

## When to use this skill

- A strategy / analysis skill has finished its decision procedure and needs to produce a final action.
- The agent is aggregating multiple skill outputs and needs to emit a single result.
- The pre-trade checklist is being run and needs a canonical action to gate.

**Anti-triggers:** do NOT use this skill during analysis itself — only at the *end*, when the analysis has converged.

## Prerequisites

- `risk-management` must have produced sizing + stop + target for any `X` or `Y`.
- `safety-and-kill-switch` must not be active.
- `pre-trade-checklist-playbook` must be runnable (the final gate runs *after* this skill proposes an action).

## The three actions

### `X` = BUY

Open or add to a long position (or, in strategies that permit, close an existing short).

**Required fields before emitting X:**
| Field | Constraint |
|---|---|
| `ticker` | Exact symbol, including exchange if needed (e.g. `NASDAQ:AAPL`) |
| `side` | `BUY` (always) |
| `qty` | Positive integer (or fractional if broker supports), from `risk-management` |
| `order_type` | One of: `MARKET`, `LIMIT`, `STOP`, `STOP_LIMIT` |
| `entry_price` | Required for `LIMIT` / `STOP` / `STOP_LIMIT`; omitted for `MARKET` |
| `stop_loss` | Absolute price — mandatory |
| `target` | Absolute price — mandatory |
| `max_risk_currency` | Currency amount at risk if stop hits — mandatory, must ≤ per-trade cap |
| `time_in_force` | `DAY` / `GTC` / `IOC` / `FOK` |
| `rationale` | Free-text: which skills concluded X, what evidence |
| `confidence` | Integer 0–100 |

If **any** required field is missing or cannot be computed → downgrade to `Z`.

### `Y` = SELL

Close or reduce a long position, or open a short if the strategy permits.

**Required fields before emitting Y:**
| Field | Constraint |
|---|---|
| `position_ref` | Which position is being exited (ticker + original entry id) |
| `side` | `SELL` (always) — includes both long exit and short entry |
| `qty` | Positive integer — may be partial (scale-out) |
| `reason` | One of: `STOP_OUT`, `TARGET_HIT`, `THESIS_BREAK`, `TIME_STOP`, `RISK_REDUCTION`, `TRAIL_TIGHTENED`, `KILL_SWITCH` |
| `order_type` | Typically `MARKET` for stop-outs, `LIMIT` for targets |
| `exit_price` | For `LIMIT`; omit for `MARKET` |
| `rationale` | Free-text |
| `confidence` | Integer 0–100 |

If any required field is missing → downgrade to `Z`.

### `Z` = HOLD / DO NOTHING

**This is the default.** Emitted whenever:
- The agent cannot confidently justify `X` or `Y` (confidence < 60)
- A required field for `X` / `Y` is missing
- Any global invariant is threatened
- Any gate in the pre-trade checklist fails
- Two or more analyses disagree meaningfully
- Screen state is ambiguous or mismatched
- News blackout active
- `safety-and-kill-switch` has been triggered

**`Z` also includes:**
- Doing nothing while a position remains open (holding)
- Doing nothing while flat (waiting for a clearer setup)
- Cancelling a pending order that no longer makes sense

**Required fields for Z:**
| Field | Constraint |
|---|---|
| `reason` | Why Z — free text citing which gate/analysis led here |
| `would_have_been` | `X` / `Y` / `null` — what would have been emitted absent the block |
| `blocking_skill` | Which skill forced the downgrade (e.g., `pre-trade-checklist-playbook`) |
| `blocking_invariant` | Which global invariant (if any) triggered |

Only log Z when it *overrode* a would-be X or Y. Default Z (nothing was going to happen anyway) is silent.

## Decision procedure

1. Receive the inputs: analysis outputs from all loaded skills + risk-management output + situation summary.
2. Check every global invariant. If any fails → `Z` (with `blocking_invariant` set). STOP.
3. Check if any skill emitted `Y` (exit triggers). If yes:
   - Validate Y fields are complete.
   - If complete → propose `Y`. Go to step 6.
   - If incomplete → `Z` (with rationale). STOP.
4. Check if any skill emitted `X` (entry triggers). If yes:
   - Validate X fields are complete (especially `risk-management` output).
   - If complete → propose `X`. Go to step 6.
   - If incomplete → `Z` (with rationale). STOP.
5. No X or Y proposed → `Z` by default (silent unless this would have been a would-be action).
6. Compute confidence (see rubric). If confidence < 60 → downgrade to `Z`.
7. Check if `pre-trade-checklist-playbook` will be run next (it always should be). Note: the checklist may override to `Z` — this skill does not have final authority.
8. Emit the JSON output (schema below).

## Confidence rubric (0–100)

Confidence is the weighted sum of evidence quality across independent dimensions.

| Dimension | Max points | How to score |
|---|---|---|
| Trend / structure agreement | 20 | Higher-timeframe trend aligns with the trade direction |
| Entry trigger clarity | 20 | Clean pattern/level, not forced |
| Volume confirmation | 15 | Volume supports the move (for breakouts); or divergence (for reversals) |
| Risk-reward ratio | 15 | R:R ≥ 2:1 full marks; ≥ 1.5 partial; < 1.5 zero |
| No conflicting signals | 10 | No major counter-signal on same timeframe |
| No pending catalyst | 10 | No high-impact news in next 24h (for swing) / next hour (for day) |
| Position in portfolio heat | 10 | Fits within heat cap cleanly |
| **Total** | **100** | |

**Gates:**
- Confidence ≥ 80 → high conviction, proceed to checklist
- Confidence 60–79 → proceed with reduced size (0.5×)
- Confidence < 60 → downgrade to `Z`

## Output JSON schema

```json
{
  "skill": "buy-sell-hold-decision",
  "timestamp": "2026-04-11T14:23:17Z",
  "action": "X" | "Y" | "Z",
  "confidence": 0-100,
  "payload": {
    // for X:
    "ticker": "NASDAQ:AAPL",
    "side": "BUY",
    "qty": 119,
    "order_type": "LIMIT",
    "entry_price": 182.05,
    "stop_loss": 177.80,
    "target": 192.00,
    "max_risk_currency": 505.75,
    "time_in_force": "DAY",

    // for Y:
    "position_ref": "AAPL-2026-03-14-entry",
    "reason": "TARGET_HIT",
    // ...

    // for Z:
    "reason": "Confidence 54 below 60 threshold",
    "would_have_been": "X",
    "blocking_skill": "buy-sell-hold-decision",
    "blocking_invariant": null
  },
  "rationale": "Short free-text summary of which skills supported the decision and why",
  "skills_invoked": ["price-action-and-market-structure", "risk-management", "..."],
  "invariants_checked": ["risk-before-return", "news-blackout", "caps-are-hard", "..."]
}
```

The downstream system (pre-trade-checklist, execution, journal) parses this schema.

## Heuristics & thresholds

- **Z beats X beats nothing.** If you're not sure → Z.
- **Completeness beats conviction.** A confident X with a missing stop is still Z.
- **One strong Y beats three weak X's.** Exit discipline is more valuable than entry discipline.
- **Silent Z is fine.** Do not spam the journal with "thought about it, didn't do it."
- **Loud Z is mandatory.** If you were going to X or Y and something stopped you, log it.
- **Confidence inflation is the enemy.** Prefer being harshly honest; err on the low side.

## Common failure modes

- **Phantom X.** Emitting X without a complete order spec. Always require all fields.
- **Premature X.** Emitting X before risk-management has sized the trade. Order matters.
- **Missed Y.** Holding past the stop "just a little longer." Stops are binary — hit = Y.
- **Confidence inflation.** Scoring conflicting signals as confluence. Double-check independence.
- **Silent override.** Downgrading to Z without logging why. Always log the block.
- **Ignoring checklist authority.** This skill proposes; the checklist disposes. Never skip it.

## Outputs expected

Exactly one JSON object matching the schema above. No prose, no ambiguity. The schema is the contract.

## References (lazy-load)

- `references/xyz-action-vocabulary.md` — formal definitions, edge cases, short-selling handling.
- `references/buy-triggers.md` — canonical conditions under which X is justified.
- `references/sell-triggers.md` — canonical conditions under which Y is justified.
- `references/hold-triggers.md` — when Z is the correct answer (long list; Z is the default).

## Cross-links

- Pairs with: `risk-management` (provides sizing for X/Y), `pre-trade-checklist-playbook` (final gate), `trading-master` (router that calls this skill last), `trade-journaling-and-backtesting` (logs every X/Y and every loud Z).

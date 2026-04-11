---
name: trading-master
description: Use when the cowork trading agent first boots or needs to route a new situation to the right sub-skills. Loads global invariants, the decision tree, and the skill index.
---

# Trading Master — Router & Global Invariants

This is the **root skill**. Load it first. It holds the decision tree that routes every situation to the correct downstream skills, the X/Y/Z contract, and the global invariants every action must obey.

## When to use this skill

- Fresh session boot — before any other skill.
- The agent is handed a new screenshot or prompt and does not yet know which skills to load.
- The agent finishes a trade and needs to return to the default scanning state.
- The user asks a broad question like "what should I do?" with no specific skill named.

**Anti-triggers:** do NOT use this skill for deep analysis — it only routes. Once routed, defer to the downstream skill.

## Prerequisites

None. This is the root.

## The Global Invariants (never violate)

1. **Risk before return.** No `X` or `Y` without a fresh `risk-management` output.
2. **Screen is truth.** No click without `screenshot-vision-protocol` pre-click verification.
3. **Caps are hard.** Never exceed account daily-loss, per-trade risk, or portfolio heat caps.
4. **Journal everything.** Every `X`, `Y`, and every `Z` that overrode a would-be action.
5. **Mismatch = abort.** Screen state ≠ internal state → `safety-and-kill-switch` → `Z`.
6. **ToS first.** Broker, exchange, and regulatory rules override this library.
7. **News blackout.** No discretionary action in the ±5 min window around a high-impact event for the instrument, unless the strategy is a pre-planned event trade.
8. **Z is the default.** Any ambiguity → `Z`.

The agent MUST cite the relevant invariant any time it emits `Z` as an override.

## The X / Y / Z Contract (output vocabulary)

Every decision collapses to **exactly one** of:

- **`X` = BUY** — open or add to a long position (or close a short). Requires a full order spec: ticker, side, qty, entry type/price, stop, target, max risk in currency.
- **`Y` = SELL** — close or reduce a long position, or open a short if the strategy permits. Requires: position reference, reason (`stop-out` / `target` / `thesis-break` / `time-stop` / `risk-reduction`), exit order type.
- **`Z` = HOLD / DO NOTHING** — no action. The *default*. Emitted whenever conditions are ambiguous, incomplete, or not confidently `X`/`Y`.

See `buy-sell-hold-decision/SKILL.md` for the formal definitions, confidence rubric, and JSON output schema.

## Routing Decision Tree

Read the current situation and follow the first matching branch. Stop at the first match.

```
IF kill-switch active OR daily-loss cap hit OR anomaly detected
  → load safety-and-kill-switch → emit Z

ELSE IF screenshot is unfamiliar / ambiguous / popup blocking
  → load screenshot-vision-protocol + trading-app-ui-navigation → emit Z until resolved

ELSE IF news blackout window active for the instrument
  → load news-and-macro-awareness → emit Z

ELSE IF currently holding a position
  → load risk-management (check exit triggers)
  → load the strategy skill that opened the position
  → IF exit trigger fires → emit Y
  → ELSE emit Z

ELSE IF scanning for new opportunity (no position)
  BRANCH by time-horizon intent:
    long-horizon / value
      → fundamental-analysis-and-value-investing
      → watchlist-and-screening
      → news-and-macro-awareness
      → risk-management
      → buy-sell-hold-decision
    swing / position-trading (days to weeks)
      → price-action-and-market-structure
      → chart-patterns
      → support-resistance-and-fibonacci
      → volume-analysis
      → technical-indicators
      → risk-management
      → buy-sell-hold-decision
    day-trading (intraday)
      → price-action-and-market-structure
      → volume-analysis
      → technical-indicators
      → risk-management
      → buy-sell-hold-decision

ELSE IF evaluating an options / futures trade
  → derivatives-options-and-futures
  → risk-management
  → buy-sell-hold-decision

ELSE IF evaluating a crypto trade
  → crypto-trading-specifics
  → risk-management
  → buy-sell-hold-decision

ELSE → emit Z (nothing to do)
```

Before every action, **always** run `pre-trade-checklist-playbook`. The checklist has final veto authority: even a confident `X` becomes `Z` if any gate fails.

## Decision Procedure

1. Receive the situation (screenshot + prompt).
2. Check global invariants. If any is violated → `safety-and-kill-switch` → `Z`.
3. Walk the routing decision tree above. Load the first matching set of skills.
4. Execute the downstream skills' decision procedures in order.
5. Collect their outputs (each emits `X`, `Y`, or `Z` with justification and confidence).
6. Aggregate: if any skill emits `Z` with higher priority (safety > risk > strategy), the aggregate is `Z`.
7. Run `pre-trade-checklist-playbook`. If any gate fails → override to `Z`.
8. Emit the final action via `buy-sell-hold-decision` output schema.
9. If action ∈ {`X`, `Y`}, drive execution through `screenshot-vision-protocol` + `trading-app-ui-navigation` + `order-types-execution`.
10. Log the result via `trade-journaling-and-backtesting`.

## Heuristics & thresholds

- When in doubt between two skills, load the more conservative one.
- Prefer higher-timeframe evidence over lower-timeframe noise.
- If confidence < 60 on any X/Y → downgrade to Z.
- If any single screenshot is < 95% unambiguous → pre-click fails → Z.
- If three consecutive Z decisions on the same setup → log "watching" and move on.

## Common failure modes

- **Over-routing.** Loading every skill for every situation. Route narrowly — only what the branch calls for.
- **Skipping the checklist.** The checklist is mandatory, not optional. It catches what the strategy missed.
- **Acting on stale screenshots.** Always refresh before the click.
- **Ignoring invariants.** Invariants override strategy output every time.
- **Double-counting confluence.** RSI + Stochastic are both momentum — they don't independently confirm each other.

## Outputs expected

The trading-master skill itself does not emit the final action — it emits a **routing decision**:

```json
{
  "skill": "trading-master",
  "situation_summary": "...",
  "invariants_ok": true,
  "routed_skills": ["risk-management", "price-action-and-market-structure", "..."],
  "next_action": "run downstream skills",
  "notes": "..."
}
```

The final `X` / `Y` / `Z` is emitted by `buy-sell-hold-decision` after the downstream pass.

## References (lazy-load)

- `references/skill-index.md` — machine-readable list of every skill + one-line purpose.
- `references/global-invariants.md` — expanded rationale and failure cases for each invariant.
- `references/decision-tree.md` — full routing tree with worked examples.

## Cross-links

- Pairs with: `buy-sell-hold-decision` (final output), `pre-trade-checklist-playbook` (final gate), `safety-and-kill-switch` (emergency override).

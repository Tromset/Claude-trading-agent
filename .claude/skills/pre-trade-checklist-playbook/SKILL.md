---
name: pre-trade-checklist-playbook
description: Use when an X (buy) or Y (sell) action has been proposed to run the mandatory 12-step verification gate before execution.
---

# Pre-Trade Checklist Playbook — The Final Gate

The last word before any trade executes. Even if `buy-sell-hold-decision` emits a confident X or Y, this checklist can override it to Z if any gate fails. No trade bypasses these 12 steps. None. Ever.

## When to use this skill

- After `buy-sell-hold-decision` has proposed an X (buy) or Y (sell).
- Before any order is placed on the platform.
- This skill is the FINAL gate in the decision chain: analysis -> strategy -> risk -> decision -> **checklist** -> execution.

**Anti-triggers:** do NOT run this checklist for Z (hold) actions. Z is already a no-op. Only X and Y proposals pass through this gate.

## Prerequisites

- A fully formed X or Y from `buy-sell-hold-decision`, with all required fields populated.
- `risk-management` output attached (sizing, stops, targets, heat).
- A fresh screenshot available or obtainable (for step 10).
- Access to current market state (for steps 1, 2, 8).

## Authority

This skill has **absolute override authority**. It outranks every other skill except `safety-and-kill-switch` (which runs even earlier). If `buy-sell-hold-decision` says X with 95 confidence and this checklist fails at step 6, the result is Z. No exceptions. No "just this once."

## The 12-Step Checklist

Run all steps **sequentially**. Fail-fast: if any step fails, immediately emit Z with the failing step noted. Do NOT continue checking after a failure.

### Step 1: Market Regime Check

Is the market open? Is this instrument trading in regular hours? Any halts?

- Skills invoked: `trading-fundamentals`, `market-microstructure`
- Pass: market is open, instrument is in regular session, no halts active
- Fail: market closed, instrument halted, pre/post-market without explicit strategy permission

### Step 2: News / Macro Check

Any high-impact events in the next 30 minutes? Earnings within 24 hours? FOMC announcement?

- Skill invoked: `news-and-macro-awareness`
- Pass: no high-impact events within the blackout window
- Fail: high-impact event pending within window, earnings imminent, FOMC day without explicit macro-strategy

### Step 3: Strategy Alignment

Does the proposed trade match a defined strategy? Which one?

- Skill invoked: `trading-strategies-playbook`
- Pass: trade maps to a named strategy with defined entry/exit rules
- Fail: trade is ad-hoc, does not match any defined strategy, or contradicts the matched strategy's rules

### Step 4: Technical Confirmation

Do price action, patterns, indicators, support/resistance, and volume align? Minimum 3 out of 5 confluence required.

- Skills invoked: `price-action-and-market-structure`, `chart-patterns`, `technical-indicators`, `support-resistance-and-fibonacci`, `volume-analysis`
- Pass: >= 3 of the 5 technical dimensions confirm the trade direction
- Fail: < 3 confirm, or any dimension actively contradicts

### Step 5: Fundamental Check (if applicable)

For position trades or Buffett-style candidates: does the company pass the fundamental screen?

- Skill invoked: `fundamental-analysis-and-value-investing`
- Pass: company passes the fundamental screen (or step is N/A for day/swing trades)
- Fail: company fails the fundamental screen on a position trade

### Step 6: Risk Sizing (NON-OVERRIDABLE)

Is position size <= 1% account risk? Is R:R >= 2:1? Is portfolio heat <= 6%?

- Skill invoked: `risk-management`
- Pass: all three caps satisfied
- Fail: any cap exceeded
- **This step cannot be overridden, even by a human operator.** The 1% per-trade cap is absolute.

### Step 7: Order Specification

Is the order fully specified? Ticker, side, qty, entry type/price, stop, target all defined?

- Skill invoked: `order-types-execution`
- Pass: every required field in the X or Y schema is populated with a valid value
- Fail: any required field is missing, null, or out of valid range

### Step 8: Safety Check (NON-OVERRIDABLE)

Any kill-switch triggers active? Daily loss limit hit? Consecutive loss streak?

- Skill invoked: `safety-and-kill-switch`
- Pass: `kill_state` = `none`, no hard or soft kills active
- Fail: any kill condition active
- **Hard kill triggers cannot be overridden.** Soft kills block new X but allow existing Y exits.

### Step 9: Platform Verification

Correct account loaded (paper vs live)? Correct ticker displayed?

- Skill invoked: `trading-app-ui-navigation`
- Pass: account matches expected mode (paper or live), correct ticker loaded
- Fail: wrong account, wrong ticker, platform not recognized

### Step 10: Screenshot Verification (NON-OVERRIDABLE)

Fresh screenshot taken? 7-step vision protocol passed? Pre-click fields match order spec?

- Skill invoked: `screenshot-vision-protocol`
- Pass: screenshot is fresh (< 5 seconds), all 7 vision steps pass, every field matches intent
- Fail: stale screenshot, any vision step fails, any field mismatch
- **Screenshot freshness is non-overridable.** A stale or missing screenshot is always a fail.

### Step 11: Confidence Gate

Is confidence >= 60? If in paper mode, >= 50 is allowed.

- Skill invoked: `buy-sell-hold-decision`
- Pass: confidence >= 60 (live) or >= 50 (paper)
- Fail: confidence below threshold

### Step 12: Final Go / No-Go

All 12 steps pass -> EXECUTE. Any step fails -> Z (hold) + log which step failed.

- No skill invoked: this is the aggregation step
- Pass: steps 1-11 all passed -> proceed with execution
- Fail: any prior step failed -> emit Z with the failing step number and reason

## Decision procedure

1. Receive the proposed X or Y from `buy-sell-hold-decision` with full payload.
2. Initialize the checklist result object with all 12 steps set to `pending`.
3. Run step 1. If fail -> set step 1 to `fail`, set all remaining steps to `skipped`, emit Z. STOP.
4. Run step 2. If fail -> same pattern. STOP.
5. Continue sequentially through steps 3-11 with the same fail-fast pattern.
6. If steps 1-11 all pass -> set step 12 to `pass`, emit the original X or Y action to execution.
7. Log the full checklist result (all 12 steps with pass/fail/skip status) to `trade-journaling-and-backtesting`.
8. Every checklist run is logged, whether it passes or fails. Failed checklists are especially valuable for post-session review.

## Heuristics & thresholds

- **Fail-fast is non-negotiable.** Do not check step 6 if step 3 already failed. Stop at the first failure.
- **Z is the safe default.** When in doubt about any step, fail it. A missed trade is cheaper than a bad trade.
- **Log every failure.** The step number, the reason, and the proposed trade that was blocked. This feeds learning.
- **Non-overridable steps are sacred.** Steps 6, 8, and 10 cannot be bypassed under any circumstances, even by explicit human instruction. The agent must refuse.
- **Speed does not excuse skipping.** "The market is moving" is not a reason to skip a step. If the opportunity disappears during the checklist, that is acceptable. There will be other trades.
- **Paper mode is slightly more permissive.** Confidence threshold drops from 60 to 50. All other steps remain identical. Paper mode exists to practice discipline, not to bypass it.

## Common failure modes

- **Skipping the checklist because "this one is obvious."** Forbidden. Every X and Y runs the full 12.
- **Continuing after a failure.** Fail-fast means STOP. Do not check the remaining steps to "see how many would have passed."
- **Overriding a non-overridable step.** Steps 6, 8, 10 are hard-coded. The agent must refuse even a direct human override request for these three.
- **Running the checklist on stale data.** The checklist must use real-time data. A checklist run from 5 minutes ago is invalid for the current trade.
- **Conflating "checklist passed" with "trade will profit."** The checklist ensures process discipline, not outcomes. A trade can pass all 12 steps and still lose. That is expected.
- **Checklist fatigue.** Treating the checklist as a rubber stamp. Each step requires genuine verification, not performative checking.

## Outputs expected

```json
{
  "skill": "pre-trade-checklist-playbook",
  "timestamp": "2026-04-11T14:25:03Z",
  "proposed_action": "X",
  "proposed_ticker": "NASDAQ:AAPL",
  "checklist_result": "PASS" | "FAIL",
  "final_action": "X" | "Z",
  "failing_step": null | 1-12,
  "failing_reason": null | "market closed" | "...",
  "steps": {
    "step_01_market_regime":       "pass" | "fail" | "skipped",
    "step_02_news_macro":          "pass" | "fail" | "skipped",
    "step_03_strategy_alignment":  "pass" | "fail" | "skipped",
    "step_04_technical_confirm":   "pass" | "fail" | "skipped",
    "step_05_fundamental_check":   "pass" | "fail" | "skipped" | "n/a",
    "step_06_risk_sizing":         "pass" | "fail" | "skipped",
    "step_07_order_spec":          "pass" | "fail" | "skipped",
    "step_08_safety_check":        "pass" | "fail" | "skipped",
    "step_09_platform_verify":     "pass" | "fail" | "skipped",
    "step_10_screenshot_verify":   "pass" | "fail" | "skipped",
    "step_11_confidence_gate":     "pass" | "fail" | "skipped",
    "step_12_final_go_nogo":       "pass" | "fail" | "skipped"
  },
  "non_overridable_steps_status": {
    "step_06": "pass" | "fail",
    "step_08": "pass" | "fail" | "skipped",
    "step_10": "pass" | "fail" | "skipped"
  },
  "skills_invoked": [
    "trading-fundamentals",
    "market-microstructure",
    "news-and-macro-awareness",
    "trading-strategies-playbook",
    "price-action-and-market-structure",
    "chart-patterns",
    "technical-indicators",
    "support-resistance-and-fibonacci",
    "volume-analysis",
    "fundamental-analysis-and-value-investing",
    "risk-management",
    "order-types-execution",
    "safety-and-kill-switch",
    "trading-app-ui-navigation",
    "screenshot-vision-protocol",
    "buy-sell-hold-decision"
  ],
  "checklist_duration_ms": 1200,
  "journal_ref": "checklist-2026-04-11-142503"
}
```

The downstream execution system reads `final_action`. If `PASS` and `final_action` = X or Y, the order is submitted via `screenshot-vision-protocol`. If `FAIL`, the proposed action is dead.

## References (lazy-load)

- `references/checklist-12-step.md` -- detailed breakdown of each step with pass/fail criteria, override rules, common false-fails, and a worked example.

## Cross-links

This skill is the orchestrator. It touches every other skill in the system:

- **Upstream (provides the proposal):** `buy-sell-hold-decision`
- **Downstream (receives the approved action):** `screenshot-vision-protocol` (execution), `trade-journaling-and-backtesting` (logging)
- **Step 1:** `trading-fundamentals`, `market-microstructure`
- **Step 2:** `news-and-macro-awareness`
- **Step 3:** `trading-strategies-playbook`
- **Step 4:** `price-action-and-market-structure`, `chart-patterns`, `technical-indicators`, `support-resistance-and-fibonacci`, `volume-analysis`
- **Step 5:** `fundamental-analysis-and-value-investing`
- **Step 6:** `risk-management`
- **Step 7:** `order-types-execution`
- **Step 8:** `safety-and-kill-switch`
- **Step 9:** `trading-app-ui-navigation`
- **Step 10:** `screenshot-vision-protocol`
- **Step 11:** `buy-sell-hold-decision`
- **Step 12:** (aggregation -- no external skill)
- **Always active:** `trading-master` (router), `trading-psychology` (bias monitoring)
- **Peripheral:** `paper-trading-workflow` (adjusts confidence threshold), `regulations-and-tax-awareness` (PDT/wash-sale awareness), `broker-and-platform-selection` (platform capabilities), `watchlist-and-screening` (candidate universe), `derivatives-options-and-futures` (if applicable), `crypto-trading-specifics` (if applicable), `systematic-and-algo-trading` (if applicable)

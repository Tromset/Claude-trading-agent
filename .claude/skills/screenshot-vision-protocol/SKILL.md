---
name: screenshot-vision-protocol
description: Use when the agent must visually parse a trading app screenshot before any click action, to verify fields, detect anomalies, and ensure pre-click safety before emitting X or Y.
---

# Screenshot Vision Protocol

The *how to look* discipline. Before any click, the agent must see, read, verify, and confirm. This skill is the bridge between analysis (which produces X/Y/Z) and execution (which clicks buttons). No click without this protocol.

## When to use this skill

- Before EVERY click on a trading platform (order submission, modification, cancellation).
- After every click to verify the expected state change occurred.
- When the agent first opens a platform session (identify the platform, map regions).
- When anything unexpected appears on screen (popup, error, unfamiliar layout).
- When `trading-master` routes a new situation and the screenshot needs initial parsing.

**Anti-triggers:** not needed for pure analysis (reading a chart to identify patterns). Only needed when the agent is about to *act* on the platform.

## Prerequisites

- A fresh screenshot (< 5 seconds old; stale screenshots are forbidden).
- The platform has been identified (see `trading-app-ui-navigation`).
- The agent has an intent (what it plans to do — from `buy-sell-hold-decision`).

## Core concepts

### The 7-Step Vision Protocol

Every interaction with the trading platform follows this sequence:

```
1. CAPTURE  → take a fresh screenshot
2. ORIENT   → identify the platform and locate key regions
3. READ     → extract values from the relevant region
4. VERIFY   → compare every field to the agent's intent
5. CONFIRM  → check for blocking elements (popups, warnings)
6. ACT      → emit the click/type command (or abort)
7. VALIDATE → re-screenshot and verify the expected change
```

### Step 1: CAPTURE

- Always take a NEW screenshot. Never reason about a remembered screen.
- If the screenshot fails or times out → `Z` + log "capture failed."
- Timestamp the capture. If the agent's last capture was > 30s ago when it tries to act → re-capture.

### Step 2: ORIENT

Identify which platform is displayed (TradingView, Webull, Robinhood, TOS, MT5, or unknown). Use visual cues:
- Logo / branding in header.
- Layout structure (see `trading-app-ui-navigation` region maps).
- Color scheme, font style.

If the platform is **unknown** → emit `Z`, log "unrecognized platform," escalate. Do NOT interact with an unrecognized interface.

Map the visible regions:
- Chart area (center, typically largest region).
- Order ticket / order panel (usually right side or popup).
- Watchlist (usually left sidebar).
- Positions / orders / history (usually bottom panel).
- Account bar (top bar — shows account name, cash, buying power).

### Step 3: READ

From the relevant region for the intended action, extract:

**For an order submission (X or Y action):**
| Field | Where to look | Example |
|---|---|---|
| Symbol / ticker | Order ticket header or input field | "AAPL" |
| Side | BUY / SELL button highlight or text | "BUY" (green) |
| Quantity | Qty input field | "119" |
| Order type | Dropdown or toggle | "LIMIT" |
| Limit price | Price input field | "182.05" |
| Stop price | Stop input field (if stop order) | "177.80" |
| Time-in-force | TIF selector | "DAY" |
| Account | Account dropdown (if multiple) | "Individual - xxxx1234" |
| Bid / Ask | Quote display near order ticket | "181.95 / 182.10" |
| Estimated cost | Total or cost estimate field | "$21,663.95" |

**For chart reading (analysis):**
| Field | Where to look |
|---|---|
| Ticker + exchange | Top-left of chart or symbol search bar |
| Timeframe | Timeframe selector (1m, 5m, 15m, 1H, 4H, D, W) |
| Current price | Last price on the right axis or ticker display |
| Indicator values | Indicator overlays or sub-panels |

### Step 4: VERIFY

Compare **every** extracted field to the agent's intent:

```
intent.symbol    == screen.symbol    ? ✓ : ABORT
intent.side      == screen.side      ? ✓ : ABORT
intent.qty       == screen.qty       ? ✓ : ABORT
intent.order_type == screen.order_type ? ✓ : ABORT
intent.limit_price == screen.limit_price ? ✓ : ABORT (within ±$0.01 tolerance)
intent.stop_price  == screen.stop_price  ? ✓ : ABORT
intent.tif       == screen.tif       ? ✓ : ABORT
intent.account   == expected_account ? ✓ : ABORT
```

**Any single mismatch → ABORT → emit `Z-OVERRIDE` with `blocking_skill: screenshot-vision-protocol`.**

Common mismatches to watch for:
- Platform auto-filled a previous ticker (shows MSFT when intent is AAPL).
- Qty defaulted to a platform default (100) instead of computed size (119).
- Account selector switched to a different account (paper vs live).
- TIF defaulted to GTC when intent is DAY.
- Side defaulted to BUY when intent is SELL.

### Step 5: CONFIRM

Check for blocking elements:
- **Popups:** 2FA prompt, "Are you sure?" confirmation, margin warning, error dialog.
- **Warnings:** insufficient funds, pattern day trader warning, position limit warning.
- **Platform state:** connected vs disconnected, live vs paper, session status.

If any popup or warning is present → do NOT click through it automatically. Emit `Z`, log the popup content, escalate to `safety-and-kill-switch`.

Exception: if the popup is the platform's standard order confirmation dialog ("Confirm order: BUY 119 AAPL LIMIT $182.05 DAY") and all fields match intent → this is expected. Click "Confirm."

### Step 6: ACT

Only after steps 1-5 pass. Emit the click command for the submit button.

- Identify the submit button visually (typically "Buy" / "Sell" / "Place Order" / "Submit").
- Click it.
- Do NOT double-click. One click only. Wait for response.

### Step 7: VALIDATE

Re-screenshot immediately after the click.

- Verify the order appeared in the "Orders" or "Working Orders" panel.
- Verify the order details match intent (ticker, side, qty, type, price).
- If the order is a market order, check if it filled immediately and verify the fill price.
- If the screen shows an error ("Order rejected," "Insufficient buying power," etc.) → log the error, emit `Z`, escalate.

If validation passes → the action is complete. Log to `trade-journaling-and-backtesting`.

## Decision procedure

1. Receive intent from `buy-sell-hold-decision` (X or Y with full order spec).
2. Run the 7-step protocol above.
3. If any step fails → emit `Z-OVERRIDE`, log the failure step and reason.
4. If all steps pass → the order is placed and validated.
5. Return the validation result to the calling skill.

## Heuristics & thresholds

- **Stale threshold:** > 30 seconds since last capture → re-capture before any action.
- **Mismatch tolerance:** prices within ±$0.01 due to rounding; all other fields must be exact.
- **Popup handling:** NEVER click through an unexpected popup. Always `Z` + escalate.
- **Unknown platform:** NEVER interact. `Z` + escalate.
- **Multiple monitors / tabs:** if the agent can see multiple windows, focus only on the active trading window. Ignore secondary windows.

## Common failure modes

- **Acting on stale screenshots.** Always re-capture. Memory is not the screen.
- **Clicking through warnings without reading them.** Margin warnings, PDT warnings are CRITICAL. Never dismiss automatically.
- **Wrong account.** The most dangerous single-field mismatch. Paper vs live is catastrophic.
- **Trusting auto-fill.** Platforms remember last-used values. Always verify from scratch.
- **Double-clicking submit.** Creates duplicate orders. One click, then validate.
- **Not validating post-click.** The order might have been rejected silently.

## Outputs expected

```json
{
  "skill": "screenshot-vision-protocol",
  "step_results": {
    "capture": "ok",
    "orient": {"platform": "tradingview", "regions_identified": true},
    "read": {"symbol": "AAPL", "side": "BUY", "qty": 119, "...": "..."},
    "verify": "all_match" | "mismatch_detected",
    "confirm": "no_blockers" | "popup_detected",
    "act": "click_submitted" | "aborted",
    "validate": "order_confirmed" | "error_detected"
  },
  "final_status": "success" | "aborted",
  "abort_reason": null | "symbol_mismatch" | "popup_blocking" | "...",
  "screenshot_refs": ["capture_before.png", "capture_after.png"]
}
```

## References (lazy-load)

- `references/pre-click-verification.md` — the full pre-click checklist with examples.
- `references/error-recovery.md` — recovery paths for every type of screen anomaly.

## Cross-links

- Pairs with: `trading-app-ui-navigation` (what to see), `buy-sell-hold-decision` (provides intent), `order-types-execution` (order fields), `safety-and-kill-switch` (abort target), `pre-trade-checklist-playbook` (gate 12).

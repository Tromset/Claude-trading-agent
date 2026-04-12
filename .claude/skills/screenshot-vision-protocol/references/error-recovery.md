# Error Recovery — Handling Screen Anomalies

When something unexpected appears on the trading platform screen, the default is always **pause → Z → escalate**. Never click through an anomaly.

## Recovery paths by anomaly type

### Connection errors

**Symptoms:** "Disconnected," "Connection lost," grayed-out interface, spinning loader, frozen prices.

**Recovery:**
1. Emit `Z` immediately.
2. Do NOT submit any orders — they may queue and fire unexpectedly on reconnection.
3. Wait 30 seconds. Re-screenshot.
4. If reconnected → re-orient, verify positions match expected state.
5. If still disconnected after 60 seconds → escalate to `safety-and-kill-switch`.
6. If positions are open and connection is lost → the resting stops/targets on the broker server should protect. Do NOT attempt to manually manage.

### 2FA / Authentication prompts

**Symptoms:** popup asking for authentication code, SMS verification, device confirmation.

**Recovery:**
1. Emit `Z`. Do NOT enter codes automatically.
2. Log the prompt type and content.
3. Escalate to the human operator — 2FA requires human interaction.
4. Session is effectively paused until the human resolves the prompt.
5. After resolution, re-orient the entire screen before any action.

### Margin warnings / calls

**Symptoms:** "Margin call," "Maintenance requirement not met," "Liquidation warning."

**Recovery:**
1. Emit `Z` for all new actions.
2. Immediately route to `safety-and-kill-switch` with condition `margin-call`.
3. The kill switch will determine whether to flatten positions.
4. Do NOT attempt to deposit funds or adjust margin — that's human territory.
5. Log the warning content verbatim.

### PDT warnings

**Symptoms:** "Pattern Day Trader warning," "This trade would be your Nth day trade."

**Recovery:**
1. ABORT the current action → `Z-OVERRIDE`.
2. Route to `regulations-and-tax-awareness` to re-count day trades.
3. Do NOT dismiss the warning — log its content.
4. The order was NOT placed (the warning blocked it).
5. Reconsider the trade: can it be held overnight instead of day-traded?

### Order rejection

**Symptoms:** "Order rejected," "Insufficient buying power," "Symbol not found," "Outside trading hours."

**Recovery:**
1. Log the rejection reason verbatim.
2. Do NOT resubmit the same order automatically.
3. Diagnose the cause:
   - Insufficient funds → reduce qty via `risk-management` or skip (`Z`).
   - Symbol not found → verify the ticker is correct, check if the market is open.
   - Outside trading hours → check `order-types-execution` for extended-hours order types (LIMIT + EXT TIF only).
   - Unknown reason → `Z` + escalate.
4. If the diagnosis produces a valid corrected order → re-run the full 7-step protocol from scratch.

### Unexpected popups (non-trading)

**Symptoms:** "Platform update available," "New feature announcement," "Survey," cookie consent, ad.

**Recovery:**
1. Do NOT click any button on the popup.
2. If the popup has an "X" (close) button and the agent is confident it's a dismissible non-trading popup → close it. Re-screenshot to verify it's gone.
3. If the popup is ambiguous or covers the order area → `Z` + escalate. The human should dismiss it.
4. After dismissal, re-run ORIENT to confirm the underlying screen is intact.

### "Are you sure?" confirmation dialogs

**Symptoms:** "Confirm order," "Review your order," with a summary of the order and Confirm/Cancel buttons.

**Recovery:**
1. This is EXPECTED for most brokers.
2. Read the confirmation dialog fields carefully — they are the LAST checkpoint.
3. Verify every field in the dialog matches intent (just like pre-click verification).
4. If all fields match → click "Confirm."
5. If any field differs from intent → click "Cancel" → ABORT → `Z-OVERRIDE`.

### Trading halts

**Symptoms:** "Trading halted," "LULD pause," no bid/ask displayed, price frozen.

**Recovery:**
1. Do NOT attempt to trade a halted instrument.
2. Emit `Z`.
3. If holding a position in the halted instrument:
   - Resting stops/targets will execute when trading resumes (on most brokers).
   - Do NOT cancel resting orders during a halt.
   - Log the halt time and wait.
4. After trading resumes → re-screenshot, check position state, resume normal protocol.

### Wrong account displayed

**Symptoms:** account name/number in the header does not match the expected account.

**Recovery:**
1. CRITICAL ABORT. This is the most dangerous anomaly.
2. Emit `Z` immediately. Do NOT trade on the wrong account.
3. Do NOT attempt to switch accounts — the agent might accidentally trade on the wrong one during the switch.
4. Escalate to human operator.
5. Verify: are there any positions on the wrong account that the agent didn't place? If yes → `safety-and-kill-switch` for investigation.

### Screen layout changed (platform update)

**Symptoms:** familiar platform but layout has shifted — buttons moved, panels rearranged, new UI elements.

**Recovery:**
1. Emit `Z` — the agent's region map is stale.
2. Re-orient using `trading-app-ui-navigation` generic region map.
3. If the new layout can be mapped to the generic model → update the agent's region understanding and proceed cautiously.
4. If the layout is unrecognizable → treat as unknown platform → `Z` + escalate.

### Multiple windows / tabs

**Symptoms:** more than one trading window visible, or the agent accidentally focused a non-trading window.

**Recovery:**
1. Identify which window is the active trading session.
2. Ignore all other windows.
3. If the windows show different accounts → CRITICAL ABORT, same as "wrong account."
4. Ensure clicks are targeted to the correct window.

## Default recovery (for any unlisted anomaly)

```
1. Do NOT click anything.
2. Emit Z.
3. Take a screenshot and log it with description of what's unexpected.
4. Escalate to safety-and-kill-switch.
5. Wait for human resolution or automated reset.
```

The cost of pausing is near zero. The cost of clicking through an unknown screen is potentially catastrophic.

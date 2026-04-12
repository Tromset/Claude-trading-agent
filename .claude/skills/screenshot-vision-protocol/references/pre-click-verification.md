# Pre-Click Verification Checklist

This checklist runs after ORIENT + READ and before ACT. Every field must pass. Any failure → abort → Z.

## Order Submission Checklist

| # | Check | Pass condition | Common failure |
|---|---|---|---|
| 1 | **Symbol** | Screen symbol exactly matches intent symbol (including exchange prefix if shown) | Platform auto-filled a previous symbol |
| 2 | **Side** | BUY/SELL on screen matches intent | Defaulted to opposite side from last trade |
| 3 | **Quantity** | Screen qty matches intent (integer exact match) | Platform used a default qty (e.g., 100) |
| 4 | **Order type** | Screen shows LIMIT/STOP/MARKET/etc. matching intent | Dropdown reverted to MARKET when intent was LIMIT |
| 5 | **Limit price** | Screen price within ±$0.01 of intent | Price field empty or shows stale value |
| 6 | **Stop price** | Screen stop price within ±$0.01 of intent (if stop order) | Stop field not visible for selected order type |
| 7 | **Time-in-force** | Screen TIF matches intent (DAY/GTC/etc.) | Platform defaulted to GTC when intent was DAY |
| 8 | **Account** | Screen shows the correct account (paper vs live, correct account number) | Switched to live when should be paper, or vice versa |
| 9 | **Bid/Ask sanity** | Spread is < 3× 20-day average for this instrument | Unusually wide spread indicates illiquidity or halt |
| 10 | **Cost estimate** | Estimated cost/margin is within agent's available cash/margin | Insufficient funds would cause immediate rejection |
| 11 | **No blocking popup** | No popup, warning dialog, or confirmation over the order area | 2FA, margin warning, PDT warning, platform error |
| 12 | **Platform connected** | Connection indicator shows "connected" / "live" | Disconnected state — orders will queue or fail |
| 13 | **Correct mode** | Platform is in trading mode, not replay/simulator (unless paper intended) | TradingView replay mode looks like live but isn't |
| 14 | **Time check** | Current time is within expected trading session for this order type | Placing a DAY order outside RTH will reject on some brokers |

## Example: passing verification

**Intent:** BUY 119 AAPL LIMIT $182.05 DAY on paper account

**Screen reads:**
- Symbol: AAPL ✓
- Side: BUY (green highlight) ✓
- Qty: 119 ✓
- Type: LIMIT ✓
- Price: $182.05 ✓
- Stop: n/a (limit order, no stop field) ✓
- TIF: DAY ✓
- Account: "Paper Trading" ✓
- Bid/Ask: $182.00 / $182.10 (spread $0.10, normal) ✓
- Est. cost: $21,663.95 ✓
- Popups: none ✓
- Connected: yes (green dot) ✓
- Mode: Paper Trading ✓
- Time: 10:30 AM ET, RTH ✓

**Result:** ALL PASS → proceed to ACT.

## Example: failing verification

**Intent:** SELL 50 KO LIMIT $70.00 GTC on live account

**Screen reads:**
- Symbol: **PEP** ← MISMATCH (expected KO, got PEP)
- Side: SELL ✓
- Qty: 50 ✓

**Result:** FAIL at check #1. ABORT immediately. Do not continue checking — one failure is enough.

**Action:** Emit Z-OVERRIDE, log: "Pre-click verification failed: symbol mismatch (intent=KO, screen=PEP). Aborted."

## Example: popup blocking

**Intent:** BUY 200 SPY LIMIT $450.00 DAY

**Screen reads:**
- All fields match... but a popup is overlaying the order ticket:
  "Pattern Day Trader Warning: This trade would be your 4th day trade in 5 business days..."

**Result:** FAIL at check #11. ABORT.

**Action:** Emit Z-OVERRIDE with `blocking_invariant: PDT`. Route to `regulations-and-tax-awareness`. Do NOT dismiss the popup — log its contents and escalate.

## Post-Click Validation Checklist

After submitting the order, re-screenshot and verify:

| # | Check | Pass condition |
|---|---|---|
| 1 | Order appears in Orders/Working tab | New entry matching intent visible |
| 2 | Order status | "Working" / "Open" / "Pending" (not "Rejected") |
| 3 | Order details match | Symbol, side, qty, type, price all correct |
| 4 | Fill status (market orders) | Fill price shown; slippage within expected range |
| 5 | No error messages | No rejection notice, no insufficient funds |
| 6 | Account balance updated | Cash/margin available reduced by expected amount |

If any post-click check fails → the order may not have been placed. Do NOT re-submit without re-running the full protocol. Log the anomaly and escalate to `safety-and-kill-switch`.

## Special cases

### Bracket orders
Verify all three legs (entry + stop + target) separately. Each leg's fields must match.

### Modification of existing order
Verify the order being modified is the correct one (match by order ID or position in the list). Read the modified fields before confirming.

### Cancellation
Verify the order being cancelled is the intended one. After cancellation, re-screenshot to confirm it disappeared from the working orders list.

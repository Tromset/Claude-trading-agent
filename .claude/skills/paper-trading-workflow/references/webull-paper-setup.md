# Webull Paper Trading Setup

## How to enable paper trading

1. Open Webull (desktop app or web at app.webull.com).
2. Look for the **account selector** in the upper-right area of the header bar.
3. Click the account dropdown — options include "Individual" (live) and "Paper Trading" (simulated).
4. Select **"Paper Trading."**
5. The interface switches to the paper account. A "Paper" or "Simulated" label appears in the header.
6. Starting balance is typically $1,000,000 (can be adjusted in settings).

## Visual identification of paper mode

- **"Paper" label** in the account selector or header bar.
- **Simulated balance** — usually $1,000,000 default (much larger than most live accounts).
- **Same UI layout** as live — chart, order panel, positions all in the same places.
- **Orange/teal color scheme** is the same in both modes — the only visual difference is the account label.

## Placing a paper trade

1. Search for a ticker using the search bar (top of screen).
2. The chart loads in the center.
3. On the **right side**, the order panel appears with:
   - Side toggle: Buy / Sell
   - Order type dropdown: Market / Limit / Stop / Stop-Limit
   - Quantity input
   - Price input (for limit/stop)
   - Time-in-force selector (Day / GTC / EXT)
4. Fill in the fields according to the trade plan.
5. Click **"Place Order"** (green for buy, red for sell).
6. A confirmation dialog may appear — verify all fields before confirming.

## Monitoring positions

- **Positions** tab at the bottom shows open positions: ticker, qty, avg cost, market value, P&L.
- **Orders** tab shows working (pending) orders.
- **History** tab shows completed trades.
- Real-time P&L updates based on live market data.

## Resetting the paper account

1. Go to Account Settings (gear icon or profile menu).
2. Look for "Paper Trading" section.
3. Select "Reset Paper Account."
4. Balance resets, all positions closed, history cleared.

## Limitations

- **Simulated fills** — same as TradingView: limits fill at limit price, no slippage on market orders.
- **No commissions** in paper mode.
- **Large default balance** ($1M) can create unrealistic sizing. Reset to match intended live account size.
- **Some features may differ** between paper and live (options approval levels, margin).

## Agent workflow on Webull paper

```
1. ORIENT: confirm "Paper" label in account selector.
2. Verify balance matches reset target (e.g., $50,000 to match planned live).
3. Search for intended ticker.
4. Perform analysis on the chart.
5. Run buy-sell-hold-decision → X/Y/Z.
6. If X or Y: fill order panel fields on right side.
7. Run full screenshot-vision-protocol.
8. Place the order.
9. Validate in Positions/Orders tabs.
10. Journal the trade.
```

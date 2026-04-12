# TradingView Paper Trading Setup

## How to enable paper trading

1. Open TradingView (web or desktop).
2. At the bottom of the screen, find the **Trading Panel** bar.
3. Click on it to expand. If collapsed, look for a thin bar with broker logos.
4. Select **"Paper Trading"** from the broker/account list (it's built-in, no account needed).
5. The panel expands showing: Account Summary, Orders, Positions, History.
6. A label "Paper Trading" appears in the panel header — this is how the agent confirms it's in paper mode.

## Visual identification of paper mode

- **Header label:** "Paper Trading" text in the trading panel header.
- **Balance:** shows a simulated balance (default $100,000 USD — can be reset).
- **Orders/Positions:** appear in the same bottom panel as live orders would.
- **No real broker connection** — no broker logo next to the account name.

## Placing a paper trade

1. **From the chart:** right-click on a price level → select "Create Buy Order" or "Create Sell Order."
2. **From the Trading Panel:** click "Buy" or "Sell" in the order entry area.
3. **Order dialog:** appears with fields:
   - Symbol (auto-filled from current chart)
   - Side (Buy/Sell)
   - Quantity (shares)
   - Order type (Market/Limit/Stop)
   - Price (for limit/stop)
   - Take Profit (optional)
   - Stop Loss (optional)
4. Click **"Place Order"** to submit.
5. The order appears in the **Orders** tab of the trading panel.

## Order types available in paper

- Market
- Limit
- Stop
- Stop-Limit (via "Stop" with a limit price)

Note: bracket orders (TP + SL attached to entry) are supported via the TP/SL fields in the order dialog.

## Monitoring positions

- **Positions tab:** shows open positions with entry price, qty, P&L (unrealized).
- **Orders tab:** shows working (unfilled) orders.
- **History tab:** shows filled and cancelled orders.
- P&L updates in real-time based on live market data.

## Resetting the paper account

1. In the Trading Panel, click the **gear icon** (settings) or look for "Reset" option.
2. Select "Reset Paper Trading Account."
3. Balance resets to default ($100,000 or custom amount if configured).
4. All positions and order history are cleared.

**When to reset:** at the start of a new strategy validation cycle, or after a promotion review.

## Limitations

- **Fills are simulated.** Limit orders fill at limit price immediately when price touches — unrealistic. Live limits may not fill even at the exact price.
- **No slippage.** Market orders fill at last price — no bid/ask spread impact.
- **No commissions.** Paper P&L does not deduct commissions.
- **No margin simulation.** Paper account has unlimited margin (may allow positions larger than live would).
- **Data is real-time.** Prices are live, so analysis is valid — only fills are simulated.

## Agent workflow on TradingView paper

```
1. ORIENT: identify "Paper Trading" label in trading panel header.
2. Verify balance matches expected starting amount.
3. Navigate to the chart for the intended instrument.
4. Perform full analysis (price action, patterns, indicators, S/R, volume).
5. Run buy-sell-hold-decision → X/Y/Z.
6. If X or Y: open the order dialog via right-click or trading panel.
7. Run full screenshot-vision-protocol 7-step process.
8. Place the order.
9. Validate in the Orders/Positions tab.
10. Journal the trade.
```

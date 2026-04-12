# Webull -- Visual Layout Reference

Desktop and web trading platform. Recognized by its dark theme with orange
and teal accent colors, prominent account summary bar, and clean modern UI.

## ASCII Mockup

```
+======================================================================+
| ACCOUNT BAR (full width, dark background, ~50px)                     |
| [W logo] [Account: xxxx1234 v]  Net Liq: $25,430  |  Day P&L: +$85 |
|          [Paper Trade | Live]   Buying Power: $12,200  |  +0.34%    |
+=============+========================================+===============+
|             |                                        |               |
| WATCHLIST   |           CHART AREA                   | ORDER PANEL   |
| (left col)  |                                        | (right col)   |
|             | +------------------------------------+ |               |
| [Search___] | | AAPL  174.25  +1.32 (+0.76%)       | | AAPL         |
|             | |                                    | |               |
| My List  v  | |  Candlestick chart                 | | [Buy] [Sell]  |
| ----------- | |  with indicators                   | |  (teal)(orange)|
| AAPL  174.2 | |                                    | |               |
| TSLA  245.1 | |  Price scale right -->    [174.25] | | Order Type:   |
| NVDA  875.3 | |                                    | | [Limit    v]  |
| AMD   178.4 | |  Time axis bottom                  | |               |
| MSFT  410.5 | |                                    | | Price:        |
| SPY   510.2 | +------------------------------------+ | [174.25    ]  |
|             | [1m][5m][15m][1H][1D][1W] Volume bars  | |               |
| ----------- |                                        | Shares:       |
| Gainers     | Tabs below chart:                      | [100       ]  |
| Losers      | [Summary][Financials][Analysis][News]   | |               |
| Most Active |                                        | TIF: [Day  v] |
|             |                                        |               |
|             |                                        | Est Cost:     |
|             |                                        | $17,425.00    |
|             |                                        |               |
|             |                                        | [Place Order] |
|             |                                        |  (teal btn)   |
+=============+========================================+===============+
| BOTTOM PANEL -- POSITIONS / ORDERS (full width)                      |
| [Positions] [Open Orders] [Filled] [Cancelled] [Performance]        |
| ------------------------------------------------------------------- |
| Symbol | Qty  | Avg Cost | Market Val | Unrealized P&L | Day P&L    |
| AAPL   | 100  | 172.90   | $17,425    | +$135.00       | +$85.00    |
| TSLA   |  25  | 242.00   | $6,127     | +$77.50        | +$12.25    |
+======================================================================+
```

## Account Bar -- Top Strip

- **Position**: Full width, topmost element. Approximately 50px tall, dark
  background (darker than the rest of the UI).
- **Visual cues**: Webull "W" logo at far left. Account selector dropdown
  showing a masked account number (e.g., "xxxx1234"). Net liquidation
  value, buying power, and daily P&L displayed prominently.
- **Paper Trade toggle**: A tab or dropdown within the account bar allows
  switching between "Live" and "Paper Trade" modes. Look for text "Paper
  Trade" or "Paper" as a clickable tab near the account selector.
- **How to identify**: The "W" logo is distinctive -- a stylized letter W
  in orange/white. The account bar shows dollar amounts and has the
  paper/live toggle.

## Paper Trading -- How to Toggle and Identify

- **Activation**: Click the account selector in the top bar. A dropdown
  shows "Live Trading" and "Paper Trading" (or "Simulator"). Select
  "Paper Trading." On some versions, a dedicated "Paper Trade" tab appears
  next to the account number.
- **Visual indicator when active**: The account bar may show "Paper" or
  "Simulated" label. The account balance resets to the simulated starting
  amount (often $1,000,000). Some versions show an orange banner or
  different background tint.
- **Key difference**: Paper mode uses simulated funds. The net liquidation
  and buying power numbers reflect the paper account, not real money.

## Watchlist -- Left Column

- **Position**: Left column, approximately 15-20% of screen width.
- **Visual cues**: Search box at the top. Below it, a dropdown or tab to
  select watchlist categories ("My List", "Gainers", "Losers", "Most
  Active", "52W High", etc.). Below that, a vertical list of ticker
  symbols with last price and daily change.
- **Color coding**: Teal/green text for positive change, orange/red for
  negative. Webull uses teal (not pure green) as its positive color.
- **How to identify**: Left-side vertical list of tickers. The search box
  at the top and category tabs are distinctive.

## Chart Area -- Center

- **Position**: Center, largest element. Bounded by watchlist (left), order
  panel (right), account bar (top), bottom panel (bottom).
- **Visual cues**: Standard candlestick chart. The current ticker and price
  are displayed in large text at the top-left of the chart area (e.g.,
  "AAPL 174.25 +1.32 (+0.76%)"). Timeframe buttons (1m, 5m, 15m, 1H, 1D,
  1W, 1M) appear either above or below the chart.
- **Below the chart**: Tabs for fundamental data: "Summary", "Financials",
  "Analysis", "News", "Options Chain." These are specific to Webull.
- **Webull-specific**: Chart may show an "Analysis" overlay with analyst
  ratings. Candle colors are teal (up) and orange/red (down).

## Order Panel -- Right Column

- **Position**: Right side, approximately 20-25% of screen width.
- **Visual cues**: Symbol name at top. Buy and Sell buttons side by side --
  Buy is TEAL, Sell is ORANGE (Webull's signature color scheme). Below the
  buttons: order type dropdown, price input, shares input, time-in-force
  dropdown, estimated cost.
- **Order types available**: Market, Limit, Stop, Stop Limit, Trailing Stop.
- **How to identify**: Teal Buy button and orange Sell button are the most
  distinctive Webull visual cue. The "Place Order" confirmation button at
  the bottom is typically teal.
- **Workflow**: Select Buy or Sell -> set order type -> enter price (for
  limit) -> enter quantity -> review estimated cost -> click "Place Order."

## Bottom Panel -- Positions and Orders

- **Position**: Full width, bottom of screen. Collapsible.
- **Visual cues**: Tab bar with labels "Positions", "Open Orders", "Filled",
  "Cancelled", "Performance." Below the tabs: data table with columns for
  symbol, quantity, average cost, market value, unrealized P&L, day P&L.
- **How to identify**: Horizontal tabs at the bottom containing portfolio
  data. The "Performance" tab (showing charts of account performance over
  time) is Webull-specific.
- **Color coding**: P&L values in teal (profit) or orange/red (loss).

## Visual Identification Checklist

- Dark theme with TEAL and ORANGE as primary accent colors: strong Webull
  signal. Most platforms use green/red, not teal/orange.
- Stylized "W" logo in the top-left corner.
- Buy button is teal, Sell button is orange (reversed from most platforms
  where Buy=green, Sell=red).
- Fundamental tabs below chart (Summary, Financials, Analysis).
- Paper/Live toggle near the account selector in the top bar.
- Clean, modern UI with rounded corners and consistent spacing.
- "Webull" text in the window title bar or footer.

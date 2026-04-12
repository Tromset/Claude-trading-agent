# Generic Trading Platform Region Map

Universal layout model for identifying the 5 standard regions on any trading
platform screenshot. Use this as the fallback when the specific platform is
not recognized.

## ASCII Mockup -- Canonical Layout

```
+======================================================================+
|  ACCOUNT BAR  (full width, thin strip)                               |
|  [Logo] [Account: $xxx,xxx]  [Buying Power: $xx,xxx]  [P&L: +$xxx]  |
+============+=========================================+===============+
|            |                                         |               |
| WATCHLIST  |              CHART AREA                 |  ORDER TICKET |
| (narrow    |  (largest element on screen)            |  (narrow col) |
|  column)   |                                         |               |
|            |  +-----------------------------------+  |  Symbol: AAPL |
| AAPL 174.2 |  |                                   |  |  Action: Buy  |
| MSFT 410.5 |  |   Price candles / line chart       |  |  Qty: [___]   |
| GOOG 155.8 |  |   with overlays & indicators       |  |  Type: Limit  |
| TSLA 245.1 |  |                                   |  |  Price: [___]  |
| AMZN 185.3 |  |   X-axis: time                     |  |  TIF: Day     |
| META 495.0 |  |   Y-axis: price scale (right)      |  |               |
|            |  +-----------------------------------+  |  [ BUY  ]     |
|            |  Volume bars along bottom of chart      |  [ SELL  ]     |
|            |                                         |               |
+============+=========================================+===============+
|  BOTTOM PANEL  (full width, moderate height)                         |
|  [Positions] [Open Orders] [Filled Orders] [Account History]        |
|  ------------------------------------------------------------------ |
|  Symbol | Qty | Avg Cost | Mkt Value | P&L      | P&L %             |
|  AAPL   | 100 | 170.50   | 17,420.00 | +$370.00 | +2.17%            |
|  MSFT   |  50 | 408.00   | 20,525.00 | +$125.00 | +0.61%            |
+======================================================================+
```

## Region 1 -- Account Bar (Top Strip)

- **Position**: Full width of the window, topmost element. Height typically
  20-50 pixels.
- **Visual cues**: Contains the broker logo (leftmost), account name or
  number, cash balance, buying power, daily P&L, and sometimes a mode
  indicator (Paper / Live / Simulated).
- **How to identify**: Look for a thin horizontal strip at the very top
  containing numeric dollar values and the broker brand. Usually darker or
  contrasting background from the rest of the interface.
- **Key data**: Account value, buying power, realized/unrealized P&L, margin
  status, paper-vs-live label.

## Region 2 -- Watchlist (Left Column)

- **Position**: Left side, vertically oriented list. Narrow column (roughly
  15-25% of screen width).
- **Visual cues**: A scrollable column of ticker symbols with associated
  prices and percentage changes. Rows are often alternating shades. Green
  text = up, red text = down.
- **How to identify**: Look for a vertical list of 3-5 character uppercase
  strings (ticker symbols) each followed by decimal numbers. Often has a
  search box at the top of the column.
- **Key data**: Symbol names, last price, change amount, change percent,
  bid/ask (on some platforms).
- **Variation**: Some platforms put the watchlist on the right side or as a
  floating panel. If no left column is visible, check the right sidebar or
  look for a tab labeled "Watchlist."

## Region 3 -- Chart Area (Center, Largest)

- **Position**: Center of the screen. Almost always the single largest
  visual element, consuming 40-60% of screen area.
- **Visual cues**: Candlestick or line chart with a time axis (bottom) and
  price axis (right or left). Background is usually solid dark or light
  color with a grid. Colored candles (green/white = up, red/black = down).
  Volume bars sometimes appear as a sub-panel below the candles.
- **How to identify**: The chart is the largest rectangular region. It
  contains non-text graphical elements (candles, lines, shaded areas). A
  toolbar above it shows timeframe buttons (1m, 5m, 15m, 1H, 1D, 1W) and
  indicator names.
- **Key data**: Current price (often a horizontal line or label at the right
  edge), OHLC of hovered candle, indicator overlays (moving averages,
  Bollinger bands), drawing annotations.
- **Tip**: If you are unsure which region is the chart, it is the one with
  the horizontal time axis and vertical price axis. No other region has
  both axes.

## Region 4 -- Order Ticket (Right Column or Popup)

- **Position**: Right side column, or a popup/modal that appears after
  clicking a trade button. Narrow (15-25% width) when docked.
- **Visual cues**: Contains INPUT FIELDS (text boxes for quantity, price),
  dropdown menus (order type, TIF), and prominently colored action buttons
  (green "Buy", red "Sell"). Radio buttons or tabs to toggle Buy/Sell.
- **How to identify**: Look for the colored Buy/Sell buttons. These are
  almost always green and red respectively, and are the most visually
  prominent buttons on the entire screen. Also look for labeled input
  fields: "Qty", "Quantity", "Price", "Limit Price", "Stop Price".
- **Key data**: Symbol, side (buy/sell), quantity, order type (market, limit,
  stop, stop-limit), limit price, stop price, time-in-force (DAY, GTC,
  IOC), estimated cost.
- **Variation**: On mobile or minimalist platforms, the order ticket is a
  full-screen overlay triggered by tapping "Trade."

## Region 5 -- Bottom Panel (Positions, Orders, History)

- **Position**: Full width, bottom of the screen. Height roughly 15-30% of
  screen.
- **Visual cues**: Tabbed interface with tabs like "Positions," "Orders,"
  "Trades," "History," "Account." Below the tabs: a data table with columns
  (Symbol, Qty, Price, P&L, etc.).
- **How to identify**: Look for a horizontal tab bar near the bottom of the
  screen. Below it will be a structured data table with rows of trades or
  positions. Column headers are visible.
- **Key data**: Open positions with unrealized P&L, pending/working orders,
  filled order history, account activity.
- **Tip**: If the bottom panel is collapsed or hidden, look for a thin
  strip or drag handle at the very bottom of the screen. Some platforms
  show only a single row or a small tab bar until expanded.

## Cross-Platform Identification Tips

1. **Chart is king** -- always the largest element. Start by finding it.
2. **Buy/Sell buttons** -- most visually distinct elements. Green and red,
   large, high contrast. Finding them locates the order ticket.
3. **Ticker lists** -- vertical columns of uppercase symbols with numbers.
   Finding one locates the watchlist.
4. **Data tables** -- horizontal rows of structured financial data at the
   bottom locates the positions/orders panel.
5. **Dollar signs and percentages** -- concentrated in the account bar and
   bottom panel. The account bar is at the top; the bottom panel is at the
   bottom.
6. **Dark vs light theme** -- does not change region positions. Layout is
   consistent regardless of color theme.
7. **Collapsed regions** -- a region may be minimized. Look for thin bars,
   arrows, or tab labels at expected positions.

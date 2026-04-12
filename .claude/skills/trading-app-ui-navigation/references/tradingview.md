# TradingView -- Visual Layout Reference

Web-based charting platform at tradingview.com. Used for analysis and paper
trading. Recognized by its dark-themed interface, prominent top toolbar, and
left-side drawing tool sidebar.

## ASCII Mockup

```
+======================================================================+
| TOP TOOLBAR (full width, ~40px tall)                                 |
| [AAPL v] [1H v] [Candle v] [Compare+] [fx Indicators] [>> Replay]  |
| [Template] [Alert] [Undo] [Redo]  ...  [Settings] [Fullscreen]      |
+=+====================================================+==============+
|D|                                                    | RIGHT SIDEBAR|
|R|                MAIN CHART AREA                     | [Watchlist]   |
|A|                                                    | [Alerts]      |
|W|  +----------------------------------------------+ | [Data Window] |
|I|  | MA(20) 173.45  MA(50) 170.12  RSI(14) 58.3   | | [DOM]         |
|N|  |                                               | | [News]        |
|G|  |   Candlestick chart with overlays             | |              |
| |  |                                               | | When DOM open:|
|T|  |   Price scale on right edge -------> [174.25] | | Ask  |  Size |
|O|  |                                               | | 174.5|   120 |
|O|  |                                               | | 174.4|   340 |
|L|  |   Crosshair tracks mouse position             | | 174.3|   250 |
|S|  |                                               | |---[174.25]---|
| |  |   Time axis along bottom                      | | 174.2|   180 |
|~|  +----------------------------------------------+ | 174.1|   410 |
|30|  [Volume bars]                                   | Bid  |  Size |
|px|                                                   |              |
+=+====================================================+==============+
| BOTTOM PANEL (collapsible, full width)                               |
| [Stock Screener] [Pine Editor] [Strategy Tester] [Trading Panel]     |
| -----------------------------------------------------------------   |
| Trading Panel content (when "Paper Trading" selected):               |
|  Symbol | Side | Qty | Entry | P&L     | Close                      |
|  AAPL   | Long | 10  | 172.5 | +$17.50 | [X]                        |
|  Overview: Net Liq $100,000.00 | Open P&L +$17.50                   |
+======================================================================+
```

## Top Toolbar -- Identification and Contents

- **Position**: Topmost bar, full width, approximately 40 pixels tall.
- **Visual cues**: Row of small dropdown buttons and icon buttons. The
  leftmost element is the symbol search box showing the current ticker
  (e.g., "AAPL" or "NASDAQ:AAPL") with a small down-arrow.
- **Key elements left to right**:
  - Symbol search (dropdown, shows current ticker)
  - Timeframe selector (e.g., "1H", "D", "W" -- small dropdown)
  - Chart type selector (candle icon with dropdown)
  - Compare button ("+")
  - Indicators button (labeled "fx" or "Indicators")
  - Replay button (labeled with a play-like icon or "Replay")
  - Template, Alert, Undo/Redo icons further right
  - Settings gear and fullscreen icon at far right
- **How to identify**: Dense row of small controls at the top. The symbol
  box is the most recognizable -- bold text of a ticker symbol.

## Left Sidebar -- Drawing Tools

- **Position**: Narrow vertical strip (approximately 30-40px wide) along the
  left edge, below the top toolbar.
- **Visual cues**: Column of small square icon buttons. Icons represent
  drawing tools: trend lines, horizontal lines, Fibonacci, text, shapes,
  measurement tools. A magnifying glass icon for zoom controls at bottom.
- **How to identify**: Very narrow column of monochrome icons stacked
  vertically. No text labels -- icons only.

## Main Chart Area -- Center

- **Position**: Center, largest element. Bounded by drawing tools (left),
  right sidebar, top toolbar, and bottom panel.
- **Visual cues**: Standard candlestick/bar/line chart. Indicator labels
  appear in the upper-left corner of the chart (e.g., "MA(20) 173.45").
  Price scale on the right edge shows current price highlighted in a
  colored label. Time axis at bottom.
- **TradingView-specific**: Watermark "TradingView" in light gray in the
  center of the chart background (free accounts). Chart background defaults
  to dark navy/black.

## Right Sidebar -- Watchlist, DOM, Data

- **Position**: Right edge, vertical column. Toggleable via icons at the
  right edge of the screen. Width approximately 200-300px when open.
- **Visual cues**: Stacked panels toggled by tab icons on the right edge.
  Each panel has a small icon: list icon (watchlist), bell (alerts), "i"
  (data window), ladder icon (DOM), newspaper (news).
- **Watchlist panel**: Vertical list of tickers with last price and change%.
- **DOM (Depth of Market)**: Price ladder showing bid/ask quantities at each
  price level. The current price sits in the middle, highlighted. Buy and
  sell buttons appear at the top of the DOM.
- **Order placement via DOM**: Click on a price level in the DOM to place a
  limit order. The buy/sell buttons at the top of the DOM panel are the
  primary order entry for paper trading.

## Bottom Panel -- Screener, Pine Editor, Trading

- **Position**: Bottom of screen, full width. Collapsed by default into a
  thin tab bar (~25px). Expands upward when a tab is clicked.
- **Tab labels**: "Stock Screener", "Pine Editor", "Strategy Tester",
  "Trading Panel". Tabs appear as text labels in the thin bar.
- **Trading Panel**: This is where paper trading is accessed.
  1. Click the "Trading Panel" tab at the bottom.
  2. A broker/paper selection dropdown appears. Select "Paper Trading."
  3. The panel shows: simulated positions, open orders, order history,
     and a net liquidation value (default $100,000).
  4. To place a trade: use the DOM in the right sidebar or right-click
     the chart and select "Trade" from the context menu.

## Paper Trading vs Live -- Visual Distinction

- **Paper mode indicator**: When Paper Trading is active, the Trading Panel
  tab at the bottom shows "Paper Trading" in its header. The simulated
  account balance (default $100,000) is visible.
- **No real broker connected**: If no broker is connected, only "Paper
  Trading" appears as an option in the Trading Panel.
- **Live broker**: If a broker (e.g., TradeStation, Interactive Brokers) is
  connected, it appears as a separate option in the Trading Panel dropdown.
  The broker name and real account number are shown.
- **Key visual difference**: Paper Trading uses a generic TradingView icon
  and the label "Paper Trading." Live accounts show the broker logo and
  real account identifiers.

## Order Entry Workflow

1. Open the DOM panel in the right sidebar (click the ladder icon).
2. At the top of the DOM: Buy and Sell buttons (blue/green for buy,
   red/pink for sell).
3. Select order type from a dropdown (Market, Limit, Stop, Stop Limit).
4. Enter quantity in the Qty field.
5. For limit orders: click a price level in the DOM ladder, or type a price.
6. Click Buy or Sell to submit.
7. Alternatively: right-click on the chart -> "Trade" -> submenu with
   Buy/Sell options pre-filled at the clicked price level.

## Visual Identification Checklist

- Dark navy background with green/red candles: likely TradingView.
- Left sidebar of small square drawing-tool icons: confirms TradingView.
- "fx" or "Indicators" button in top toolbar: confirms TradingView.
- Watermark text "TradingView" on the chart (free tier).
- Bottom tab bar with "Pine Editor": unique to TradingView.
- Symbol search box at top-left with exchange prefix (e.g., "NASDAQ:AAPL").

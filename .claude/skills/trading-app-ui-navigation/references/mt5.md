# MetaTrader 5 (MT5) -- Visual Layout Reference

Classic desktop trading platform for forex, futures, and CFDs. Recognized by
its Windows-native application style, multi-chart tiled layout, Market Watch
panel on the left, and Terminal panel at the bottom. Published by MetaQuotes.

## ASCII Mockup

```
+======================================================================+
| MENU BAR (standard Windows menu)                                     |
| [File] [View] [Insert] [Charts] [Tools] [Window] [Help]             |
+======================================================================+
| TOOLBAR ROW 1 (icon buttons, full width)                             |
| [New Order] [M1][M5][M15][M30][H1][H4][D1][W1][MN] [Zoom+][Zoom-]  |
| [Crosshair] [Line] [Fibo] [Text] [Shapes]  ... [AutoTrading on/off] |
+======================================================================+
| TOOLBAR ROW 2 (optional, chart templates, profiles)                  |
| [Default] [Template1] [Template2] ...                                |
+=============+====================================+===================+
|             |                                    |                   |
| MARKET      |        CHART WINDOW(S)             |  (Charts can be  |
| WATCH       |                                    |   tiled or        |
| (left panel)|  +------------------------------+  |   cascaded)      |
|             |  | EURUSD, H1                    |  |                   |
| Symbol  Bid |  | [One-Click Trading btn]       |  |                   |
| ------  ----|  |  SELL        BUY              |  |                   |
| EURUSD 1.085|  |  1.0850    1.0852             |  |                   |
| GBPUSD 1.262|  |                               |  |                   |
| USDJPY 151.4|  |  Candlestick chart            |  |                   |
| XAUUSD 2341 |  |  with indicators              |  |                   |
| US500  5102 |  |                               |  |                   |
|             |  |  Price scale right             |  |                   |
| [Tick Chart]|  |  Time axis bottom              |  |                   |
| [Depth]     |  |                               |  |                   |
|             |  +------------------------------+  |                   |
|=============|                                    |                   |
| NAVIGATOR   |  +------------------------------+  |                   |
| (left below)|  | GBPUSD, M15                   |  |                   |
|             |  | (second chart, tiled below)    |  |                   |
| [+]Accounts |  |                               |  |                   |
| [+]Indicators| +------------------------------+  |                   |
| [+]Expert   |                                    |                   |
|   Advisors  |                                    |                   |
| [+]Scripts  |                                    |                   |
|             |                                    |                   |
+=============+====================================+===================+
| TERMINAL (bottom panel, full width, tabbed)                          |
| [Trade] [Exposure] [History] [News] [Mailbox] [Alerts] [CodeBase]   |
| [Journal]                                                            |
| ------------------------------------------------------------------- |
| Trade tab content:                                                   |
| Order  | Time       | Type | Size | Symbol | Price  | S/L    | T/P  |
| #12345 | 2026.04.12 | Buy  | 0.10 | EURUSD | 1.0840 | 1.0800 | 1.09 |
| #12346 | 2026.04.12 | Sell | 0.05 | GBPUSD | 1.2630 | 1.2670 | 1.25 |
| ---                                                                  |
| Balance: 10000.00 | Equity: 10045.30 | Margin: 108.40 | Free: 9936  |
+======================================================================+
```

## Menu Bar and Toolbars

- **Position**: Top of window. Standard Windows-style menu bar (File, View,
  Insert, Charts, Tools, Window, Help) followed by one or two rows of icon
  toolbars.
- **Toolbar row 1**: Contains the "New Order" button (often a green/blue
  icon with a plus sign), timeframe buttons (M1, M5, M15, M30, H1, H4,
  D1, W1, MN), zoom controls, crosshair, drawing tools, and the
  AutoTrading toggle button.
- **AutoTrading button**: Shows a green play icon when enabled, red stop
  icon when disabled. This controls whether Expert Advisors (EAs) can
  execute trades.
- **How to identify**: Windows-native menu bar plus dense icon toolbars.
  The timeframe buttons (M1, M5, etc.) as a row of small labeled buttons
  are distinctive to MetaTrader.

## Market Watch -- Left Panel (Upper)

- **Position**: Left side of the screen, upper portion. Default width
  approximately 200px.
- **Visual cues**: A table with columns: Symbol, Bid, Ask (and optionally
  Spread, High, Low). Each row is a tradable instrument. Forex pairs
  shown as 6-character codes (EURUSD, GBPUSD). Prices update in
  real-time with brief color flashes (blue for up-tick, red for down-tick).
- **Context menu**: Right-click a symbol to access "Chart Window" (open
  chart), "New Order" (place trade), "Depth of Market", "Specification."
- **Tabs at bottom of Market Watch**: "Symbols" (the list), "Tick Chart"
  (real-time tick chart of selected symbol), "Depth" (order book depth).
- **How to identify**: Left-side panel with forex pair codes and bid/ask
  prices in a tight table. The 6-character pair format (EURUSD not EUR/USD)
  is MetaTrader convention.

## Navigator -- Left Panel (Lower)

- **Position**: Left side, below Market Watch. Collapsible tree view.
- **Visual cues**: Tree structure with expandable folders: Accounts (shows
  connected trading accounts), Indicators (built-in and custom technical
  indicators), Expert Advisors (automated trading programs), Scripts
  (one-time execution scripts).
- **How to identify**: Tree view with folder icons. "Expert Advisors" folder
  is unique to MetaTrader.
- **Usage**: Drag an indicator from the Navigator onto a chart to apply it.
  Drag an EA onto a chart to attach it for automated trading.

## Chart Window(s) -- Center

- **Position**: Center area, fills remaining space between left panels and
  right edge, between toolbars and Terminal.
- **Visual cues**: One or more chart windows, which can be tiled (horizontal
  or vertical split), cascaded, or tabbed. Each chart has a title bar
  showing "SYMBOL, Timeframe" (e.g., "EURUSD, H1"). Standard candlestick/
  bar/line chart with price scale on the right and time axis on the bottom.
- **One-Click Trading button**: A small panel in the upper-left corner of
  each chart showing SELL price, BUY price, and a volume/lot size field.
  Click SELL or BUY for instant market order execution. This panel is
  toggled via Alt+T or right-click menu.
- **How to identify**: Charts have Windows-style title bars with minimize/
  maximize/close buttons. Multiple charts visible simultaneously is common.
  The title format "SYMBOL, Timeframe" is distinctive.

## One-Click Trading Panel (on chart)

- **Position**: Upper-left corner of the chart window, small floating panel.
- **Visual cues**: Two price buttons side by side: SELL (left, typically
  red/pink background) and BUY (right, typically blue background). Between
  or below them, a lot size input field.
- **How to identify**: Small overlay on the chart with colored price buttons.
  Shows real-time bid/ask prices.
- **CAUTION**: One-click trading executes IMMEDIATELY with no confirmation
  dialog. The agent must verify lot size before clicking.

## Order Dialog (New Order Window)

- **Access**: Click "New Order" in toolbar, press F9, or right-click chart
  and select "Trading" -> "New Order."
- **Visual layout**: Modal dialog with fields: Symbol, Type (Market
  Execution, Pending Order), Volume (lot size), Stop Loss, Take Profit,
  and a Comment field. For pending orders: additional fields for Price and
  Expiration.
- **Buttons**: "Sell by Market" (red) and "Buy by Market" (blue) at the
  bottom. For pending orders: "Place" button.
- **Order types available**: Market, Buy Limit, Sell Limit, Buy Stop, Sell
  Stop, Buy Stop Limit, Sell Stop Limit.
- **How to identify**: Standalone dialog box with "Symbol" and "Volume"
  fields and two colored market execution buttons at the bottom.

## Terminal -- Bottom Panel

- **Position**: Full width, bottom of the screen. Tabbed interface.
- **Tabs**: Trade, Exposure, History, News, Mailbox, Alerts, CodeBase,
  Journal.
- **Trade tab**: Shows open positions and pending orders in a table.
  Columns: Order number, Time, Type (Buy/Sell), Size (lots), Symbol,
  Price, S/L (stop loss), T/P (take profit), Profit. Below the table:
  Balance, Equity, Margin, Free Margin, Margin Level %.
- **History tab**: Closed trades and deposit/withdrawal history.
- **Journal tab**: Platform log messages (useful for debugging EAs).
- **How to identify**: Bottom panel with "Trade | Exposure | History" tabs.
  The "Exposure" and "CodeBase" tabs are unique to MetaTrader.

## Visual Identification Checklist

- Windows-native application look (standard Windows title bar, menu bar,
  toolbar icons) -- not a modern web-based UI.
- Timeframe buttons as M1, M5, M15, M30, H1, H4, D1, W1, MN in the
  toolbar -- unique notation to MetaTrader.
- Market Watch panel with 6-character forex pair codes (EURUSD not EUR/USD).
- Navigator panel with "Expert Advisors" tree node.
- Multiple chart windows tiled within the application frame (MDI style).
- Terminal panel at bottom with "Trade | Exposure | History" tabs.
- One-click trading overlay on chart with SELL/BUY price buttons.
- "MetaTrader 5" or "MT5" in the window title bar.
- Lot-based sizing (0.01, 0.10, 1.00) rather than share quantities.
- Balance/Equity/Margin/Free Margin line at the bottom of the Trade tab.

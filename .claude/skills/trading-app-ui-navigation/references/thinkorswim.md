# Thinkorswim (Schwab) -- Visual Layout Reference

Professional desktop trading platform. Recognized by its dense, information-
heavy interface, dark background, multiple workspace tabs, and "paperMoney"
mode for simulated trading. Formerly TD Ameritrade, now Charles Schwab.

## ASCII Mockup -- Trade Tab Active

```
+======================================================================+
| TITLE BAR                                                            |
| thinkorswim - [paperMoney] OR [Live Trading] - XXXXX1234            |
+======================================================================+
| MAIN TAB BAR (full width, ~35px)                                     |
| [Monitor] [Trade] [Analyze] [Scan] [MarketWatch] [Charts] [Tools]   |
|           ^^^^^^^^ (selected tab highlighted)                        |
+======================================================================+
| SYMBOL BOX + TOOLBAR                                                 |
| [AAPL____] [Last: 174.25] [Chg: +1.32] [Bid: 174.20] [Ask: 174.30] |
+==================+===================================================+
|                  |                                                   |
| LEFT SIDEBAR     |   TRADE TAB -- ORDER ENTRY                       |
| (collapsible)    |                                                   |
|                  |   All Products | Forex | Futures | Futures Options |
| Gadgets:         |   ------------------------------------------------|
| [+] MarketWatch  |   Symbol: AAPL     Last: 174.25                   |
| [+] Quick Chart  |                                                   |
| [+] Live News    |   Stock/ETF    Options Chains (below)             |
| [+] Scratch Pad  |   -----------------------------------------      |
| [+] Calculator   |   Side:  [Buy v]  [Sell v]  [Buy to Cover]       |
|                  |   Qty:   [100    ]                                |
|                  |   Order: [LIMIT  v]                               |
|                  |   Price: [174.25  ]                               |
|                  |   TIF:   [DAY    v]  (DAY/GTC/EXT/GTC-EXT)       |
|                  |   Route: [Best   v]                               |
|                  |                                                   |
|                  |   [Confirm and Send]   Est. Cost: $17,425.00      |
|                  |                                                   |
|                  |   OPTIONS CHAIN (lower portion of Trade tab):     |
|                  |   Expiration: [Apr 19 v]  Strikes: [All v]        |
|                  |   Call Bid|Call Ask|Strike|Put Bid|Put Ask         |
|                  |   3.50    |3.55    | 175  | 4.20  | 4.25          |
|                  |   2.80    |2.85    | 177.5| 5.10  | 5.15          |
|                  |   2.15    |2.20    | 180  | 6.00  | 6.10          |
+==================+===================================================+
| STATUS BAR (bottom strip, ~20px)                                     |
| Connected | Server: OK | Quotes: Real-time | CPU: 12% | Mem: 2.1GB  |
+======================================================================+
```

## ASCII Mockup -- Monitor Tab

```
+======================================================================+
| [Monitor] [Trade] [Analyze] [Scan] [MarketWatch] [Charts] [Tools]   |
|  ^^^^^^^^ (selected)                                                 |
+======================================================================+
| MONITOR TAB CONTENT                                                  |
| Sub-tabs: [Activity and Positions] [Account Statement] [Risk Profile]|
|                                                                      |
| Account Summary:                                                     |
| Net Liq: $102,345.67 | Cash: $45,123 | BP: $90,247 | P&L: +$1,234  |
|                                                                      |
| Position Statement:                                                  |
| -------------------------------------------------------------------  |
| Instrument   | Qty  | Trade Price | Mark  | P/L Open  | P/L Day    |
| -------------------------------------------------------------------  |
| AAPL         | +100 | 172.90      |174.25 | +$135.00  | +$85.00    |
|   > Apr175C  |  -2  |   3.20      |  3.50 |  -$60.00  | -$20.00    |
| MSFT         |  +50 | 408.00      |410.50 | +$125.00  | +$62.50    |
| -------------------------------------------------------------------  |
| Working Orders:                                                      |
| AAPL LMT Buy 50 @ 172.00 DAY                        [Cancel][Edit]  |
+======================================================================+
```

## ASCII Mockup -- Active Trader (Price Ladder)

```
+==========================================+
| ACTIVE TRADER -- AAPL                    |
| [Settings] [Flatten] [Rev] [Cancel All]  |
|                                          |
| Buy Qty |  Price  | Sell Qty | Volume    |
|         | 175.00  |     200  | 1,234     |
|         | 174.90  |     150  |   890     |
|         | 174.80  |     320  |   567     |
|         | 174.70  |      80  |   234     |
|         | 174.60  |     110  |   456     |
|    ====>| 174.50  |<====     |   789     |
|         | 174.40  |          |   345     |  <- Bid/Ask spread
|    ====>| 174.30  |<====     |   678     |
|     100 | 174.20  |          |   901     |
|     250 | 174.10  |          |   432     |
|     180 | 174.00  |          |   765     |
|     300 | 173.90  |          |   543     |
|                                          |
| Position: +100 | Avg: 172.90 | P&L: +135|
| [Buy Market] [Sell Market] Qty: [100]    |
+==========================================+
```

## Main Tab Bar -- Primary Navigation

- **Position**: Full width, directly below the title bar. Approximately
  35px tall.
- **Tabs**: Monitor, Trade, Analyze, Scan, MarketWatch, Charts, Tools.
  Each tab reveals an entirely different workspace. The selected tab is
  highlighted (lighter background or underlined).
- **How to identify**: This tab bar is the defining feature of thinkorswim.
  No other platform has this exact set of named tabs. Finding "Monitor",
  "Trade", "Analyze" in a horizontal tab bar confirms thinkorswim.

## Title Bar -- Paper vs Live Identification

- **Position**: Very top of the window.
- **paperMoney mode**: Title bar shows "thinkorswim - paperMoney" or
  "[paperMoney]" prominently. The background may have a slightly different
  tint (some versions use a green-tinted title bar for paper).
- **Live mode**: Title bar shows "thinkorswim" with the real account number.
  No "paperMoney" label.
- **Separate login**: paperMoney uses a different login credential set.
  Users log in specifically to "paperMoney" from the login screen.
- **Key visual check**: ALWAYS read the title bar first. If "paperMoney"
  appears, the agent is in simulated mode. If it does not, the agent is
  controlling real money.

## Monitor Tab

- **Purpose**: View positions, account balances, order status, P&L.
- **Sub-tabs**: "Activity and Positions" (default), "Account Statement",
  "Risk Profile."
- **Account Summary row**: Net liquidation, cash balance, buying power,
  open P&L, day P&L -- all in a single dense row at the top.
- **Position Statement**: Table with columns: Instrument, Qty (positive =
  long, negative = short), Trade Price, Mark (current), P/L Open, P/L Day.
  Grouped by underlying (stock positions and related option positions
  nested under the same ticker).
- **Working Orders section**: Below positions, shows all open/pending orders
  with Cancel and Edit buttons.

## Trade Tab -- Order Entry

- **Sub-tabs**: "All Products", "Forex", "Futures", "Futures Options."
- **Order entry fields**: Side (Buy/Sell/Buy to Cover/Sell Short), Qty,
  Order Type (Market, Limit, Stop, Stop Limit, Trailing Stop, Market on
  Close, Limit on Close), Price, TIF (DAY, GTC, EXT, GTC+EXT), Route.
- **Confirm and Send**: Button that opens a confirmation dialog before
  submitting. The dialog shows full order details and estimated cost.
- **Options Chain**: Lower portion shows the full options chain for the
  selected symbol. Expiration date selector, strike price list with
  bid/ask for calls and puts.
- **How to identify**: Dense form with many dropdowns and input fields.
  The "Confirm and Send" button is the submit trigger.

## Active Trader (Price Ladder)

- **Access**: From the Trade tab, click "Active Trader" sub-tab, or open
  from the Charts tab.
- **Visual layout**: Vertical price ladder. Current price in the center.
  Buy quantities on the left, sell quantities on the right. Volume at each
  price level on the far right.
- **One-click trading**: Click a price level on the buy side to place a buy
  limit order, or on the sell side to place a sell limit order.
- **Controls at top**: Flatten (close all positions), Reverse (flip long to
  short or vice versa), Cancel All (cancel all working orders).
- **Position info at bottom**: Current position size, average price, P&L.
  Market buy/sell buttons for immediate execution.

## Charts Tab

- **Separate from the Trade tab chart**: The Charts tab provides full-screen
  charting with extensive customization.
- **Features**: Multiple chart panes, hundreds of built-in indicators
  ("Studies" in thinkorswim terminology), drawing tools, custom
  thinkScript studies.
- **Visual cue**: Charts fill the entire workspace area. Study labels appear
  in the upper-left of each chart pane.

## Visual Identification Checklist

- Dark background (charcoal/black) as default theme.
- Tab bar with "Monitor | Trade | Analyze | Scan | MarketWatch | Charts"
  -- unique to thinkorswim.
- Dense, information-heavy interface with small fonts and many panels.
- "paperMoney" in the title bar (if simulated mode).
- "thinkorswim" text in the title bar or splash screen.
- Options chains integrated directly in the Trade tab.
- Active Trader price ladder with one-click trading.
- Status bar at bottom showing connection status, CPU, memory usage.
- Schwab or TD Ameritrade branding (varies by version).

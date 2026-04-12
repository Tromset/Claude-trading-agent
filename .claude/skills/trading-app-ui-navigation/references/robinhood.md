# Robinhood -- Visual Layout Reference

Web and mobile trading platform. Recognized by its minimalist design, bright
green brand color, large chart with minimal chrome, and simplified trade flow.
No traditional order ticket panel -- trades go through a multi-step modal.

## ASCII Mockup -- Web Interface

```
+======================================================================+
| TOP NAV BAR (full width, white/light background, ~50px)              |
| [Robinhood feather logo]  [Search____________]    [$] [Bell] [User] |
+======================================================================+
|                                                                      |
|  LEFT CONTENT (main scrollable area, ~70% width)                     |
|                                                                      |
|  AAPL - Apple Inc.                                                   |
|  $174.25                                                             |
|  +$1.32 (+0.76%) Today                                               |
|                                                                      |
|  +----------------------------------------------------------+       |
|  |                                                          |       |
|  |              CHART AREA                                  |       |
|  |   Large, clean line chart (default) or candle chart      |       |
|  |   Minimal gridlines                                      |       |
|  |   Green line if stock is up, red if down                 |       |
|  |                                                          |       |
|  |   No visible Y-axis labels by default                    |       |
|  |   Hover to see price tooltip                             |       |
|  +----------------------------------------------------------+       |
|  [1D] [1W] [1M] [3M] [YTD] [1Y] [5Y]  (timeframe buttons)          |
|                                                                      |
|  +-----------------------+                                           |
|  | [Trade AAPL]  (green) |  <-- Primary action button                |
|  +-----------------------+                                           |
|                                                                      |
|  Key Statistics              | RIGHT SIDEBAR (~30%)                  |
|  Open: 173.10                | +----------------------------------+  |
|  High: 175.02                | | WATCHLIST                        |  |
|  Low: 172.80                 | |                                  |  |
|  Vol: 45.2M                  | | AAPL     $174.25    +0.76%       |  |
|  Mkt Cap: 2.7T               | | MSFT     $410.50    +0.31%       |  |
|                              | | TSLA     $245.10    -1.20%       |  |
|  About Apple Inc.            | | GOOG     $155.80    +0.45%       |  |
|  [Company description...]    | | AMZN     $185.30    +0.92%       |  |
|                              | |                                  |  |
|  Analyst Ratings             | | LISTS                            |  |
|  [Buy/Hold/Sell bar]         | | [My First List]                  |  |
|                              | | [Tech Stocks]                    |  |
|  News                        | | [Recently Viewed]                |  |
|  [News headlines...]         | +----------------------------------+  |
|                                                                      |
+======================================================================+
```

## ASCII Mockup -- Trade Modal (appears after clicking "Trade")

```
+================================+
|          Trade AAPL             |
|================================|
|                                |
|   [Buy]    [Sell]              |
|   (selected tab is green)      |
|                                |
|   Order Type: [Market    v]    |
|                                |
|   Shares:    [________]        |
|    or                          |
|   Dollars:   [$_______]        |
|                                |
|   Market Price: $174.25        |
|   Estimated Cost: $---         |
|                                |
|   [Review Order]  (green btn)  |
|                                |
+================================+
        |
        v  (after clicking Review)
+================================+
|      Review Your Order          |
|================================|
|                                |
|   Buy AAPL                     |
|   Market Order                 |
|   10 Shares                    |
|   Est. Price: $174.25          |
|   Est. Total: $1,742.50        |
|                                |
|   [Submit Order] (green btn)   |
|   [Edit]                       |
|                                |
+================================+
```

## Top Navigation Bar

- **Position**: Full width, topmost. White or very light background.
- **Visual cues**: Robinhood feather logo (a single feather silhouette) at
  the far left in green. A search bar in the center or left-center. At the
  right: dollar/portfolio icon, notifications bell, user account icon.
- **How to identify**: The green feather logo is unmistakable. The nav bar
  is clean white with very few elements -- minimalism is the hallmark.
- **No account bar in the traditional sense**: Portfolio value appears on
  the home/dashboard page as a large number, not in a persistent bar.

## Chart Area -- Center/Left

- **Position**: Center-left of the page, taking approximately 70% width.
  Very large relative to other elements.
- **Visual cues**: Default view is a LINE CHART (not candles). The line is
  solid green if the stock is up for the selected period, solid red if
  down. Minimal gridlines. No visible Y-axis price labels by default --
  price only appears on hover as a tooltip.
- **Timeframe buttons**: Below the chart, a row of period buttons: 1D, 1W,
  1M, 3M, YTD, 1Y, 5Y. These are small text buttons. The selected one is
  underlined or highlighted in green.
- **Above the chart**: Ticker name, company name, current price in large
  bold text, and the daily change in dollars and percent.
- **Robinhood-specific**: The chart is exceptionally clean. No indicator
  overlays by default. No drawing tools. Candle view is available but not
  the default.

## Trade Button and Order Flow

- **Position**: Below the chart, a prominent green button labeled
  "Trade AAPL" (or similar text with the ticker).
- **Visual cues**: Large green button, high contrast. This is the primary
  call to action on the stock detail page.
- **Order flow** (multi-step modal):
  1. Click "Trade AAPL" -- a modal/slide-over panel opens.
  2. Select Buy or Sell tab at the top of the modal.
  3. Choose order type from a dropdown: Market, Limit, Stop Loss, Stop
     Limit (note: order type availability may vary by instrument).
  4. Enter quantity as shares OR dollar amount.
  5. Click "Review Order" -- a confirmation screen appears.
  6. Review: shows side, order type, qty, estimated price, estimated total.
  7. Click "Submit Order" to execute.
- **Key note**: There is no persistent order ticket panel on screen. The
  order flow is entirely within a modal overlay.

## Watchlist -- Right Sidebar

- **Position**: Right side of the page on web, approximately 30% width.
  Scrollable list.
- **Visual cues**: Titled "Lists" or showing custom list names. Each row
  shows ticker, price, and a mini sparkline chart. Change percentage shown
  in green (up) or red (down).
- **How to identify**: Right column with small inline sparkline charts next
  to each ticker. This inline mini-chart is distinctive to Robinhood.
- **Sections**: "My First List" (default), custom lists, "Recently Viewed."

## Positions and Portfolio

- **Not a traditional bottom panel**: Robinhood does not show a persistent
  positions table like other platforms.
- **Portfolio page**: Accessible from the main navigation. Shows total
  portfolio value as a very large number at the top, with a portfolio
  performance chart below.
- **Individual positions**: Click a stock in your portfolio to see position
  details (shares owned, average cost, total return, equity).
- **Orders**: Accessible from the account menu. Shows pending, filled, and
  cancelled orders in a simple list.

## Limitations the Agent Must Know

- **Order types**: Historically limited. Market, Limit, Stop Loss, Stop
  Limit available for stocks. Options have their own flow. No OCO, OTO,
  or bracket orders.
- **No Level 2 data**: Level 2 (depth of market) requires Robinhood Gold
  subscription. Without it, only NBBO (best bid/ask) is shown.
- **No advanced charting**: No built-in indicator library, no drawing tools
  (basic charting only). For technical analysis, use a separate platform.
- **Fractional shares**: Robinhood supports fractional shares for many
  stocks. The order entry allows dollar-amount orders.
- **Crypto**: Robinhood supports crypto trading in the same interface.
  Crypto assets appear in the watchlist and portfolio alongside stocks.

## Visual Identification Checklist

- Bright GREEN as the dominant brand color: green feather logo, green
  trade button, green positive-change text.
- Minimalist white/light UI with very little visual clutter.
- Line chart as default (not candles) -- distinctive among trading apps.
- Mini sparkline charts in the watchlist sidebar.
- No persistent order ticket panel -- trades via modal only.
- Large bold price text above the chart.
- "Trade [TICKER]" green button below the chart.
- Feather logo in the top-left corner.
- No drawing tools or indicator sidebar.

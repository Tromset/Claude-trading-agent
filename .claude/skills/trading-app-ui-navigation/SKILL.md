---
name: trading-app-ui-navigation
description: Use when the agent needs to identify a trading platform from a screenshot and map its visual regions to locate the chart, order ticket, watchlist, positions, and account bar for safe interaction.
---

# Trading App UI Navigation

The *what to see* skill. Maps any trading platform's visual layout to a generic region model so the agent knows where the chart is, where orders go, where positions are shown, and where the account bar lives.

## When to use this skill

- First time the agent sees a new platform screenshot.
- After a platform UI update changes the layout.
- When `screenshot-vision-protocol` ORIENT step needs to map regions.
- When the agent needs to find a specific UI element (order ticket, position table, etc.).

**Anti-triggers:** not for chart analysis (use price-action, chart-patterns, indicators). Only for navigating the platform interface.

## Prerequisites

- A screenshot of the trading platform.
- Platform identity (known or to be determined).

## Core concepts

### The Generic Region Model

Every trading platform follows approximately the same layout:

```
┌────────────────────────────────────────────────────┐
│ ACCOUNT BAR  (account name, cash, buying power)    │
├──────────┬──────────────────────┬──────────────────┤
│ WATCHLIST │                      │ ORDER TICKET     │
│ (symbols, │    CHART AREA        │ (symbol, side,   │
│  prices,  │    (candles, lines,  │  qty, type,      │
│  change)  │     indicators,      │  price, TIF,     │
│           │     drawing tools)   │  submit button)  │
│           │                      │                  │
├─���────────┴──────────────────────┴──────────────────��
│ BOTTOM PANEL (positions, working orders, history)   │
└──────────────��───────────────────────────��─────────┘
```

**Region roles:**

| Region | Role | What to look for |
|---|---|---|
| Account Bar | Account identification, available capital | Account name/number, cash balance, buying power, margin used |
| Watchlist | Instrument selection, price scanning | Ticker symbols, last price, change %, click to load chart |
| Chart Area | Price analysis, pattern recognition | Candles/bars, time axis, price axis, indicator overlays |
| Order Ticket | Trade execution | Side (buy/sell), qty, order type, prices, TIF, submit |
| Bottom Panel | Position management, order tracking | Open positions, working orders, filled orders, P&L |

### Platform Identification

Visual cues to identify the platform:

| Platform | Key visual cues |
|---|---|
| **TradingView** | Dark/light theme toggle, pine script editor tab, "Strategy Tester" tab, TV logo (feather icon), "Paper Trading" panel |
| **Webull** | Orange/teal color scheme, "Paper" toggle, mobile-inspired web design |
| **Robinhood** | Minimalist green/white, large chart center, limited order options, no L2 by default |
| **Thinkorswim (TOS)** | Dense, dark interface, multiple tabs (Monitor/Trade/Analyze/Scan), "Active Trader" ladder |
| **MetaTrader 5** | Classic Windows-style, "Market Watch" panel, "Navigator" panel, "Terminal" at bottom |

If the platform cannot be identified → treat as unknown → emit `Z` → escalate.

### Mapping Unknown Platforms

If the agent encounters a platform it hasn't seen before but can still identify the generic regions:

1. Look for the chart (usually the largest visual element, center).
2. Look for an order entry area (forms with buy/sell buttons, price fields).
3. Look for a positions/orders table (tabular data at the bottom).
4. Look for an account indicator (balance, name — usually top).
5. If all four regions can be mapped → proceed cautiously with explicit field verification.
6. If any region is ambiguous → `Z` + escalate.

## Decision procedure

1. Receive a screenshot.
2. Identify the platform (visual cues from table above).
3. If known platform → load the corresponding reference file for detailed layout.
4. If unknown → attempt generic region mapping.
5. Map each region in the current screenshot to the generic model.
6. Report the mapping to `screenshot-vision-protocol` for the ORIENT step.
7. Highlight any deviations from the expected layout (missing panel, rearranged elements).

## Heuristics & thresholds

- Chart area is almost always the largest region by pixel area.
- Order tickets have input fields (text boxes) and colored buttons (green=buy, red=sell).
- Position tables have columns with tickers, qty, avg price, P&L.
- Account bars are at the top and contain dollar amounts.
- If the platform uses tabs (TOS, TradingView), ensure the correct tab is active.

## Common failure modes

- **Confusing chart tools with order entry.** Drawing tools (lines, Fib) are NOT order entry.
- **Missing the account selector.** Some platforms have multiple accounts in a dropdown — easy to miss.
- **Confusing paper vs live mode.** The visual difference is often subtle (a small "Paper" label).
- **Not noticing a tab switch.** On TOS, the "Trade" tab shows order entry; "Monitor" shows positions. Being on the wrong tab → can't find expected regions.

## Outputs expected

```json
{
  "skill": "trading-app-ui-navigation",
  "platform": "tradingview" | "webull" | "robinhood" | "thinkorswim" | "mt5" | "unknown",
  "regions_mapped": {
    "account_bar": {"found": true, "location": "top"},
    "watchlist": {"found": true, "location": "left"},
    "chart": {"found": true, "location": "center"},
    "order_ticket": {"found": true, "location": "right"},
    "bottom_panel": {"found": true, "location": "bottom"}
  },
  "mode": "live" | "paper" | "unknown",
  "deviations": []
}
```

## References (lazy-load)

- `references/generic-region-map.md` — the universal layout with detailed descriptions.
- `references/tradingview.md` — TradingView-specific layout + paper trading.
- `references/webull.md` — Webull layout + paper trading.
- `references/robinhood.md` — Robinhood layout.
- `references/thinkorswim.md` — Thinkorswim layout.
- `references/mt5.md` — MetaTrader 5 layout.

## Cross-links

- Pairs with: `screenshot-vision-protocol` (ORIENT step), `paper-trading-workflow` (platform-specific paper setup), `broker-and-platform-selection` (platform evaluation).

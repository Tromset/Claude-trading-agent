---
name: claude-trade
description: Use when you need to find the right trading skill for any situation — routes questions, analyses, and trade decisions to the correct skill by keyword, intent, or scenario matching.
---

# Skill Finder — Trading Skills Router

The entry point to the trading skills library. Invoke this skill when you don't know which trading skill to use, or when you want to understand what's available. It maps any trading situation, question, or intent to the correct skill(s).

## When to use this skill

- You're about to trade and don't know where to start.
- You have a question about markets, analysis, or execution and need the right skill.
- You want to see all available skills organized by category.
- You need to chain multiple skills together for a complex scenario.

## Quick Lookup — By What You Want To Do

### "I want to trade"
→ Start with `trading-master` — it routes everything.
→ Then `pre-trade-checklist-playbook` — 12-step gate before any order.
→ Then `buy-sell-hold-decision` — produces the final X (buy) / Y (sell) / Z (hold).

### "I want to analyze a chart"
→ `price-action-and-market-structure` — trend, structure, swing points.
→ `chart-patterns` — H&S, flags, triangles, double tops, cup & handle.
→ `technical-indicators` — RSI, MACD, Bollinger, ATR, ADX, VWAP.
→ `support-resistance-and-fibonacci` — key levels, pivots, Fib retracement.
→ `volume-analysis` — volume confirmation, divergence, profile.

### "I want to evaluate a stock like Buffett"
→ `fundamental-analysis-and-value-investing` — 10-K, moat, DCF, margin of safety.
→ `watchlist-and-screening` — build and manage your candidate universe.

### "I want to size my position / manage risk"
→ `risk-management` — 1% rule, ATR stops, R:R, Kelly, portfolio heat.

### "I want to pick a strategy"
→ `trading-strategies-playbook` — index of all strategies, then drill into:
  - `references/day-trading.md`
  - `references/swing-trading.md`
  - `references/position-trading.md`
  - `references/breakout.md`
  - `references/mean-reversion.md`
  - `references/trend-following.md`

### "I want to trade crypto"
→ `crypto-trading-specifics` — 24/7 markets, on-chain metrics, exchange risk.
→ `crypto-trading-specifics/references/perps-and-funding.md` — perpetuals, funding rates, liquidation.

### "I want to trade options or futures"
→ `derivatives-options-and-futures` — Greeks, strategies, margin.
→ `derivatives-options-and-futures/references/greeks.md` — delta, gamma, theta, vega.
→ `derivatives-options-and-futures/references/options-strategies.md` — spreads, straddles, iron condors.
→ `derivatives-options-and-futures/references/futures-basics.md` — contracts, contango, roll.

### "I want to practice without real money"
→ `paper-trading-workflow` — setup, promotion criteria (30+ trades), protocol.
→ `paper-trading-workflow/references/tradingview-paper-setup.md`
→ `paper-trading-workflow/references/webull-paper-setup.md`

### "I want to review my performance"
→ `trade-journaling-and-backtesting` — journal entries, R-multiples, metrics.
→ `trade-journaling-and-backtesting/references/metrics-glossary.md` — Sharpe, Sortino, expectancy, drawdown.
→ `trade-journaling-and-backtesting/references/journal-schema.md` — JSON schema for entries/exits/overrides.

### "I want to evaluate a systematic strategy"
→ `systematic-and-algo-trading` — backtest validity, walk-forward, Monte Carlo.
→ `systematic-and-algo-trading/references/backtest-pitfalls.md` — overfitting, look-ahead bias, survivorship.
→ `systematic-and-algo-trading/references/walk-forward.md` — WFA methodology.

### "I want to navigate a trading platform"
→ `trading-app-ui-navigation` — generic region model + per-platform layouts.
→ `screenshot-vision-protocol` — 7-step visual verification before any click.

### "Something feels wrong / I need to stop"
→ `safety-and-kill-switch` — hard kills, soft kills, abort protocol.

### "I need to check rules / regulations"
→ `regulations-and-tax-awareness` — PDT, wash-sale, KYC, settlement.
→ `broker-and-platform-selection` — choosing the right broker/platform.

### "I'm on tilt / making emotional decisions"
→ `trading-psychology` — biases, FOMO, revenge trading, discipline.

### "What's happening in the macro environment?"
→ `news-and-macro-awareness` — FOMC, CPI, NFP, earnings calendar, sentiment.

### "I want to understand how markets work"
→ `trading-fundamentals` — exchanges, sessions, asset classes, settlement.
→ `market-microstructure` — order book, bid/ask, liquidity, halts.
→ `order-types-execution` — market/limit/stop/OCO, time-in-force.

## Keyword → Skill Map

| Keyword | Skill |
|---|---|
| buy, entry, long, open | `buy-sell-hold-decision` → X |
| sell, exit, close, short, stop-out | `buy-sell-hold-decision` → Y |
| hold, wait, nothing, skip | `buy-sell-hold-decision` → Z |
| candle, trend, structure, swing, BOS, CHOCH | `price-action-and-market-structure` |
| pattern, head-and-shoulders, flag, triangle, wedge, cup | `chart-patterns` |
| RSI, MACD, Bollinger, EMA, SMA, ADX, ATR, stochastic | `technical-indicators` |
| support, resistance, Fibonacci, pivot, level | `support-resistance-and-fibonacci` |
| volume, OBV, VWAP, profile, divergence | `volume-analysis` |
| Buffett, value, moat, DCF, intrinsic, 10-K, earnings quality | `fundamental-analysis-and-value-investing` |
| screen, watchlist, filter, universe, candidates | `watchlist-and-screening` |
| FOMC, CPI, NFP, news, macro, calendar, blackout | `news-and-macro-awareness` |
| size, position, risk, stop, R:R, Kelly, heat | `risk-management` |
| bias, FOMO, tilt, revenge, discipline, emotion | `trading-psychology` |
| strategy, day-trade, swing, breakout, mean-reversion, trend | `trading-strategies-playbook` |
| option, call, put, Greek, delta, theta, spread, straddle | `derivatives-options-and-futures` |
| crypto, Bitcoin, ETH, funding, perp, liquidation, on-chain | `crypto-trading-specifics` |
| backtest, walk-forward, overfit, systematic, algo | `systematic-and-algo-trading` |
| screenshot, click, verify, pre-click, vision | `screenshot-vision-protocol` |
| platform, TradingView, Webull, Robinhood, TOS, MT5 | `trading-app-ui-navigation` |
| paper, practice, simulate, promotion | `paper-trading-workflow` |
| journal, log, R-multiple, metrics, Sharpe, expectancy | `trade-journaling-and-backtesting` |
| kill, stop, abort, emergency, flatten, anomaly | `safety-and-kill-switch` |
| checklist, gate, verify, pre-trade | `pre-trade-checklist-playbook` |
| PDT, wash-sale, regulation, tax, KYC, margin-call | `regulations-and-tax-awareness` |
| broker, platform, account, commission | `broker-and-platform-selection` |
| order, limit, market, stop-limit, OCO, TIF | `order-types-execution` |
| order-book, spread, liquidity, slippage, bid, ask | `market-microstructure` |
| exchange, session, asset-class, settlement | `trading-fundamentals` |

## Full Skill Index (27 skills, 5 tiers)

See `references/full-skill-index.md` for the complete index with tier classification and priority ranking.

## Decision Procedure

1. Read the user's intent or the current situation.
2. Match keywords or intent to the tables above.
3. If multiple skills match → load them in priority order (safety > risk > strategy > analysis).
4. If no clear match → start with `trading-master` which routes everything.
5. If the user just wants information → load the relevant skill, answer, emit Z (no action).
6. If the user wants to trade → follow the full chain: analysis → strategy → risk → decision → checklist → execution → journal.

## Common Chains (multi-skill workflows)

**Full trade workflow:**
`trading-master` → analysis skills → `risk-management` → `buy-sell-hold-decision` → `pre-trade-checklist-playbook` → `screenshot-vision-protocol` → `order-types-execution` → `trade-journaling-and-backtesting`

**Buffett deep-dive:**
`watchlist-and-screening` → `fundamental-analysis-and-value-investing` → `news-and-macro-awareness` → `risk-management` → `buy-sell-hold-decision`

**Quick technical scan:**
`price-action-and-market-structure` → `chart-patterns` → `technical-indicators` → `support-resistance-and-fibonacci` → `volume-analysis`

**Post-trade review:**
`trade-journaling-and-backtesting` → `trading-psychology` (if loss streak) → `systematic-and-algo-trading` (if systematic strategy)

**Emergency:**
`safety-and-kill-switch` → flatten → `trade-journaling-and-backtesting` → `paper-trading-workflow` (return to paper)

## References (lazy-load)

- `references/full-skill-index.md` — complete index with descriptions, tiers, and priority.

## Cross-links

- Routes to: every other skill in the library.
- Start here if you don't know where to start.

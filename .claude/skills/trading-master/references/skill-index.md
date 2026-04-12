# Skill Index (machine-readable)

One line per skill. Every skill in `.claude/skills/` must appear here.

## Tier 0 — Orchestration
- `trading-master` — router, global invariants, decision tree. Root skill.
- `buy-sell-hold-decision` — X/Y/Z action primitive and output schema.

## Tier 1 — Foundations
- `trading-fundamentals` — market structure, asset classes, sessions, participants.
- `market-microstructure` — order book, bid/ask, liquidity, spread, slippage.
- `order-types-execution` — market/limit/stop/stop-limit/trailing/OCO, TIF.
- `regulations-and-tax-awareness` — PDT, wash-sale, KYC/AML, holding-period basics.
- `broker-and-platform-selection` — how to choose a broker/account.

## Tier 2 — Analysis Toolkits
- `price-action-and-market-structure` — candles, BOS/CHOCH, HH/HL/LH/LL.
- `chart-patterns` — H&S, triangles, flags, wedges, double tops/bottoms.
- `technical-indicators` — MA/EMA/RSI/MACD/BB/Stoch/ATR/ADX + references.
- `support-resistance-and-fibonacci` — S/R, pivots, Fib retracement/extension.
- `volume-analysis` — volume, OBV, VWAP, volume profile.

## Tier 3 — Fundamentals & Macro
- `fundamental-analysis-and-value-investing` — Buffett, 10-K, DCF, moat, MoS.
- `watchlist-and-screening` — building/maintaining candidate universe.
- `news-and-macro-awareness` — econ calendar, FOMC/CPI/NFP, earnings.

## Tier 4 — Decision & Strategy
- `risk-management` — sizing, R:R, Kelly, portfolio heat, stops.
- `trading-psychology` — biases, discipline, tilt, journaling mindset.
- `trading-strategies-playbook` — day/swing/position/breakout/mean-reversion/trend-following.
- `derivatives-options-and-futures` — options Greeks, strategies, futures basics.
- `crypto-trading-specifics` — 24/7, perps, funding, exchange risk.
- `systematic-and-algo-trading` — backtest pitfalls, walk-forward, overfitting.

## Tier 5 — Embodiment
- `screenshot-vision-protocol` — pre-click verification, error recovery.
- `trading-app-ui-navigation` — per-vendor region maps and element catalogs.
- `paper-trading-workflow` — TradingView/Webull/Investopedia practice protocols.
- `trade-journaling-and-backtesting` — journal schema, metrics glossary.
- `safety-and-kill-switch` — abort conditions, drawdown, anomaly handling.
- `pre-trade-checklist-playbook` — master 12-step gate, final veto.

## Routing priority (tie-break)

When two skills disagree, the higher wins:

1. `safety-and-kill-switch`
2. `pre-trade-checklist-playbook`
3. `risk-management`
4. `regulations-and-tax-awareness`
5. `fundamental-analysis-and-value-investing` (for long-horizon setups)
6. Strategy skills (playbook / derivatives / crypto)
7. Analysis toolkits (price action, patterns, indicators, S/R, volume)
8. Discretionary judgment (last resort → default to `Z`)

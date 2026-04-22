# Full Skill Index

Complete index of all 27 trading skills + this skill-finder. Organized by tier with priority ranking.

## Priority Ranking (when skills disagree, higher rank wins)

| Priority | Skill | Why it outranks |
|---|---|---|
| 1 | `safety-and-kill-switch` | Capital preservation is absolute |
| 2 | `pre-trade-checklist-playbook` | Final gate, veto authority |
| 3 | `risk-management` | No trade without risk clearance |
| 4 | `regulations-and-tax-awareness` | Law > strategy |
| 5 | `fundamental-analysis-and-value-investing` | Long-horizon conviction |
| 6 | Strategy skills (playbook, derivatives, crypto) | Trade logic |
| 7 | Analysis skills (PA, patterns, indicators, S/R, volume) | Evidence |
| 8 | Discretionary judgment | Last resort → default Z |

## Tier 0 — Orchestration

| Skill | Description | Invoke when |
|---|---|---|
| `trading-master` | Root router, global invariants, X/Y/Z contract | Session boot, new situation, don't know where to start |
| `buy-sell-hold-decision` | X/Y/Z action primitive, confidence rubric, output schema | Any analysis is complete and needs to collapse to a decision |
| `skill-finder` | This skill — routes to the right skill by keyword/intent | You don't know which skill to use |

## Tier 1 — Foundations

| Skill | Description | Invoke when |
|---|---|---|
| `trading-fundamentals` | Market structure, asset classes, sessions, participants | Need market context for an instrument |
| `market-microstructure` | Order book, bid/ask, liquidity, spread, slippage, halts | Reasoning about execution quality or order book |
| `order-types-execution` | All order types, TIF, brackets, short-sale rules | Choosing order type for an X or Y |
| `regulations-and-tax-awareness` | PDT, wash-sale, KYC/AML, settlement | Checking if a trade would violate rules |
| `broker-and-platform-selection` | Broker evaluation, account types | Choosing or evaluating a broker |

## Tier 2 — Analysis Toolkits

| Skill | Description | Invoke when |
|---|---|---|
| `price-action-and-market-structure` | Candles, trend, BOS/CHOCH, HH/HL/LH/LL, supply/demand | Reading a chart with just price and volume |
| `chart-patterns` | H&S, triangles, flags, wedges, double tops, cup & handle | Classifying a price formation into a named pattern |
| `technical-indicators` | RSI, MACD, Bollinger, ATR, ADX, Stochastic, VWAP | Selecting/interpreting indicators for confluence |
| `support-resistance-and-fibonacci` | Horizontal S/R, pivots, Fib retracement/extension | Identifying key price levels for entry/stop/target |
| `volume-analysis` | OBV, VWAP, volume profile, divergence | Confirming or denying a price move with volume |

## Tier 3 — Fundamentals & Macro

| Skill | Description | Invoke when |
|---|---|---|
| `fundamental-analysis-and-value-investing` | Buffett-style: 10-K, moat, DCF, margin of safety | Evaluating a stock as a long-term value candidate |
| `watchlist-and-screening` | Candidate universe, screening, tier management | Building or filtering a watchlist |
| `news-and-macro-awareness` | FOMC, CPI, NFP, earnings, news blackout, sentiment | Checking macro events before trading |

## Tier 4 — Decision & Strategy

| Skill | Description | Invoke when |
|---|---|---|
| `risk-management` | 1% rule, ATR stops, R:R, Kelly, portfolio heat | Before every X or Y — sizing and risk clearance |
| `trading-psychology` | Biases, FOMO, tilt, revenge trading, discipline | Recognizing emotional interference |
| `trading-strategies-playbook` | Day/swing/position/breakout/mean-reversion/trend | Picking a strategy for the current setup |
| `derivatives-options-and-futures` | Greeks, options strategies, futures basics | Considering options or futures |
| `crypto-trading-specifics` | 24/7 markets, perps, funding, on-chain, exchange risk | Trading any cryptocurrency |
| `systematic-and-algo-trading` | Backtesting, walk-forward, overfitting, Monte Carlo | Evaluating a rule-based strategy |

## Tier 5 — Embodiment

| Skill | Description | Invoke when |
|---|---|---|
| `screenshot-vision-protocol` | 7-step vision: capture→orient→read→verify→confirm→act→validate | Before any click on a trading platform |
| `trading-app-ui-navigation` | Generic region model + TradingView/Webull/Robinhood/TOS/MT5 | Identifying and navigating a platform screenshot |
| `paper-trading-workflow` | Paper setup, promotion criteria (≥30 trades), protocol | Practicing before live, validating strategies |
| `trade-journaling-and-backtesting` | Journal schema, R-multiples, metrics dashboard | Logging trades, reviewing performance |
| `safety-and-kill-switch` | Hard kills, soft kills, abort protocol, reset | Emergency stop, anomaly, drawdown limit |
| `pre-trade-checklist-playbook` | 12-step final gate before any order | Last check before executing any X or Y |

## Reference Files Quick Access

Each skill may have reference files for deep content. Key ones:

| Reference | Parent Skill | Content |
|---|---|---|
| `buy-triggers.md` | buy-sell-hold-decision | When to emit X |
| `sell-triggers.md` | buy-sell-hold-decision | When to emit Y |
| `hold-triggers.md` | buy-sell-hold-decision | When to emit Z |
| `xyz-action-vocabulary.md` | buy-sell-hold-decision | Formal X/Y/Z definitions |
| `position-sizing-formulas.md` | risk-management | 6 sizing methods |
| `kelly-and-heat.md` | risk-management | Kelly criterion, portfolio heat |
| `buffett-checklist.md` | fundamental-analysis | 4-point Buffett gate |
| `dcf-worked-example.md` | fundamental-analysis | Full DCF walkthrough |
| `financial-ratios.md` | fundamental-analysis | 25+ ratios with formulas |
| `candlesticks.md` | price-action | Full candle pattern catalog |
| `market-structure-bos-choch.md` | price-action | BOS/CHOCH definitions |
| `reversal-patterns.md` | chart-patterns | H&S, double top/bottom, etc. |
| `continuation-patterns.md` | chart-patterns | Flags, pennants, triangles |
| `pattern-reliability-table.md` | chart-patterns | 18-pattern reliability data |
| `trend.md` | technical-indicators | SMA, EMA, ADX, Ichimoku |
| `momentum.md` | technical-indicators | RSI, MACD, Stochastic, CCI |
| `volatility.md` | technical-indicators | ATR, Bollinger, Keltner |
| `volume-indicators.md` | technical-indicators | OBV, VWAP, A/D, CMF, MFI |
| `greeks.md` | derivatives | Delta, gamma, theta, vega |
| `options-strategies.md` | derivatives | Spreads, straddles, condors |
| `futures-basics.md` | derivatives | Contracts, margin, roll |
| `perps-and-funding.md` | crypto | Perpetuals, funding rate, liquidation |
| `backtest-pitfalls.md` | systematic-algo | 10 backtesting errors |
| `walk-forward.md` | systematic-algo | WFA methodology |
| `metrics-glossary.md` | journaling | All performance metrics |
| `journal-schema.md` | journaling | JSON schema for journal entries |
| `checklist-12-step.md` | pre-trade-checklist | Detailed 12-step breakdown |
| `pre-click-verification.md` | screenshot-vision | 14-field verification |
| `error-recovery.md` | screenshot-vision | 11 anomaly recovery paths |
| `economic-calendar-events.md` | news-macro | Event impact ratings |
| `order-type-matrix.md` | order-types | 25-row situation→order mapping |
| `global-invariants.md` | trading-master | 8 inviolable rules |
| `decision-tree.md` | trading-master | Full routing with examples |
| `skill-index.md` | trading-master | Machine-readable skill list |

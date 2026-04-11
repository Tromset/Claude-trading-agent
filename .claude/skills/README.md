# Claude Trading Agent — Skills Library

A dense, composable knowledge base for a Claude-based trading cowork agent that reasons about markets and acts on trading app views (screenshot-driven).

> **Educational only.** Nothing here is financial advice. No guarantee of profit. The agent must respect broker Terms of Service, exchange rules, and applicable regulations at all times.

## Philosophy

1. **Buffett-first.** Prefer inaction. Prefer quality. Prefer long horizons. Short-term playbooks exist but are subordinate to value-based conviction.
2. **Z is the default.** Every decision collapses to `X` (buy), `Y` (sell), or `Z` (hold / do nothing). When anything is unclear — emit `Z`.
3. **Risk before return.** No order is placed without an approved risk-management output.
4. **Screen is truth.** The agent re-screenshots before every click and aborts on any mismatch with its internal state.
5. **Fail safe.** Ambiguity → `safety-and-kill-switch` → `Z`.
6. **Numbers over adjectives.** "Volume > 1.5× 20-day average," not "heavy volume."
7. **References are lazy.** `SKILL.md` is dense and short; deep tables / per-vendor layouts live in `references/*.md` inside each skill folder.

## How a Cowork Agent Uses This Library

1. **Boot** — load `trading-master/SKILL.md`. It routes to everything else.
2. **Identify situation** — screenshot + text prompt describes what the agent is facing.
3. **Route** — `trading-master` decision tree selects the skills needed for the situation.
4. **Gate** — `pre-trade-checklist-playbook` runs the master 12-step gate.
5. **Decide** — output resolves to `X`, `Y`, or `Z` via `buy-sell-hold-decision`.
6. **Act** — `screenshot-vision-protocol` + `trading-app-ui-navigation` drive the click path; `order-types-execution` chooses the order type.
7. **Record** — `trade-journaling-and-backtesting` logs every decision (including `Z` overrides).

## Skill Index (by tier)

### Tier 0 — Orchestration
- `trading-master` — the router. Read first. Holds the decision tree + global invariants.
- `buy-sell-hold-decision` — the X / Y / Z action primitive every other skill resolves to.

### Tier 1 — Foundations
- `trading-fundamentals` — market structure, asset classes, sessions, participants.
- `market-microstructure` — order book, spread, liquidity, slippage.
- `order-types-execution` — market / limit / stop / stop-limit / trailing / OCO, TIF.
- `regulations-and-tax-awareness` — PDT, wash-sale, KYC/AML, holding-period basics.
- `broker-and-platform-selection` — how to pick a broker / account type.

### Tier 2 — Analysis Toolkits
- `price-action-and-market-structure` — candlesticks, BOS/CHOCH, HH/HL/LH/LL, supply/demand.
- `chart-patterns` — H&S, triangles, flags, wedges, double tops/bottoms, cup & handle.
- `technical-indicators` — MA/EMA, RSI, MACD, BB, Stochastic, ATR, ADX (trend/momentum/vol/volume refs).
- `support-resistance-and-fibonacci` — S/R, pivots, Fib retracement / extension, confluence.
- `volume-analysis` — volume bars, OBV, VWAP, volume profile.

### Tier 3 — Fundamentals & Macro
- `fundamental-analysis-and-value-investing` — Buffett principles, 10-K reading, DCF, moat, margin of safety.
- `watchlist-and-screening` — building/maintaining a candidate universe.
- `news-and-macro-awareness` — economic calendar, FOMC/CPI/NFP, earnings.

### Tier 4 — Decision & Strategy
- `risk-management` — sizing, R:R, Kelly, portfolio heat, stop placement.
- `trading-psychology` — biases, discipline, tilt prevention.
- `trading-strategies-playbook` — day/swing/position, trend/mean-reversion/breakout.
- `derivatives-options-and-futures` — options basics, Greeks, futures margin.
- `crypto-trading-specifics` — 24/7, perps, funding rates, exchange risk.
- `systematic-and-algo-trading` — backtest pitfalls, walk-forward, signal discipline.

### Tier 5 — Embodiment (visual / operational)
- `screenshot-vision-protocol` — how to *look* at a screen (pre-click verification, error recovery).
- `trading-app-ui-navigation` — per-vendor region maps (TradingView, Webull, Robinhood, TOS, MT5).
- `paper-trading-workflow` — practice protocols on TradingView / Webull paper / Investopedia sim.
- `trade-journaling-and-backtesting` — trade log schema, metrics glossary.
- `safety-and-kill-switch` — abort conditions, drawdown limits, anomaly escalation.
- `pre-trade-checklist-playbook` — master 12-step gate. Runs last, can veto any `X`/`Y` to `Z`.

## Global Invariants (enforced by every skill)

1. Never place an order without a fresh `risk-management` output.
2. Never click without pre-click verification from `screenshot-vision-protocol`.
3. Never exceed account-level risk caps (daily loss, per-trade, portfolio heat).
4. Always journal every action — including `Z` overrides.
5. If screen state disagrees with internal state → abort to `safety-and-kill-switch` → emit `Z`.
6. Respect broker ToS, exchange rules, PDT, wash-sale, applicable regulations.
7. No action during the 5 minutes before or after a high-impact news release for the relevant instrument (unless the strategy is explicitly an event-trading strategy and the setup was planned in advance).

## Verification

See `.claude/skills/verification/scenarios/` for frozen dry-run scenarios. Each scenario lists:
- The situation (screenshot description + context)
- The expected skill-invocation path
- The expected final output (`X`, `Y`, or `Z` with justification)

Run a fresh Claude session against each scenario with only the skill files available and compare outputs.

## Disclaimers

- **Not financial advice.** Educational content only.
- **Past performance ≠ future results.** No strategy is guaranteed.
- **Know your jurisdiction.** Tax and regulatory rules vary; consult a professional.
- **Broker ToS first.** If broker rules conflict with this library, the broker wins and the agent emits `Z`.

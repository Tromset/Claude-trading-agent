---
name: trading-fundamentals
description: Use when the agent needs to situate an instrument in its market context — exchange, session, asset class, corporate actions, settlement, index membership — before any analysis or order. Covers market structure, asset classes, sessions, participants, and corporate events.
---

# Trading Fundamentals

Ground truth about *what* is being traded and *where*. Every downstream analysis assumes the agent has correctly identified the asset class, exchange, session, and any pending corporate action. Getting this layer wrong invalidates everything above it.

## When to use this skill

- First contact with an unfamiliar ticker or instrument.
- Before routing to analysis skills — the asset class determines which playbook applies.
- When a screenshot shows an unusual session (pre-market, after-hours, holiday, half-day).
- When a ticker has pending dividends, splits, or other corporate actions.
- When the agent needs to verify it is trading on the correct exchange / venue.

**Anti-triggers:** do NOT use this skill for technical analysis, sizing, or execution mechanics — those live in their own skills. This one is situational context only.

## Prerequisites

- `trading-master` has routed here.
- The instrument identifier (ticker, exchange, expiry/strike if derivative) is captured from the screen.

## Core concepts

### Exchanges and venues

- **Primary listing exchange:** where the security is registered (NYSE, NASDAQ, AMEX/NYSE American, LSE, TSE, HKEX, etc.).
- **Order routing venues:** retail orders often execute off-exchange at wholesalers/internalizers (Citadel Securities, Virtu) or on ATSs (alternative trading systems) / dark pools.
- **ECNs:** Electronic Communication Networks (ARCA, BATS, EDGX, IEX) — transparent order books that match buyers/sellers directly.
- **Market makers (MMs):** firms obligated (NYSE DMMs, NASDAQ MMs) or incentivized to post two-sided quotes. They profit on the spread and rebates.
- The tape (SIP / consolidated feed) aggregates trades across venues; direct feeds are faster and paid.

### Asset classes (each has its own rules)

| Class | Unit | Venue | Hours (US) | Settlement | Leverage typical |
|---|---|---|---|---|---|
| Equities | Share | NYSE / NASDAQ / ARCA | 09:30–16:00 ET RTH | T+1 (as of May 2024) | Reg T 2:1 overnight, 4:1 intraday PDT |
| ETFs | Share | Same as equities | Same | T+1 | Same as equities |
| Bonds | Face value | OTC / TRACE reporting | ~08:00–17:00 ET | T+1 | Haircut-based |
| FX (spot) | Notional | OTC interbank | 24/5 (Sun 17:00 ET – Fri 17:00 ET) | T+2 spot | Retail 50:1 majors (US), 30:1 (EU) |
| Futures | Contract | CME / ICE / Eurex | Near 24/5 w/ daily pause | Daily mark-to-market | SPAN margin, often 10–30:1 |
| Options | Contract (100 shrs) | CBOE / ISE / etc. | 09:30–16:00 ET (some 16:15) | T+1 | Defined risk long; margined short |
| Crypto | Coin | CEX/DEX | 24/7/365 | Instant on-chain / exchange | 1:1 spot, up to 100:1 perps offshore |

An equity playbook does NOT apply to a perpetual swap without adjustment. The agent must confirm the class before loading a strategy skill.

### Session times (US equities reference)

- **Pre-market (ETH):** 04:00–09:30 ET. Thin liquidity, wide spreads, limited order types, not all brokers support.
- **Regular Trading Hours (RTH):** 09:30–16:00 ET. Deepest liquidity. The "09:30 open" and "16:00 close" are auctions, not continuous.
- **After-hours (ETH):** 16:00–20:00 ET. Thin again.
- **Opening auction:** single-price cross at 09:30 ET. MOO / LOO orders participate.
- **Closing auction:** single-price cross at 16:00 ET. MOC / LOC orders participate — usually the highest-volume print of the day.
- **Half-days:** early close at 13:00 ET on select dates (day after Thanksgiving, Christmas Eve, etc.).
- **Holiday calendar:** NYSE publishes annually; the agent must have the list loaded.

### Global sessions (FX / index futures convention)

- **Tokyo:** 19:00–04:00 ET
- **London:** 03:00–12:00 ET (overlap with NY 08:00–12:00 ET is the highest-volume window)
- **New York:** 08:00–17:00 ET
- **Sydney:** 17:00–02:00 ET

Equity-index futures (ES, NQ, YM, RTY) trade ~23 hours/day with a short daily settlement pause.

### Participants

- **Retail** — small orders, typically routed via wholesalers. Often the "dumb money" in classical lore; increasingly informed post-2020.
- **Institutional (long-only)** — mutual funds, pensions, SMAs. Large, slow, benchmark-aware.
- **Hedge funds** — directional, long/short, often levered. Varied horizons.
- **Market makers (MMs)** — profit on spread + rebates; neutral on direction; hedge inventory.
- **HFT / proprietary** — latency-sensitive, microseconds. *Out of scope for a screenshot-driven agent.*
- **Corporate** — buybacks, insider trades, issuance. Large but infrequent.
- **Central banks / sovereigns** — FX and bond markets.

### Ticker anatomy

- **Root symbol:** `AAPL`, `MSFT`, `ES`, `BTC`.
- **Exchange prefix:** `NASDAQ:AAPL`, `NYSE:BRK.B`. Always disambiguate when writing orders — some symbols exist on multiple venues.
- **Class suffix:** `BRK.A` vs `BRK.B`, `GOOG` vs `GOOGL` (voting vs non-voting).
- **Futures:** `ESM2026` = E-mini S&P 500, June 2026. Month codes F,G,H,J,K,M,N,Q,U,V,X,Z.
- **Options:** `AAPL 2026-06-19 C 200` = Apple June 19 2026 $200 call. OCC symbology.
- **Crypto:** `BTC/USD`, `BTC-PERP`, `ETHUSDT`. Pair + venue.

### Dividends, splits, corporate actions

- **Cash dividend:** record date → ex-dividend date → payment date. Price drops by ~dividend amount on ex-date. Stops placed just below price may wick out on the ex-open.
- **Stock split / reverse split:** `2:1` halves the price and doubles the shares; `1:10` reverse decuples price and drops share count. Old stops/targets become invalid — must be recomputed.
- **Spin-off:** shareholders receive shares of a new entity; the parent re-prices. Cost basis splits across parent + spin.
- **M&A:** cash deal pins price at deal price minus arb spread; stock deal tracks acquirer.
- **Earnings:** not a corporate action per se, but a scheduled volatility event — see `news-and-macro-awareness`.

If any corporate action falls within the holding window, the agent should downgrade to `Z` until the event is processed or the thesis is explicitly designed around it.

### Settlement

- **T+1** — US equities, ETFs, corporate bonds (since May 28, 2024). Trade Monday → settles Tuesday.
- **T+2** — FX spot, many non-US equities.
- **T+0 / instant** — crypto on exchange; on-chain pending confirmations.
- **Daily** — futures mark-to-market; variation margin moves every session.
- **Cash accounts** must wait for settled funds before re-using proceeds — a good-faith violation can freeze the account.

### Indices and how they are built

- **S&P 500 (SPX):** 500 US large caps, float-adjusted market-cap weighted. Rebalanced quarterly. Tracked by SPY, IVV, VOO; futures: ES.
- **NASDAQ-100 (NDX):** 100 largest non-financial NASDAQ names, modified cap-weighted with capping rules. Tracked by QQQ; futures: NQ.
- **Dow Jones Industrial Average (DJI):** 30 names, **price-weighted** (higher-priced stocks have more influence — a historical quirk). Tracked by DIA; futures: YM.
- **Russell 2000 (RUT):** 2000 small caps, cap-weighted. Tracked by IWM; futures: RTY.
- **VIX:** derived from SPX option prices, measures 30-day implied vol. Not directly tradable; VX futures and VIX-linked ETPs are proxies.

An index move is a weighted average — a few mega-caps can mask broad weakness. Always cross-check with breadth (advancers/decliners, equal-weight index).

## Decision procedure

1. Parse the ticker from the screen. Identify root + exchange + class suffix / expiry / strike.
2. Classify the asset: equity / ETF / option / future / FX / crypto / bond. If uncertain → `Z`.
3. Identify the primary listing exchange and confirm the current session (pre/RTH/post/closed/holiday).
4. If session is not RTH, flag and consult the strategy skill — most strategies are RTH-only.
5. Check for pending corporate actions in the next 5 trading days (dividends, splits, earnings, M&A vote). If any falls inside the intended holding window → flag to `risk-management` and `buy-sell-hold-decision`.
6. For index / ETF exposure, note the underlying construction and whether the agent is trading the derivative (futures, options) or the cash product.
7. Produce the fundamentals JSON output and hand off to the next skill in the routing chain.

## Heuristics & thresholds

- If the ticker has a class suffix (`.A`/`.B`/`5`) the agent does not recognize → `Z` until confirmed.
- If the session is pre-market / after-hours and the strategy is not explicitly an ETH strategy → downgrade to `Z`.
- If a dividend ex-date is within the next 2 trading days and the position would cross it → recompute stops and notify `risk-management`.
- If a split becomes effective during the holding window → force `Z` on the day of the split; re-enter after prices reset.
- Half-day sessions: cut all time-stops and end-of-day logic to the early close time; do not assume 16:00 ET.
- For non-US instruments: default to `Z` unless the agent has a jurisdiction-specific skill loaded.

## Common failure modes

- **Wrong share class.** Trading `GOOG` when the analysis was on `GOOGL`.
- **Wrong exchange.** Dual-listed names (e.g., `RIO` in NY vs London) have different sessions, liquidity, and currency.
- **Ignoring the ex-dividend drop.** A 2% dividend looks like a 2% gap down and can trigger noise stops.
- **Trading an ETF as if it were its underlying.** ETF NAV can drift from price during stress; leveraged/inverse ETFs decay.
- **Assuming 24/5 = 24/7.** FX is closed on weekends; futures have a daily pause and weekly maintenance.
- **Treating the DJIA like a cap-weighted index.** It is price-weighted — `UNH` moves the Dow more than `AAPL`.
- **Forgetting half-days.** Placing a DAY order expecting a 16:00 close on December 24.

## Outputs expected

```json
{
  "skill": "trading-fundamentals",
  "ticker": "NASDAQ:AAPL",
  "asset_class": "equity",
  "exchange": "NASDAQ",
  "currency": "USD",
  "session_state": "RTH" | "pre-market" | "after-hours" | "closed" | "holiday" | "half-day",
  "next_session_close_et": "2026-04-11T16:00:00-04:00",
  "settlement": "T+1",
  "pending_corporate_actions": [
    {"type": "ex-dividend", "date": "2026-04-15", "amount": 0.26}
  ],
  "index_memberships": ["SPX", "NDX"],
  "notes": "Half-day on 2026-11-27 (early close 13:00 ET)",
  "context_ok": true
}
```

This output feeds into `buy-sell-hold-decision` as context. If `context_ok = false` (unrecognized class, wrong account, pending action inside window) → upstream emits `Z`.

## References (lazy-load)

- `references/asset-class-cheatsheet.md` — hours, settlement, leverage, typical tick sizes per class.
- `references/corporate-actions-handling.md` — how to adjust stops/targets for each action type.
- `references/index-construction.md` — weighting methodologies and rebalance calendars.
- `references/holiday-calendar.md` — US market holidays and half-days through 2030.

## Cross-links

- Pairs with: `market-microstructure` (what happens inside the venue), `regulations-and-tax-awareness` (jurisdiction rules), `news-and-macro-awareness` (scheduled events), `risk-management` (adjusts stops around corporate actions), `buy-sell-hold-decision` (consumes context flags).
- Upstream: `trading-master` (router).

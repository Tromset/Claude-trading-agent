---
name: broker-and-platform-selection
description: Use when choosing or evaluating a broker or trading platform, to match account type, order capabilities, and data quality to the agent's strategy needs.
---

# Broker & Platform Selection

The broker is the agent's gateway to the market. A wrong choice limits order types, increases costs, or blocks strategies entirely. This skill provides evaluation criteria — not rankings.

## When to use this skill

- First-time setup: choosing a broker before paper trading begins.
- Strategy mismatch: a strategy needs an order type or asset class the current broker doesn't support.
- Cost review: commissions or spreads are eating into edge.
- Platform change: migrating from paper to live, or upgrading.

**Anti-triggers:** not for mid-trade decisions. Broker is chosen before trading begins.

## Prerequisites

- Strategy set (which strategies the agent will run → determines order type and asset needs).
- Account size bracket ($1k–$10k, $10k–$100k, $100k+).
- Geographic jurisdiction (determines regulatory body).

## Core concepts

### Evaluation criteria

| Criterion | Why it matters | What to check |
|---|---|---|
| **Regulation / SIPC** | Counterparty risk. Unregulated = uninsured. | SEC/FINRA (US), FCA (UK), ASIC (AU), etc. SIPC coverage up to $500k. |
| **Commissions** | Direct cost per trade. Zero-commission has hidden costs (PFOF). | Per-share, per-contract, spread markup. |
| **Spreads** | Hidden cost for market orders and PFOF brokers. | Compare effective spread vs exchange NBBO. |
| **Order types** | Strategy feasibility. No stop-limit = can't run breakout stops safely. | Market, limit, stop, stop-limit, trailing, OCO, bracket. |
| **Asset coverage** | Can you trade what you need? | US equities, options, futures, forex, crypto, international. |
| **Execution quality** | Price improvement vs adverse fill. | FINRA Rule 606 reports, execution statistics. |
| **Margin rates** | Cost of leverage. | Compare APR; lower is better for swing holds. |
| **Paper trading** | Can the agent practice without real money? | Simulated fills, paper account reset, data quality. |
| **Data quality** | Real-time vs delayed, L1 vs L2. | Data fees, exchange permissions, historical data availability. |
| **API availability** | Future automation potential. | REST/WebSocket API, rate limits, documentation. |
| **Platform stability** | Downtime during volatile markets = kill-switch trigger. | Track record, outage history. |
| **Mobile / web / desktop** | Agent operates via screenshots — platform must be visually parseable. | Clean UI, consistent layout, no excessive popups. |

### Account types

| Type | Key characteristics | PDT applies? | Tax treatment (US) |
|---|---|---|---|
| **Cash** | No leverage, no margin, settlement T+1 | No (exempt) | Taxable |
| **Margin** | 2:1 intraday / 4:1 day-trade leverage, margin interest | Yes if < $25k | Taxable |
| **IRA (Traditional)** | Tax-deferred contributions, taxed on withdrawal | No (cash-like) | Tax-deferred |
| **Roth IRA** | After-tax contributions, tax-free growth/withdrawal | No (cash-like) | Tax-free growth |
| **Custodial / UGMA** | Minor's account, limited activity | Depends | Kiddie tax rules |

**Agent default:** Margin account with > $25k to avoid PDT friction. If under $25k → cash account to avoid PDT restrictions.

### Broker buckets (criteria, not names)

**Discount / zero-commission:** lowest cost, PFOF revenue model, limited research, basic order types. Good for: simple strategies, buy-and-hold, DCA.

**Full-service / active-trader:** advanced order types (bracket, OCO, conditional), better execution, L2 data, complex options. Good for: swing/day trading, multi-leg options, futures.

**Prop / funded:** external capital, profit-sharing, drawdown rules. Good for: experienced traders seeking leverage beyond personal capital.

**Crypto-native:** 24/7 markets, spot + perps, wallet custody options. Good for: crypto strategies. Risk: less regulated, counterparty risk is higher.

### What matters most for the agent

1. **Paper trading support** — the agent must practice first.
2. **Clean visual layout** — agent needs to screenshot-parse the UI reliably.
3. **Order type coverage** — at minimum: market, limit, stop, stop-limit.
4. **Real-time data** — delayed data is unusable for active strategies.
5. **Stability** — no outages during market hours. Kill-switch can't fire if the platform is down.

## Decision procedure

1. List the strategies the agent will run.
2. Derive the required order types, asset classes, and data needs.
3. Check current broker against the criteria table above.
4. If any critical gap (missing order type, no paper trading, delayed data) → flag and recommend switch before trading.
5. If broker is adequate → log the evaluation and proceed to `paper-trading-workflow`.

## Heuristics & thresholds

- If commissions > 0.1% of average trade notional → cost is material; consider alternatives.
- If spreads on the primary instrument > 3× exchange NBBO average → execution quality is suspect.
- If the platform had > 2 outages during RTH in the last quarter → stability risk is elevated.
- Zero-commission is fine for value-investing / swing. For day-trading, execution quality matters more.

## Common failure modes

- **Choosing the cheapest broker without checking order types.** A broker that doesn't support stop-limit orders breaks the risk-management workflow.
- **Ignoring paper-trading quality.** Some paper sims give unrealistic fills (guaranteed limit fills, no slippage). Agent must not over-trust paper results.
- **Not reading the fine print on margin.** Margin calls are real and trigger `safety-and-kill-switch`.
- **Assuming all brokers are regulated.** Check the specific regulatory body.

## Outputs expected

```json
{
  "skill": "broker-and-platform-selection",
  "evaluation": {
    "broker_name": "...",
    "regulation": "SEC/FINRA",
    "order_types_available": ["MARKET", "LIMIT", "STOP", "STOP_LIMIT", "OCO"],
    "paper_trading": true,
    "data_quality": "real-time L1, L2 available for fee",
    "critical_gaps": [],
    "recommendation": "adequate" | "switch recommended"
  }
}
```

## References (lazy-load)

None — this skill is self-contained.

## Cross-links

- Pairs with: `order-types-execution` (order type availability), `paper-trading-workflow` (paper support), `trading-app-ui-navigation` (visual layout parsability), `regulations-and-tax-awareness` (account type → regulatory exposure).

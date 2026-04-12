---
name: derivatives-options-and-futures
description: Use when the agent considers using options or futures for hedging, directional trades, or income generation, to ensure defined-risk structures are used, margin danger is understood, and naked short exposure is never taken.
---

# Derivatives — Options and Futures

Derivatives are tools, not lottery tickets. This agent defaults to **defined-risk structures** (max loss is known before entry). Undefined risk (naked short options, unhedged futures) is forbidden except for covered calls and cash-secured puts on positions the agent is willing to own.

## When to use this skill

- The agent is considering using options instead of stock for a directional trade.
- A hedge is needed for an existing position or portfolio.
- Income generation via covered calls or cash-secured puts is appropriate.
- Futures are being considered as an alternative to ETFs for index/commodity exposure.
- The agent needs to understand margin requirements before entering a derivative position.

**Anti-triggers:**
- Pure stock/ETF trades that do not involve options or futures — use the strategy playbook directly.
- Options pricing theory for academic purposes — this is a practical skill.
- Complex multi-leg strategies beyond what is defined here — emit Z (stay simple).

## Prerequisites

- Options approval level from broker (Level 1-4 determines what is allowed).
- Understanding of the instrument's options liquidity (bid-ask spread, open interest).
- Current implied volatility rank (IVR) to determine if options are cheap or expensive.
- Days to expiration (DTE) appropriate for the strategy (not weekly options for beginners).
- Account margin availability if using futures.
- Fresh `risk-management` sizing run on the max-loss of the structure.

## Core concepts

### Philosophy: defined risk always

| Structure type | Max loss known? | Agent permission |
|---|---|---|
| Long call / long put | Yes (premium paid) | Allowed |
| Vertical spread (debit or credit) | Yes (width minus credit, or debit paid) | Allowed |
| Iron condor / iron butterfly | Yes (width minus credit) | Allowed |
| Covered call (own 100 shares) | Upside capped, downside = stock decline | Allowed |
| Cash-secured put (cash reserved) | Assignment at strike (willing to own) | Allowed |
| Naked short call | Unlimited loss | FORBIDDEN |
| Naked short put (no cash reserve) | Large loss if stock goes to zero | FORBIDDEN |
| Naked short futures | Unlimited loss | FORBIDDEN |

### When to use options (directional)

Options make sense for directional trades when:
1. The agent wants defined risk without a stop-loss order (options cannot be stopped out early by wicks — max loss is the premium).
2. Leverage is desired but must be bounded (a long call controls 100 shares for a fraction of the cost).
3. Implied volatility is low (IVR < 30) — options are cheap, and a vol expansion amplifies gains.
4. The time horizon matches the DTE (minimum 45 DTE for directional, to reduce theta decay).

### When to use options (hedging)

1. Protective put on a stock position facing a binary event (earnings, FDA).
2. Collar (long put + short call) to lock in gains on a position while keeping some upside.
3. Portfolio hedge: long put on SPY/QQQ to protect against broad market decline.

### When to use futures

1. Broad index exposure (ES, NQ) with better capital efficiency than ETFs.
2. Commodity exposure (CL for crude, GC for gold) without ETF tracking error.
3. Overnight hedging when options markets are closed.
4. Short-term directional views on macro instruments.

### When NOT to use derivatives

- Pre-earnings gambling ("buying cheap OTM calls before earnings"). Forbidden — this is a lottery ticket.
- Weekly options as directional bets. Theta decay is too aggressive; these are for defined income strategies only.
- Naked short options. Never. The unlimited-risk profile violates every risk management principle.
- Complex multi-leg structures the agent cannot fully explain the P&L profile of. If unsure, use stock.
- Illiquid options (bid-ask spread > 10% of option price). Slippage destroys edge.

### Margin danger

Futures and short options use margin. Margin amplifies both gains and losses. Rules:

- **Never use more than 50% of available margin.** A margin call forces liquidation at the worst time.
- **Futures maintenance margin can change overnight.** Exchanges raise margin during volatility spikes. Keep a buffer.
- **Short options margin can expand if the position moves against you.** Monitor daily.
- **The agent treats margin as borrowed money that can be recalled at any time.** Size conservatively.

## Decision procedure

1. Identify the trade thesis (direction, magnitude, timeframe, catalyst).
2. Determine if derivatives add value vs. simply trading the underlying:
   - Does the thesis benefit from defined risk? (binary events → yes)
   - Is leverage needed within a risk cap? (high-priced stocks → yes)
   - Is income generation the goal? (covered calls, CSPs → yes)
   - Is hedging the goal? (protective puts → yes)
   - If none of the above → use the underlying stock.
3. Select the structure from `references/options-strategies.md`:
   - Bullish + low IV → long call or call debit spread.
   - Bullish + high IV → bull put spread (credit).
   - Bearish + low IV → long put or put debit spread.
   - Bearish + high IV → bear call spread (credit).
   - Neutral + high IV → iron condor.
   - Income + existing stock → covered call.
   - Income + cash + willingness to own → cash-secured put.
4. Size the position using max loss as the risk amount:
   - `max_loss = risk_budget` from `risk-management`.
   - For debit trades: `contracts = floor(risk_budget / (premium × 100))`.
   - For credit trades: `contracts = floor(risk_budget / ((width - credit) × 100))`.
5. Verify liquidity: bid-ask spread < 5% of mid price, open interest > 100.
6. Verify DTE: minimum 30 DTE for directional, 30-45 DTE for income/credit strategies.
7. Compute the Greeks (see `references/greeks.md`) and confirm they align with the thesis.
8. Execute via limit order at the mid price or better. Do not use market orders on options.
9. Set management rules (see `references/options-strategies.md` for each structure).

## Heuristics & thresholds

- **Defined risk only.** No naked shorts. No exceptions.
- **DTE >= 30 for all strategies.** Weekly options are prohibited for this agent.
- **IVR context matters.** Buy options when IV is low (< 30 IVR). Sell options when IV is high (> 50 IVR).
- **Liquidity floor:** bid-ask < 5% of mid, open interest > 100 on the strikes used.
- **Position size = max loss.** Never risk more than 1% of account on any single options structure.
- **No more than 3 options positions simultaneously.** Options require active management; too many positions leads to neglect.
- **Close at 50% profit on credit trades.** Do not hold to expiration hoping for full credit.
- **Close at 21 DTE on all positions.** Gamma risk accelerates inside 21 DTE.

## Common failure modes

- **Buying OTM options as lottery tickets.** Low probability, high loss rate. Forbidden.
- **Selling naked calls.** Unlimited loss. Absolutely forbidden.
- **Ignoring theta.** Buying options and holding through weekends without accounting for time decay.
- **Illiquid strikes.** Wide bid-ask means the position is underwater from entry.
- **Holding through expiration.** Pin risk, assignment risk, after-hours moves. Close before.
- **Not understanding assignment.** Short options can be assigned early. Know the cash requirements.
- **Over-leveraging with futures.** A single ES contract controls ~$250k notional. Respect the size.

## Outputs expected

```json
{
  "skill": "derivatives-options-and-futures",
  "instrument_type": "option" | "future",
  "structure": "long_call" | "call_debit_spread" | "iron_condor" | etc.,
  "underlying": "AAPL",
  "contracts": 2,
  "strikes": [180, 185],
  "expiration": "2026-05-15",
  "dte": 33,
  "max_loss": 450.00,
  "max_gain": 550.00,
  "breakeven": 182.25,
  "iv_rank": 22,
  "bid_ask_spread_pct": 0.03,
  "greeks": {"delta": 0.45, "theta": -0.12, "vega": 0.08, "gamma": 0.03},
  "management_rules": "Close at 50% profit or 21 DTE, whichever comes first",
  "risk_budget_used": 450.00,
  "notes": "..."
}
```

## References (lazy-load)

- `references/greeks.md` — Delta, Gamma, Theta, Vega, Rho explained with numeric examples.
- `references/options-strategies.md` — all allowed structures with entry/exit/management rules.
- `references/futures-basics.md` — contract specs, margin, rollover, settlement.

## Cross-links

- Pairs with: `risk-management` (max-loss sizing), `technical-indicators` (IV rank), `trading-strategies-playbook` (directional thesis source).
- Feeds: `buy-sell-hold-decision` (derivative X/Y/Z), `order-types-execution` (limit orders on options).
- Defers to: `safety-and-kill-switch` (margin call risk), `regulations-and-tax-awareness` (options approval level, wash sale on options).

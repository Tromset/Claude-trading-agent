---
name: order-types-execution
description: Use when the agent has a proposed X or Y and must pick the correct order type, time-in-force, and routing instruction to send. Covers MARKET/LIMIT/STOP/STOP_LIMIT/TRAILING/OCO/OTO/auction orders, TIF, brackets, and short-sale handling.
---

# Order Types & Execution

Given a decision to buy or sell, *how* that order is represented matters as much as whether to trade. The wrong order type can turn a profitable setup into a loss through slippage, missed fills, or unintended market exposure. This skill picks the right tool.

## When to use this skill

- After `buy-sell-hold-decision` has proposed `X` or `Y` but before the order is actually sent.
- When attaching protective stops / targets to a new entry (bracket / OCO).
- When the microstructure output from `market-microstructure` indicates the default order type is inappropriate.
- When shorting an equity and a locate is required.
- When placing an auction order (MOO/MOC/LOO/LOC) in the auction window.

**Anti-triggers:** do NOT use this skill to *decide* whether to trade. Order type is execution, not analysis.

## Prerequisites

- A valid sizing + stop + target from `risk-management`.
- Microstructure snapshot from `market-microstructure` (spread, depth, session phase, halt state).
- A confirmed account type that supports the intended order type (from `broker-and-platform-selection`).

## Core concepts

### Order type catalog

| Type | Definition | Fill guarantee | Price guarantee |
|---|---|---|---|
| `MARKET` | Buy/sell immediately at best available price | Yes | No |
| `LIMIT` | Buy at ≤ limit, sell at ≥ limit | No | Yes |
| `STOP` (stop-loss / stop-market) | Becomes a MARKET order once stop price is touched | Yes (after trigger) | No |
| `STOP_LIMIT` | Becomes a LIMIT order once stop price is touched | No | Yes |
| `TRAILING_STOP` | Stop that trails by a fixed $ or % as price moves favorably | Yes (after trigger) | No |
| `TRAILING_STOP_LIMIT` | Trailing stop that becomes a limit | No | Yes |
| `MARKETABLE_LIMIT` | A LIMIT at or through the far touch — behaves like a MARKET with a worst-price cap | Usually | Cap only |
| `MOO` | Market on Open — market order executed in the opening auction | Yes | No |
| `LOO` | Limit on Open — limit order in the opening auction | Only if crosses | Yes |
| `MOC` | Market on Close — market in the closing auction | Yes | No |
| `LOC` | Limit on Close — limit in the closing auction | Only if crosses | Yes |
| `OCO` | One-Cancels-Other — a pair of orders; a fill on either cancels the other | n/a | n/a (wrapper) |
| `OTO` | One-Triggers-Other — a parent order that, once filled, activates a child | n/a | n/a (wrapper) |
| `BRACKET` | Entry + stop + target, typically OTO entry that activates an OCO (stop, target) | n/a | n/a (wrapper) |
| `PEGGED` | Order pegged to bid/ask/mid (broker-dependent) | Depends | Partial |

Not every broker supports every type. The agent must never assume a type is available without confirming support (see `broker-and-platform-selection`).

### Time in force (TIF)

| TIF | Meaning | Typical use |
|---|---|---|
| `DAY` | Expires at session close if unfilled | Intraday work, default for most retail orders |
| `GTC` | Good-till-cancelled (broker cap, often 60–180 days) | Swing/position entries, long-horizon limits |
| `IOC` | Immediate-or-cancel; any unfilled remainder is cancelled | Liquidity-taking slices that must not rest |
| `FOK` | Fill-or-kill; entire qty must fill immediately or nothing | Block-style clean fill requirement |
| `EXT` / `DAY+` | Includes extended-hours sessions | Only when strategy explicitly trades ETH |
| `GTD` | Good-till-date (specific date) | Calendar-bound setups |
| `OPG` | On-opening only (for LOO) | Opening auction participation |

A bare `LIMIT` without a TIF is ambiguous and forbidden. Every order spec must carry both `order_type` and `time_in_force`.

### When to use each order type

- **MARKET** — when (a) liquidity is deep enough that spread + walked price is negligible vs the trade's reward-per-share, (b) speed matters more than price, and (c) the agent is in the middle of RTH on a liquid name. Default *forbidden* in pre-/post-market, during auctions, on thin names, or inside news windows.
- **LIMIT** — the default for everything else. Entries on pullbacks, exits at targets, thin names, pre-/post-market, wide spreads. Trade: may not fill.
- **MARKETABLE LIMIT** — when the agent wants a market-like fill but needs a worst-price cap (e.g., "fill now, but not worse than mid + 5 bps"). This is the *preferred* MARKET replacement on retail platforms — almost never use a bare MARKET.
- **STOP (stop-market)** — protective stop on an open position. Set and forget. Trade: in a gap or flash crash, fills may be far beyond the stop price. Never use a bare STOP on a thin name or overnight.
- **STOP_LIMIT** — protective stop where slippage is worse than a missed exit (e.g., crypto with sudden wicks the agent will ride through). Risk: the limit may not fill at all in a real break, leaving the position naked. Generally not recommended as the *only* stop — pair with a time stop or a wider disaster stop.
- **TRAILING_STOP** — locking in profit on a trending position. Trail distance = 1.5–2× ATR or the swing-low rule. Do not trail tighter than noise.
- **OCO** — pairing a stop-loss with a target limit on the same position. Fill either → the other cancels automatically. Required on all open positions unless the broker offers a native bracket.
- **OTO** — "enter on a breakout, then place a stop once filled." Automates the entry + protection sequence.
- **BRACKET** — entry + OCO exit in a single spec. The preferred structure for *any* planned trade — it makes the trade's risk visible at submission time.
- **MOO / LOO** — when the strategy is an opening-auction strategy (gap-and-go, opening-range break with auction entry). Rare; confirm the broker routes to the exchange auction.
- **MOC / LOC** — end-of-day rebalances, closing-print benchmark trades, and "hold into the close" exits that want the highest-liquidity print. Submit before the 15:50 ET imbalance publication for best treatment.

### Short-sale locate

For equities, shorting requires the broker to **locate** the shares to borrow. Steps:
1. Check if the symbol is on the Easy-to-Borrow (ETB) list — instant locate, no extra cost.
2. If not, request a Hard-to-Borrow (HTB) locate; fees can be 1–100%+ annualized depending on demand.
3. A locate is good for the trading day; an overnight hold may require a re-locate or be subject to a forced buy-in.
4. SSR (short-sale restriction, aka "uptick rule" post-Reg SHO 201): triggered by a −10% intraday move; once on, shorts must be entered at a price above the NBB, not at or below. Affects a whole trading day plus next.

If the agent cannot confirm a locate before submitting a short → `Z`.

### Slippage implications by order type

- **MARKET** — worst slippage in stressed conditions; zero risk of non-fill.
- **LIMIT** — zero slippage if filled; risk is not getting filled (opportunity cost).
- **STOP** — slippage of the gap between trigger and first available fill; in a flash crash this can be catastrophic.
- **STOP_LIMIT** — zero slippage if filled after trigger; risk is the position running past your limit and leaving you unhedged.
- **TRAILING_STOP** — same slippage profile as STOP, but the trigger moves with price.
- **AUCTION (MOO/MOC/LOO/LOC)** — filled at the auction clearing price; slippage depends on imbalance and your direction.

## Decision procedure

1. Receive the proposed action from `buy-sell-hold-decision`: `X` or `Y`, ticker, direction, qty, entry/stop/target.
2. Read the microstructure snapshot: session phase, spread, depth, halt state.
3. Select the **entry** order type using the decision rules below (and the table in `references/order-type-matrix.md`):
   - Liquid, RTH, not near auction, executing now → MARKETABLE_LIMIT (preferred) or LIMIT at the bid/ask.
   - Liquid, entering on a specific level → LIMIT at that level.
   - Wants opening/closing print → LOO/MOO or LOC/MOC.
   - Thin, wide spread, or ETH → LIMIT with a price improvement attempt; no MARKET.
   - Breakout above level with confirmation → STOP_LIMIT above the level (stop trigger = the level, limit = level + tolerance).
4. Select the **stop** order type:
   - Default: STOP (stop-market) for US equities on liquid names with DAY or GTC.
   - STOP_LIMIT only when the agent explicitly prefers non-fill to bad fill and has a backup disaster stop.
   - TRAILING_STOP only after the trade is ≥ 1R in profit.
5. Select the **target** order type:
   - LIMIT at the target price with GTC (or DAY if intraday).
   - LOC if the target is "exit on the close."
6. Wrap the stop + target in OCO (or native BRACKET) so one fill cancels the other.
7. Set TIF per the intent: DAY for intraday work, GTC for swing/position, IOC/FOK only when explicitly needed.
8. For shorts: confirm locate status and SSR state before finalizing.
9. Verify the resulting order spec matches the `risk-management` output exactly (qty, stop, target).
10. Pass the finalized order spec back to `buy-sell-hold-decision` for inclusion in the X/Y payload.

## Heuristics & thresholds

- **Default to LIMIT, not MARKET.** A bare MARKET order on a retail platform is almost always a mistake.
- **Never a bare MARKET in ETH, at the open (09:30–09:32 ET), or inside ±5 min of a high-impact news print.**
- **Stop-limit only with a backup.** If used alone, add a disaster stop wider away as insurance.
- **Bracket everything.** Every new entry leaves the door with both a stop and a target, attached.
- **Trailing stops only in profit.** Trailing a losing position tightens the loss — forbidden.
- **GTC for swings, DAY for intraday.** Crossed wires cause phantom entries hours later.
- **Auction orders must be in before imbalance publication** (15:50 ET for the close, 09:28 ET for the open) or participation is not guaranteed.
- **Short without a confirmed locate → Z.** Always.

## Common failure modes

- **Naked MARKET at the open.** First-tick slippage on a liquid name can be 20+ bps at 09:30:00.
- **Stop-limit with no escape.** Price gaps through the limit; position remains open and grows the loss.
- **Missing TIF.** Broker default may be GTC when you expected DAY, leaving a live order overnight.
- **Unbracketed entry.** Filled, then the agent gets distracted, then no stop → unbounded risk.
- **Trailing too tight.** Normal pullback wicks out the trail before the trend resumes.
- **Wrong auction window.** MOO sent after 09:28 ET imbalance start may not participate.
- **Short without locate confirmation.** Broker rejects or silently fails; agent thinks it is short and is not.
- **Assuming OCO across accounts or sub-accounts.** Some platforms only OCO within a single working list.

## Outputs expected

```json
{
  "skill": "order-types-execution",
  "action": "X",
  "ticker": "NASDAQ:AAPL",
  "side": "BUY",
  "qty": 119,
  "order_type": "LIMIT",
  "entry_price": 182.05,
  "time_in_force": "DAY",
  "bracket": {
    "stop_type": "STOP",
    "stop_price": 177.80,
    "stop_tif": "GTC",
    "target_type": "LIMIT",
    "target_price": 192.00,
    "target_tif": "GTC",
    "relation": "OCO"
  },
  "short_locate": null,
  "rationale": "Liquid name, RTH midday, entering on pullback to level; marketable-limit not needed.",
  "spec_matches_risk_management": true
}
```

This spec is the exact payload `buy-sell-hold-decision` inserts into its `X` or `Y` output. If `spec_matches_risk_management = false` → downgrade to `Z`.

## References (lazy-load)

- `references/order-type-matrix.md` — long table mapping situation → recommended order type with rationale and examples.
- `references/tif-reference.md` — all TIFs with broker-compatibility notes.
- `references/short-sale-locate.md` — locate request flow, SSR table, borrow-fee impact.
- `references/bracket-templates.md` — broker-by-broker bracket order recipes.

## Cross-links

- Pairs with: `market-microstructure` (informs the choice), `risk-management` (sizing + stop source of truth), `broker-and-platform-selection` (which order types are actually available), `buy-sell-hold-decision` (consumer of the final spec), `safety-and-kill-switch` (kill-exits use MARKET by exception).

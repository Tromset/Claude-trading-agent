---
name: market-microstructure
description: Use when the agent needs to reason about the order book, spreads, depth, slippage, or auction mechanics before choosing an order type or sizing a trade. Covers Level 2, maker/taker, routing, and halts.
---

# Market Microstructure

How orders actually meet. Price on a chart is an output of a matching engine — this skill explains the matching engine. The agent uses it to predict fill quality, estimate slippage, and avoid microstructure traps (halts, wide spreads, thin depth).

## When to use this skill

- Before choosing an order type in `order-types-execution`.
- When Level 2 / depth-of-book is visible on the screen and must be interpreted.
- When the spread or quoted size looks anomalous vs historical norms.
- When a trade is near the open auction, close auction, or a halt/LULD band.
- When slippage on a prior trade exceeded the modeled estimate.

**Anti-triggers:** do NOT use this skill to find trade ideas or analyze chart patterns. Microstructure informs *how* to execute, not *whether* to trade.

## Prerequisites

- `trading-fundamentals` has identified asset class, venue, and session.

## Core concepts

### The order book (Level 2)

A sorted list of resting limit orders at each price.

- **Bid side:** buyers, sorted highest price first (best bid at top).
- **Ask (offer) side:** sellers, sorted lowest price first (best ask at top).
- **NBBO:** National Best Bid and Offer — the tightest published bid/ask across venues (US equities).
- **Level 1:** best bid + best ask + last trade. Enough for most retail decisions.
- **Level 2 (MBP — market by price):** aggregated size at each price level, per venue or consolidated.
- **Level 3 / MBO (market by order):** every individual order. Rarely exposed to retail.

### Bid, ask, mid, spread

- `bid` = highest price a buyer is willing to pay.
- `ask` = lowest price a seller is willing to accept.
- `mid` = `(bid + ask) / 2`. Fair-value reference, not a tradeable price.
- `spread` = `ask − bid`. The transactional friction cost of a round trip.
- `spread_bps` = `spread / mid × 10000`. Comparable across price levels.

Typical resting spreads (mid-day RTH):
- Mega-cap US equity: 1 cent ≈ 0.5–3 bps.
- Mid-cap US equity: 1–5 cents ≈ 5–20 bps.
- Small-cap: 5–25 cents ≈ 20–100 bps.
- ES futures: 1 tick (0.25 pts ≈ 1.25 bps).
- EUR/USD spot: 0.1–1 pip (0.1–1 bps at retail).
- BTC spot (Tier-1 CEX): 1–5 bps.

### Depth

Total resting size within the first N price levels. Thin depth → a market order eats multiple levels → slippage. The agent estimates **walked price** before sending a marketable order:

```
walked_price ≈ sum(size_i × price_i) / qty   for levels consumed in sequence
```

If the proposed qty exceeds top-of-book size by > 3× → use a LIMIT, not a MARKET.

### Makers and takers

- **Maker:** posts a resting order (limit order not immediately executable). Adds liquidity. Usually rebated or charged a lower fee.
- **Taker:** sends a marketable order that executes against a resting order. Removes liquidity. Usually charged the higher fee.
- **Maker/taker fee model** (most US equity exchanges, crypto CEXs): e.g., −0.20 bps rebate to maker, +0.30 bps fee to taker. Net 0.10 bps to the exchange.
- **Inverted venues** (EDGA, BYX): pay the taker, charge the maker — used for specific routing strategies.

### Order routing

A retail order does not necessarily touch a lit exchange. Common paths:

1. **Internalizer / wholesaler** — Citadel Securities, Virtu, G1X, Jane Street. Fills at NBBO or better, pays the broker PFOF (Payment for Order Flow) in US equities where allowed. Zero-commission brokers rely on this.
2. **Exchange (lit)** — ARCA, NASDAQ, NYSE, BATS, EDGX, IEX, etc. Transparent book, price-time priority.
3. **ATS / dark pool** — off-exchange venues that do not display quotes. Match at midpoint or NBBO. Used for large institutional orders.
4. **SOR (smart order router)** — broker-side logic that fragments and routes slices to multiple venues for best price + lowest fees.

The agent generally does not control routing on a screenshot-driven retail platform. It must assume a PFOF-style internalization path unless told otherwise.

### Price-time priority

Within a price level on a lit book: **first in, first out (FIFO)**. Older resting orders fill before newer ones at the same price. Some venues use pro-rata (options, futures) — size matters more than time.

Implication: posting a limit at the back of the queue may not fill at all even if price touches the level.

### Dark pools and internalizers

- **Dark pool:** no pre-trade transparency. Orders match at midpoint or NBBO, then print to the tape after execution.
- **Internalizer:** a single firm that fills its own customer flow against its inventory.
- For retail via PFOF: the internalizer promises NBBO or better at the moment of receipt. Studies show meaningful price improvement on liquid names; less so on illiquid.
- The retail agent sees the *outcome* (fill price) but not the *path*. That is fine for decisions that only depend on the fill price.

### Latency (brief)

- Light travels ~200 km / ms through fiber.
- Co-located HFT reacts in microseconds. Retail round-trips are typically 20–500 ms.
- A screenshot-driven agent operates at human-perception speeds — hundreds of milliseconds to seconds per cycle. It CANNOT compete on latency and must avoid strategies that require it.

### Slippage (why fills differ from expectations)

Primary causes:
1. Spread (the first tick you always pay on a marketable order).
2. Depth consumption (eating multiple levels).
3. Adverse selection (the market moves while your order is in flight).
4. Venue routing delay (internalizer hops).
5. Wide spreads at session edges (open/close, halts, news).
6. Stop orders becoming market orders during gaps.

**Slippage budget:** model expected slippage = spread/2 + (qty/top_book_size) × spread. If actual > 2× modeled → log and recalibrate.

### Iceberg and hidden orders

- **Iceberg:** a large order that displays only a small "tip" of its total size; as the tip fills, the next slice becomes visible.
- **Hidden / non-displayed:** entirely invisible on the public book; may still execute if a marketable order crosses it.
- Implication: visible depth ≠ true depth. A thin-looking book may hide size; a deep-looking book may be layered with spoofing (illegal but not eliminated).

### Auctions (opening and closing)

- **Opening auction (09:30 ET for US equities):** a single-price cross. Imbalance messages start at 09:28 ET. MOO / LOO orders participate. The resulting print is the "open" of the day.
- **Closing auction (16:00 ET):** higher volume than the open on most names. Imbalance messages begin at 15:50 ET. MOC / LOC orders participate. Benchmarked by passive funds — the highest-liquidity print of the day.
- The continuous book resumes immediately after the auction cross.

### Halts and LULD (Limit Up / Limit Down)

- **LULD bands:** dynamic price bands (typically ±5% for Tier 1 stocks ≥ $3, wider for lower-priced names). If the NBBO touches a band for 15 seconds, a 5-minute trading pause is triggered.
- **News halts (T1, T2, T12):** issuer-requested or regulator-requested pauses pending material information.
- **Volatility halts / circuit breakers:** market-wide Level 1 (−7%), Level 2 (−13%), Level 3 (−20%) on SPX vs prior close.
- **Behavior during a halt:** no trading; orders may be cancelled/modified depending on venue. The reopen is an auction cross with possible large gaps.

The agent must NOT attempt to trade a halted instrument. Halts → `Z` and `safety-and-kill-switch` engagement.

### HFT is out of scope

High-frequency trading — latency-arbitrage, quote-stuffing, rebate farming, statistical market making at microsecond resolution — is **out of scope for a screenshot-driven agent**. The agent cannot observe or react inside the time window where HFT operates. It must select strategies whose edge survives at human timescales (seconds to days) and assume it is always the slowest participant in any interaction with the book. Any playbook that requires "being first" is forbidden.

## Decision procedure

1. Identify Level 1 from the screen: best bid, best ask, last, volume.
2. If Level 2 is visible, note top-of-book size on both sides and total displayed depth in the first 5 levels.
3. Compute `spread` and `spread_bps`. Compare to the 20-day average for the instrument (if known).
4. Classify liquidity:
   - Tight spread + deep book → liquid → any order type is viable.
   - Tight spread + thin book → beware market orders; use limit.
   - Wide spread → either session edge, low-volume name, or news → downgrade size or skip.
5. Check for halt / LULD indicators on the screen (paused text, status badges, gray book). If halted → abort, emit `Z`.
6. Check session context (from `trading-fundamentals`): near open/close auction? Use MOO/LOO/MOC/LOC if the intent matches.
7. Estimate slippage for the intended qty. If estimate > 20% of the reward per share → skip or resize.
8. Emit the microstructure output JSON for the execution skill to consume.

## Heuristics & thresholds

- Spread > 3× 20-day average for the instrument → soft kill, do not take with a market order.
- Top-of-book size < intended qty / 3 → use LIMIT, not MARKET.
- First 5 levels of depth < intended qty → expect multi-tick slippage; split the order or skip.
- Within ±2 minutes of the opening auction (09:30–09:32 ET) → avoid market orders; spreads widest and prints unstable.
- Last 5 minutes before the closing auction (15:55–16:00 ET) → prefer MOC/LOC if intent is the closing print; otherwise be cautious with mid-session logic.
- On a LULD pause reopen → wait at least one full minute of continuous trading before acting.
- If Level 2 visibly thickens and thins within the same second (flicker) → likely spoof / layering → treat depth as unreliable.

## Common failure modes

- **Trusting displayed depth in thin names.** Depth can vanish the instant you send a taker order.
- **Using market orders at the open.** The first 30–120 seconds is the worst time for a marketable order.
- **Chasing spread.** Keeping a limit order and nudging it by one tick every few seconds until you become a taker anyway — just take it cleanly or walk away.
- **Ignoring auction imbalances.** A large closing imbalance published at 15:50 ET often moves the book in the 10 minutes before the cross.
- **Treating dark liquidity as reachable.** A retail agent cannot route directly to most dark venues.
- **Competing with HFT.** A screenshot agent will always lose the race. Choose strategies where microseconds do not matter.

## Outputs expected

```json
{
  "skill": "market-microstructure",
  "ticker": "NASDAQ:AAPL",
  "bid": 182.03,
  "ask": 182.05,
  "mid": 182.04,
  "spread": 0.02,
  "spread_bps": 1.1,
  "spread_vs_20d_avg": 1.0,
  "top_bid_size": 1200,
  "top_ask_size": 900,
  "depth_first_5_levels": 18500,
  "session_phase": "RTH-midday",
  "halt_state": "none",
  "luld_near": false,
  "estimated_slippage_bps": 0.8,
  "recommended_order_flavor": "LIMIT at ask (marketable limit) or MARKET",
  "notes": "Liquid; normal conditions"
}
```

If conditions are abnormal (wide spread, thin depth, halt), `recommended_order_flavor` guides `order-types-execution`, and any resulting proposal that ignores the guidance should be downgraded to `Z` by `buy-sell-hold-decision`.

## References (lazy-load)

- `references/level-2-reading.md` — annotated screenshots of typical Level 2 views per platform.
- `references/auction-mechanics.md` — opening and closing cross walkthroughs.
- `references/luld-and-halts.md` — full band table, halt codes, reopen procedures.
- `references/slippage-model.md` — derivation and worked examples.

## Cross-links

- Pairs with: `order-types-execution` (consumer of the recommendation), `trading-fundamentals` (session context), `risk-management` (slippage affects realized stop distance), `safety-and-kill-switch` (halts and wide-spread soft kills), `buy-sell-hold-decision` (may downgrade to Z on microstructure warnings).

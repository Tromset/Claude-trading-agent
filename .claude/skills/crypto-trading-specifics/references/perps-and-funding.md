# Perpetual Futures & Funding Rates

## What Are Perpetual Futures

Perpetual futures ("perps") are futures contracts with **no expiration date**. Unlike traditional futures (which expire quarterly), perps can be held indefinitely. They are the most traded derivative in crypto — daily perp volume often exceeds spot volume by 3–5×.

### Key Mechanics

| Feature | Traditional Futures | Perpetual Futures |
|---|---|---|
| Expiry | Fixed date (e.g., March, June) | None — hold forever |
| Settlement | At expiry (cash or physical) | Continuous via funding mechanism |
| Price convergence | Converges to spot at expiry | Forced via funding rate |
| Roll required | Yes (before expiry) | No |

## Mark Price vs Index Price

- **Index price:** weighted average of spot prices across major exchanges. Represents "true" market value.
- **Mark price:** the price used to calculate unrealized P&L and liquidation. Based on index price + decaying basis.
- **Last traded price:** the most recent fill price on this exchange.

**Why it matters:** liquidation is based on **mark price**, not last traded price. This prevents "scam wicks" (brief, manipulated price spikes on one exchange) from liquidating positions unfairly.

## The Funding Rate Mechanism

Funding is the mechanism that keeps perp prices anchored to spot prices. Every 8 hours (on most exchanges), one side pays the other:

### How It Works

1. If perp price > index price (premium): **longs pay shorts**. This discourages longs and encourages shorts, pushing the perp price down toward spot.
2. If perp price < index price (discount): **shorts pay longs**. This discourages shorts and encourages longs, pushing the perp price up toward spot.

### Funding Rate Formula (simplified)

```
funding_payment = position_notional × funding_rate
```

Where:
- `position_notional = qty × mark_price`
- `funding_rate` is typically expressed as a percentage per 8-hour period

### Funding Rate Cycles

Most exchanges settle funding every **8 hours** at fixed times:
- 00:00 UTC
- 08:00 UTC
- 16:00 UTC

Some exchanges (e.g., dYdX) use continuous hourly funding.

### Numerical Example

```
Position: LONG 1 BTC-USDT at mark price $65,000
Funding rate: +0.01% (positive → longs pay shorts)
Position notional: 1 × $65,000 = $65,000

Funding payment per period: $65,000 × 0.0001 = $6.50
Per day (3 periods): $6.50 × 3 = $19.50
Per year: $19.50 × 365 = $7,117.50 (annualized: 10.95%)
```

If funding is **negative** (-0.01%), the LONG receives $6.50 per period from shorts.

### Funding Rate as Sentiment Indicator

| Funding Rate | Meaning | Agent Interpretation |
|---|---|---|
| Highly positive (> +0.05%) | Longs crowded, paying premium | Contrarian bearish — longs overcrowded |
| Moderately positive (+0.01% to +0.05%) | Normal bullish market | Neutral |
| Near zero (±0.005%) | Balanced | Neutral |
| Moderately negative (-0.01% to -0.05%) | Shorts crowded, paying premium | Contrarian bullish — shorts overcrowded |
| Highly negative (< -0.05%) | Extreme fear, heavy shorting | Strong contrarian bullish signal |

**Caution:** Funding can stay extreme for extended periods. It's a supporting indicator, not a primary signal.

## Funding Rate Arbitrage

A delta-neutral strategy exploiting funding:

1. **Go long spot** (buy and hold the actual coin).
2. **Go short perp** (open a short perp of equal size).
3. Net market exposure: zero (delta neutral).
4. If funding is positive → the short perp position receives funding from longs.
5. Profit = funding received, with zero directional risk.

**Risks of funding arb:**
- Funding can flip negative → strategy starts losing.
- Exchange risk (capital locked on exchange).
- Liquidation risk on the short perp if price rises sharply (need sufficient margin).
- Transaction costs (opening/closing both legs, withdrawal fees).

**Agent rule:** funding arb is noted for understanding, not for execution by this agent (it requires continuous monitoring and capital management beyond screenshot-based operation).

## Liquidation Mechanics

When a leveraged position moves against the trader enough to consume the margin, the exchange forcibly closes the position.

### Maintenance Margin

- **Initial margin:** the margin required to open a position. `initial_margin = position_notional / leverage`.
- **Maintenance margin:** the minimum margin to keep the position open. Typically 0.5%–1% of position notional (varies by exchange and tier).

### Liquidation Price Formula (simplified, for LONG)

```
liquidation_price = entry_price × (1 - 1/leverage + maintenance_margin_rate)
```

### Worked Example

```
Entry: LONG 1 BTC at $65,000
Leverage: 10×
Initial margin: $65,000 / 10 = $6,500
Maintenance margin rate: 0.5%

Liquidation price = $65,000 × (1 - 1/10 + 0.005)
                  = $65,000 × (1 - 0.1 + 0.005)
                  = $65,000 × 0.905
                  = $58,825

A 9.5% drop from entry → liquidated → lose entire $6,500 margin.
```

### Cascade Liquidations

When a large position is liquidated, the forced sale/buy can push the price further, triggering more liquidations. This creates a cascade:

1. Price drops → leveraged longs liquidated.
2. Liquidation = forced market sell → pushes price down further.
3. More liquidations triggered → more forced sells.
4. Price crashes rapidly (a "liquidation cascade" or "long squeeze").

The reverse happens in a short squeeze (price spikes, shorts liquidated, forced buys push price higher).

**Agent impact:** cascade liquidations cause extreme volatility. If the agent sees a sharp unidirectional move with rapidly increasing volume, it should suspect a liquidation cascade and NOT enter counter-trend.

## Agent Leverage Rules

| Rule | Limit | Rationale |
|---|---|---|
| **Maximum leverage** | 3× | Even with proper stops, crypto volatility + slippage can cause losses beyond planned risk at higher leverage |
| **Recommended leverage** | 1×–2× | Behaves closer to spot trading with slightly enhanced returns |
| **Never** | > 3× | Regardless of what the exchange allows (some offer 100×+) |

### Why 3× Max

At 3× leverage with a $65,000 BTC entry:
- Initial margin: $21,667
- Liquidation at ~$44,200 (32% drop) — gives significant room
- A 5% stop-loss costs 15% of margin — manageable

At 10× leverage:
- Initial margin: $6,500
- Liquidation at ~$58,825 (9.5% drop) — normal BTC daily range can approach this
- A 5% stop-loss costs 50% of margin — devastating

At 50× leverage:
- Liquidation at ~$63,700 (2% drop) — normal intraday noise
- Essentially gambling

## Cross Margin vs Isolated Margin

| Mode | How it works | Risk | Agent rule |
|---|---|---|---|
| **Cross margin** | Entire account balance serves as margin for all positions | One bad position can drain the entire account | NEVER use |
| **Isolated margin** | Only the allocated margin is at risk for each position | Loss limited to the margin allocated to that position | ALWAYS use |

**Agent hard rule:** always use **isolated margin**. Cross margin means a single liquidation can wipe the entire account. Isolated margin limits the damage to the margin allocated to that specific position.

## Insurance Funds

Exchanges maintain insurance funds to cover socialized losses:

1. When a position is liquidated, if the liquidation price is better than the bankruptcy price → the excess goes to the insurance fund.
2. When a position is liquidated and the loss exceeds the trader's margin → the insurance fund covers the deficit.
3. If the insurance fund is depleted → "auto-deleveraging" (ADL) — profitable traders on the other side have their positions partially closed to cover the loss.

**Agent implication:** ADL is rare but real. During extreme events, even a profitable position can be partially closed by the exchange. This is an inherent risk of leveraged crypto trading.

## Summary Table

| Concept | Key Number | Agent Rule |
|---|---|---|
| Funding frequency | Every 8 hours | Check funding before opening perp positions |
| High funding threshold | > |0.05%| per period | Contrarian warning for the crowded side |
| Max leverage | 3× | Hard cap, no exceptions |
| Margin mode | Isolated only | Never cross margin |
| Liquidation buffer | Keep position size so liquidation is > 2× ATR(14) away | Prevents noise-triggered liquidation |
| Funding cost awareness | Annualize the rate before holding | +0.03%/8h = 32.85%/year cost |

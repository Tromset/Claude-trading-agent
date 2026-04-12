# Futures Basics

Reference for understanding futures contracts. The agent primarily trades equities but needs futures literacy for macro context, hedging awareness, and understanding index futures (ES, NQ) that drive pre-market sentiment.

## What Are Futures

A futures contract is a **standardized agreement** to buy or sell a specific quantity of an asset at a predetermined price on a specific future date. Unlike options, both buyer and seller are **obligated** to fulfill the contract at expiration.

- **Buyer (long):** obligated to buy the asset at the agreed price at expiry.
- **Seller (short):** obligated to sell/deliver the asset at the agreed price at expiry.
- **Standardized:** exchange-defined contract size, tick size, expiry dates, delivery terms.
- **Leveraged:** controlled via margin (a fraction of the notional value), not full payment upfront.

## Contract Specifications

Every futures contract has these specifications:

| Field | Description | Example (ES — E-mini S&P 500) |
|---|---|---|
| Underlying | Asset being traded | S&P 500 Index |
| Contract size (multiplier) | Value per point of the index/commodity | $50 per point |
| Tick size | Minimum price increment | 0.25 points |
| Tick value | Dollar value of one tick | $12.50 (0.25 × $50) |
| Notional value | Full value of one contract | ~$262,500 (at 5250 × $50) |
| Expiry months | When contracts expire | Mar (H), Jun (M), Sep (U), Dec (Z) |
| Settlement | How contracts settle at expiry | Cash settled |
| Trading hours | When trading occurs | Nearly 24h (Sun 6pm – Fri 5pm ET, with daily halt 5–6pm) |

## Key Futures Markets

| Symbol | Name | Multiplier | Tick | Tick Value | Settlement | Use Case |
|---|---|---|---|---|---|---|
| **ES** | E-mini S&P 500 | $50/pt | 0.25 | $12.50 | Cash | Broad market direction, hedging |
| **NQ** | E-mini Nasdaq 100 | $20/pt | 0.25 | $5.00 | Cash | Tech-heavy market direction |
| **YM** | E-mini Dow | $5/pt | 1.00 | $5.00 | Cash | Blue-chip direction |
| **RTY** | E-mini Russell 2000 | $50/pt | 0.10 | $5.00 | Cash | Small-cap sentiment |
| **CL** | Crude Oil (WTI) | $1,000/contract | 0.01 | $10.00 | Physical | Energy, inflation proxy |
| **GC** | Gold | $100/oz | 0.10 | $10.00 | Physical | Safe haven, inflation hedge |
| **SI** | Silver | $5,000/contract | 0.005 | $25.00 | Physical | Precious metals |
| **ZB** | 30-Year Treasury Bond | $1,000/pt | 1/32 | $31.25 | Physical | Interest rate direction |
| **ZN** | 10-Year Treasury Note | $1,000/pt | 1/64 | $15.625 | Physical | Yield curve |
| **6E** | Euro FX | $125,000/contract | 0.00005 | $6.25 | Physical | EUR/USD direction |

**Micro contracts** (MES, MNQ, etc.) are 1/10th the size of their E-mini counterparts — better for smaller accounts.

## Margin

Futures use margin, not full payment:

| Margin Type | Definition | Example (ES) |
|---|---|---|
| **Initial margin** | Deposit required to open a position | ~$15,400 |
| **Maintenance margin** | Minimum equity to hold the position | ~$14,000 |
| **Variation margin** | Daily mark-to-market gains/losses | Credited/debited daily |

- If account equity drops below maintenance margin → **margin call** → must deposit more funds or positions are liquidated.
- Futures leverage is inherent: controlling ~$262,500 notional (ES) with ~$15,400 margin ≈ 17:1 leverage.
- **This agent's rule:** never trade futures with effective leverage > 3:1 for any single position.

## Mark-to-Market (Daily Settlement)

Futures positions are **settled daily** — unrealized P&L is converted to realized P&L every day at the settlement price.

1. At market close, the exchange calculates the settlement price.
2. Gains are credited to the long's account; losses are debited (and vice versa for shorts).
3. Both margin accounts are adjusted.
4. Process repeats daily until the position is closed or the contract expires.

**Implication:** a futures position can generate cash flow (positive or negative) every single day, unlike equities where P&L is unrealized until you sell.

## Futures vs Spot Pricing

### Basis

```
basis = futures_price - spot_price
```

- **Positive basis (contango):** futures > spot. Normal for most financial futures (accounts for cost of carry: interest, storage).
- **Negative basis (backwardation):** futures < spot. Common in commodities with high convenience yield or supply shortages.

### Cost of Carry Model

Theoretical futures price:

```
F = S × e^((r - d) × t)
```

Where:
- `F` = fair futures price
- `S` = current spot price
- `r` = risk-free interest rate
- `d` = dividend yield (for index futures) or storage cost offset
- `t` = time to expiration (in years)
- `e` = Euler's number

**Example:** S&P 500 at 5250, r = 5.3%, d = 1.3%, 90 days to expiry:
```
F = 5250 × e^((0.053 - 0.013) × 0.2466) = 5250 × e^(0.00986) = 5250 × 1.00991 ≈ 5302
```

### Contango and Backwardation

| State | Futures vs Spot | When it occurs | Impact on rolling |
|---|---|---|---|
| **Contango** | Futures > Spot | Normal for financial futures, stored commodities | Rolling costs money (sell low, buy high) |
| **Backwardation** | Futures < Spot | Supply shortages, high convenience yield | Rolling earns money (sell high, buy low) |

## Futures Roll

Futures contracts expire. To maintain a continuous position, traders **roll** — close the expiring contract and open the next one.

**Roll process:**
1. Identify the current "front month" contract (nearest expiry, most liquid).
2. As expiry approaches (typically 1–2 weeks before), liquidity shifts to the next contract.
3. Close the front-month position.
4. Open an equivalent position in the next contract.
5. The price difference between contracts is the **roll cost/benefit**.

**Roll calendar (quarterly index futures):**
- March (H) → June (M) → September (U) → December (Z)
- Roll typically happens on the second Thursday of the expiry month ("roll week").

## Settlement Types

| Type | What happens at expiry | Examples |
|---|---|---|
| **Cash settled** | No physical delivery; final P&L = (settlement price - entry price) × multiplier | ES, NQ, most index futures |
| **Physical delivery** | Actual commodity/asset is delivered | CL (crude oil), GC (gold), ZB (bonds) |

**The agent should never hold a physically-delivered futures contract to expiry.** Always roll or close before the first notice date.

## Why the Agent Needs Futures Awareness

1. **Pre-market sentiment:** ES/NQ futures trade nearly 24h. Overnight futures movement signals equity market direction before the cash market opens.
2. **Macro context:** Bond futures (ZB/ZN) reflect interest rate expectations. Currency futures (6E) reflect USD strength. Gold futures (GC) reflect risk appetite.
3. **Hedging awareness:** Understanding that portfolio hedges can be implemented via short index futures (not that this agent hedges — but understanding why markets move when hedgers act).
4. **Volatility events:** Futures limit-up/limit-down events and overnight gaps affect equity market opens.
5. **Correlation:** Commodity futures (CL, GC) affect sector performance (energy stocks, miners).

## Futures-Specific Risks

- **Leverage amplification:** Small price moves → large P&L relative to margin deposited.
- **Gap risk:** Futures can gap on overnight news (though they trade nearly 24h, there's a daily 1-hour halt).
- **Roll risk:** Roll costs can erode returns for long-term positions.
- **Liquidity varies:** Back-month contracts and exotic futures may have wide spreads.
- **Margin calls:** If equity drops below maintenance → forced liquidation at worst possible time.
- **Delivery risk:** Holding a physical-delivery contract past first notice date → potential obligation to take/deliver the commodity.

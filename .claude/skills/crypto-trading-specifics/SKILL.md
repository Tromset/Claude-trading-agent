---
name: crypto-trading-specifics
description: Use when analyzing or trading cryptocurrency assets to account for 24/7 markets, exchange fragmentation, on-chain metrics, funding rates, and crypto-specific risks that differ fundamentally from equities.
---

# Crypto Trading Specifics

Crypto markets are structurally different from equities. This skill covers everything the agent must account for when the instrument is a cryptocurrency — from market mechanics to on-chain analytics to exchange risk. All general skills (risk-management, technical-indicators, etc.) still apply; this skill adds the crypto-specific layer.

**Disclaimer:** This skill is for educational purposes. Cryptocurrency markets carry extreme volatility and unique risks including total loss of capital, exchange insolvency, and regulatory action. Not financial advice.

## When to use this skill

- Whenever the instrument under analysis is a cryptocurrency (BTC, ETH, SOL, etc.).
- When evaluating a crypto exchange or wallet setup.
- When funding rates, on-chain metrics, or exchange flows are relevant to the decision.
- When trading perpetual futures or spot crypto.

**Anti-triggers:** not for equities, forex, or commodity futures (use the relevant standard skills). Not for crypto mining or DeFi protocol analysis beyond basic DEX trading.

## Prerequisites

- `trading-fundamentals` — general market concepts (adapted for crypto).
- `risk-management` — same position-sizing discipline applies (1% cap, stops, heat).
- `market-microstructure` — order book concepts (apply differently in crypto).
- `technical-indicators` — standard TA applies to crypto charts.

## Core concepts

### How crypto markets differ from equities

| Dimension | Equities | Crypto | Agent impact |
|---|---|---|---|
| Trading hours | RTH: 9:30–16:00 ET | 24/7/365 | No session-based blackouts; fatigue risk |
| Circuit breakers | Exist (LULD, market-wide halts) | None on most exchanges | Flash crashes can go further |
| Exchanges | Centralized, regulated (NYSE, NASDAQ) | Fragmented (CEXs + DEXs), varying regulation | Price can differ between exchanges |
| Settlement | T+1 (equities) | Near-instant (on-chain) or exchange-internal | Funds available faster |
| Custody | Broker holds shares | Self-custody (wallet) or exchange custody | Exchange risk: hack, insolvency |
| Short selling | Regulated, requires locate | Available via perpetual futures on most CEXs | Easier but leveraged |
| Volatility | SPY avg daily range ~1% | BTC avg daily range ~3–5%, alts 5–15% | Wider stops, smaller position sizes |
| Market cap | Apple ~$3T | BTC ~$1T, most alts < $10B | Liquidity varies wildly |
| Regulation | SEC, FINRA, well-defined | Evolving, jurisdiction-dependent | Regulatory risk is a factor |

### Exchange types

**CEX (Centralized Exchange):** Binance, Coinbase, Kraken, OKX, Bybit. Custodial — the exchange holds your funds. Regulated to varying degrees. Higher liquidity, faster execution, but counterparty risk (exchange could be hacked or go insolvent).

**DEX (Decentralized Exchange):** Uniswap, dYdX, Jupiter. Non-custodial — you hold your own keys. Lower liquidity for most pairs. Higher slippage. Smart contract risk (bugs in the protocol). No KYC typically.

**Agent rule:** trade only on established CEXs with proof-of-reserves. DEXs only for assets not available on CEXs, and with extra caution.

### Crypto-specific risks

| Risk | Description | Mitigation |
|---|---|---|
| **Exchange risk** | Exchange hack, insolvency (FTX, Mt. Gox) | Keep only active trading capital on exchange; withdraw rest to cold wallet |
| **Rug pull** | Project founders abandon, token goes to zero | Only trade established tokens (top 50 by market cap); avoid microcaps |
| **Regulatory risk** | Government bans, SEC enforcement actions | Monitor regulatory news; don't trade tokens under active SEC investigation |
| **Smart contract risk** | DeFi protocol exploit | Avoid DeFi interactions beyond established protocols |
| **Stablecoin risk** | Depeg event (UST/LUNA) | Use only battle-tested stablecoins (USDT, USDC) as quote currency |
| **Liquidity risk** | Low-cap tokens have thin books | Check 24h volume > $10M before trading; check order book depth |
| **Fork/upgrade risk** | Chain forks or protocol upgrades | Avoid positions during scheduled hard forks; reduce size |

### On-chain metrics (crypto-native analysis)

These supplement (not replace) technical analysis:

| Metric | What it measures | Bullish signal | Bearish signal |
|---|---|---|---|
| **Exchange flows (net)** | BTC/ETH moving onto or off exchanges | Net outflows (accumulation) | Net inflows (distribution, sell prep) |
| **Whale wallet activity** | Large holders (>1000 BTC) buying/selling | Whale accumulation | Whale distribution |
| **NVT ratio** | Network Value to Transactions (crypto P/E) | NVT declining (more usage per dollar of market cap) | NVT spiking (overvalued vs usage) |
| **MVRV ratio** | Market Value to Realized Value | MVRV < 1 (market below cost basis = undervalued) | MVRV > 3.5 (overheated) |
| **Funding rate** | Cost of holding perpetual futures | Negative (shorts crowded → contrarian bullish) | Extremely positive (longs crowded → toppy) |
| **Hash rate** | Mining computational power (BTC) | Rising (network health) | Declining (miner capitulation) |
| **Active addresses** | Daily unique addresses transacting | Rising (adoption) | Declining (disinterest) |

**On-chain is supplementary, not primary.** The agent still uses price action, patterns, and indicators as primary drivers. On-chain provides context, not signals.

### BTC dominance

BTC dominance = BTC market cap / total crypto market cap.

| BTC Dominance | Market phase | Alt trading |
|---|---|---|
| Rising (>50% and climbing) | Risk-off in crypto; capital flowing to BTC | Avoid alts, trade only BTC or sit out |
| Stable (45–55%) | Normal conditions | Selective alt trading acceptable |
| Falling (<45% and dropping) | "Alt season" — capital flowing to alts | Alts may outperform; still be selective |

### Stablecoins as quote currency

Most crypto pairs trade against USDT or USDC, not USD. The agent must be aware that stablecoin ≠ dollar — depeg risk exists. Always check stablecoin peg before treating as cash equivalent.

## Decision procedure

1. Identify the asset as cryptocurrency.
2. Check exchange: is this on an established CEX with proof-of-reserves? If not → extra caution or Z.
3. Check market cap and 24h volume: > $1B market cap and > $10M daily volume? If not → Z (too illiquid).
4. Check BTC dominance direction: is it safe to trade alts, or stick to BTC only?
5. Run standard technical analysis (price action, patterns, indicators, S/R, volume).
6. Check on-chain metrics as supplementary data (exchange flows, MVRV, funding rate).
7. Check funding rate (for perps): extreme positive = caution for longs; extreme negative = caution for shorts.
8. Apply standard risk-management (1% cap, stop-loss required, R:R ≥ 2:1).
9. **Crypto volatility adjustment:** stops must be wider than equities — use ATR-based stops on the crypto's actual volatility, not equity-calibrated distances.
10. Emit X, Y, or Z through `buy-sell-hold-decision`.
11. If X: use isolated margin for perps. Max 3× leverage (hard cap).

## Heuristics & thresholds

- **Only trade top 50 by market cap** unless specifically screening small-caps with a dedicated strategy.
- **24h volume must exceed $10M** for any trade.
- **ATR stops:** use 1.5–2× ATR(14) for crypto (vs 1× for equities) due to higher volatility.
- **Funding rate extremes:** |funding| > 0.1% per 8 hours is a warning signal for the crowded side.
- **Max leverage: 3×** on perpetual futures. Never exceed this regardless of exchange limits.
- **Exchange allocation:** never have more than 30% of total crypto portfolio on a single exchange.
- **Reduce position size by 50%** during extreme fear/greed index readings (>85 or <15).

## Common failure modes

- **Using equity-calibrated stops on crypto.** A 2% stop on BTC may be hit by normal noise. Use ATR.
- **Ignoring exchange risk.** "It won't happen to this exchange" — it can. Distribute or withdraw.
- **Leverage overuse.** 10×–100× leverage on crypto is gambling, not trading. Cap at 3×.
- **Trading low-cap tokens without research.** Rug pulls are real. Stick to established assets.
- **Ignoring funding costs.** Holding a perp long with +0.1% funding burns 10.95% per year.
- **FOMO during alt season.** Chasing 50% daily moves = chasing noise. Stick to the strategy.
- **Not accounting for 24/7 market.** The agent must set its own "session" for monitoring — it can't watch 24/7.

## Outputs expected

```json
{
  "skill": "crypto-trading-specifics",
  "asset": "BTC-USDT",
  "exchange": "binance",
  "exchange_risk": "LOW",
  "market_cap": "$1.2T",
  "volume_24h": "$28B",
  "btc_dominance": "52.3%",
  "btc_dominance_trend": "STABLE",
  "on_chain": {
    "exchange_flows": "NET_OUTFLOW",
    "mvrv": 1.8,
    "funding_rate": -0.005
  },
  "volatility_adjustment": "ATR-based stops, 1.5x ATR(14)",
  "crypto_risk_factors": [],
  "action_recommendation": "PROCEED_TO_BUY_SELL_HOLD"
}
```

## References (lazy-load)

- `references/perps-and-funding.md` — perpetual futures mechanics, funding rate math, liquidation, leverage limits.

## Cross-links

- Pairs with: `risk-management` (same caps apply, with crypto volatility adjustments), `trading-fundamentals` (crypto asset class differences), `market-microstructure` (order book applies but fragmented across exchanges), `technical-indicators` (standard TA applies), `safety-and-kill-switch` (exchange down = hard kill equivalent).

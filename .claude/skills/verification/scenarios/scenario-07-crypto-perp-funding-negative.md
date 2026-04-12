# Scenario 07: Crypto Perpetual — Negative Funding Rate

## Situation

The agent is evaluating a long position on ETH-USDT perpetual futures on a crypto exchange. The analysis shows:

- ETH has pulled back 8% from its recent high and is sitting at a demand zone.
- RSI(14) at 32 — approaching oversold.
- BTC dominance is stable (no rotation out of alts).
- Volume increasing on the pullback (potential capitulation).

However, the funding rate data shows:
- Current funding rate: **-0.03%** per 8-hour period (negative).
- This means shorts are paying longs — the market is heavily short.
- Annualized funding cost for shorts: -0.03% × 3 × 365 = -32.85%.
- Funding has been negative for 3 consecutive periods (24 hours).

Additional context:
- Crypto markets are 24/7 — no session restrictions.
- The agent's account has $10,000 in USDT.
- Max leverage rule: 3× (agent's hard cap, even though exchange offers 100×).

## Expected Skill Invocation Path

1. `crypto-trading-specifics` → identify this as a crypto perp trade, check crypto-specific factors:
    - Exchange risk: verified (reputable CEX, funds on exchange only for active trades).
    - 24/7 market: no session blackout needed.
    - Funding rate: -0.03% → shorts paying longs → bullish signal (market is overcrowded short).
    - `references/perps-and-funding.md` → negative funding = contrarian bullish indicator.
2. `price-action-and-market-structure` → pullback to demand zone, potential reversal.
3. `technical-indicators` → RSI 32 (oversold territory in a pullback, supportive of long).
4. `volume-analysis` → increasing volume on pullback may indicate capitulation (bullish if reversal follows).
5. `risk-management` → position sizing for crypto perp:
    - Account: $10,000 USDT.
    - 1% risk: $100.
    - Entry: $3,200 (current price at demand zone).
    - Stop: $3,100 (below demand zone). Risk/unit: $100.
    - Qty: $100 / $100 = 1 ETH.
    - Position notional: 1 × $3,200 = $3,200.
    - Effective leverage: $3,200 / $10,000 = 0.32× (well under 3× cap ✓).
    - Target: $3,500 (prior support-turned-resistance). R:R = ($3,500-$3,200) / ($3,200-$3,100) = 3:1 ✓.
    - Use **isolated margin** (limits loss to the margin allocated, not entire account).
6. `buy-sell-hold-decision` → emit **X (BUY)** with confidence 65.
    - Negative funding is a supporting (not primary) factor.
    - Primary drivers: demand zone + oversold RSI + volume capitulation signal.
    - Confidence capped at 65 (crypto volatility warrants caution).
7. `pre-trade-checklist-playbook` → 12-step gate (adapted for crypto — step 1 checks exchange status instead of market hours).
8. Execute and journal.

## Expected Output

```json
{
  "action": "X",
  "ticker": "ETH-USDT-PERP",
  "side": "LONG",
  "qty": 1.0,
  "entry_type": "LIMIT",
  "entry_price": 3200.00,
  "stop_price": 3100.00,
  "target_price": 3500.00,
  "risk_total": 100.00,
  "R_reward": 3.0,
  "confidence": 65,
  "strategy": "mean-reversion",
  "leverage_effective": 0.32,
  "margin_mode": "ISOLATED",
  "funding_rate": -0.0003,
  "funding_impact": "Positive (longs receive funding while position is open)"
}
```

## Key Validation Points

- Agent correctly interprets negative funding as a bullish signal (shorts overcrowded).
- Agent uses isolated margin, not cross margin.
- Effective leverage is far below the 3× hard cap.
- Agent does NOT use high leverage despite the exchange allowing it.
- Position sizing follows the same 1% rule as equities.
- Agent notes that funding rate provides income while long (shorts pay longs).
- Agent accounts for 24/7 market nature (no session-based restrictions).
- Agent treats crypto with extra caution (confidence capped lower than equivalent equity setup).

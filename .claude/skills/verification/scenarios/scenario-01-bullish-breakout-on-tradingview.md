# Scenario 01: Bullish Breakout on TradingView

## Situation

The agent is viewing a TradingView chart of MSFT on the daily timeframe. The paper trading panel is open at the bottom. The chart shows:

- Price has been consolidating in a range of $405–$420 for 3 weeks.
- Today's candle is a strong bullish marubozu closing at $422.50, breaking above $420 resistance.
- Volume on the breakout candle is 2.1× the 20-day average.
- RSI(14) reads 63 — above 50 but below overbought.
- MACD just crossed bullish (signal above zero line).
- 20 EMA is trending upward, price is above it.
- No earnings within the next 2 weeks.
- Account is in paper mode with $50,000 balance.

## Expected Skill Invocation Path

1. `trading-app-ui-navigation` → identify TradingView, map regions, confirm paper mode.
2. `screenshot-vision-protocol` → CAPTURE → ORIENT (platform=TradingView, mode=paper, chart=MSFT daily) → READ → VERIFY.
3. `price-action-and-market-structure` → identify range breakout, bullish structure (HH forming).
4. `chart-patterns` → recognize rectangle/range breakout pattern.
5. `technical-indicators` → RSI 63 (bullish but not overbought), MACD bullish cross, price above 20 EMA.
6. `support-resistance-and-fibonacci` → $420 was resistance, now becomes support. Next resistance at $435 (prior swing high).
7. `volume-analysis` → 2.1× volume confirms breakout conviction.
8. `news-and-macro-awareness` → no earnings, no FOMC — clear.
9. `trading-strategies-playbook` → matches `breakout` strategy template.
10. `risk-management` → compute position size:
    - Stop below breakout level: $418.00 (below the broken resistance).
    - Risk per share: $422.50 - $418.00 = $4.50.
    - 1% account risk: $50,000 × 0.01 = $500.
    - Shares: floor($500 / $4.50) = 111 shares.
    - Target: $435 (next resistance) → reward = $12.50 → R:R = 2.78:1 ✓.
    - Portfolio heat: single position, heat = $500 / $50,000 = 1% ✓.
11. `buy-sell-hold-decision` → emit **X (BUY)** with confidence 74.
12. `pre-trade-checklist-playbook` → run 12-step gate → all pass.
13. `screenshot-vision-protocol` → pre-click verification → CONFIRM → ACT → VALIDATE.
14. `trade-journaling-and-backtesting` → log entry record.

## Expected Output

```json
{
  "action": "X",
  "ticker": "MSFT",
  "side": "LONG",
  "qty": 111,
  "entry_type": "LIMIT",
  "entry_price": 422.50,
  "stop_price": 418.00,
  "target_price": 435.00,
  "risk_total": 499.50,
  "R_reward": 2.78,
  "confidence": 74,
  "strategy": "breakout"
}
```

## Key Validation Points

- Agent correctly identifies paper mode before trading.
- Risk per trade does not exceed 1% ($500).
- Stop is placed logically (below breakout level, not arbitrary).
- Volume confirmation is checked (>1.5× average).
- All 12 checklist steps pass before execution.
- Trade is journaled with full context.

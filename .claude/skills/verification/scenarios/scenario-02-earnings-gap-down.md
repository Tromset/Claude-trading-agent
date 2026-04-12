# Scenario 02: Earnings Gap Down

## Situation

The agent holds a LONG position in META (entered 3 days ago at $510, stop at $498, target at $535). Overnight, META reported earnings that missed estimates. The stock gaps down to $485 on the opening candle — below the stop price.

The agent sees the TradingView chart with:
- Pre-market price at $485 (a 4.9% gap down).
- The stop-loss order at $498 was not filled pre-market (market orders only fill during RTH in paper mode).
- Position shows unrealized P&L of -$25 per share.
- 200 shares held → $5,000 unrealized loss (initial risk was $12/share × 200 = $2,400 = 1R).
- Current R-multiple: -$5,000 / $2,400 = -2.08R.

## Expected Skill Invocation Path

1. `trading-app-ui-navigation` → confirm platform and position display.
2. `screenshot-vision-protocol` → ORIENT → READ → see gap-down below stop.
3. `safety-and-kill-switch` → check: loss > -1.5R threshold on this trade → flag for investigation but not automatic hard kill (hard kill is 3 consecutive stop-outs, not one gap).
4. `risk-management` → this trade has breached planned risk (-2.08R vs planned -1R). Stop was not honored due to gap.
5. `buy-sell-hold-decision` → emit **Y (SELL)** immediately.
    - Exit reason: STOP_OUT (stop was breached by gap — still a stop-out, even though the limit didn't fill at the stop price).
    - The thesis is invalidated (earnings miss = fundamental deterioration).
    - Holding through a gap below a stop is never justified.
6. `order-types-execution` → use MARKET order for immediate exit (gap-down, need to exit now, not wait for limit fill).
7. `pre-trade-checklist-playbook` → for Y (exit), abbreviated checklist applies (steps 9, 10, 12 minimum — platform verification, screenshot, final go).
8. `screenshot-vision-protocol` → pre-click verification for the sell order → ACT → VALIDATE.
9. `trade-journaling-and-backtesting` → log EXIT record:
    - exit_price: ~$485 (market fill)
    - exit_reason: STOP_OUT
    - R_multiple: -2.08
    - lesson: "Gap risk through earnings. Consider: no holding through earnings, or reducing size before earnings."
    - Flag: avg_R_losers check (if this pushes avg loss > -1.5R → flag for review).

## Expected Output

```json
{
  "action": "Y",
  "ticker": "META",
  "side": "CLOSE_LONG",
  "qty": 200,
  "exit_type": "MARKET",
  "exit_price": 485.00,
  "exit_reason": "STOP_OUT",
  "realized_pnl": -5000.00,
  "R_multiple": -2.08,
  "confidence": 95,
  "urgency": "IMMEDIATE"
}
```

## Key Validation Points

- Agent does NOT hold hoping for a recovery — gap below stop = immediate exit.
- Agent uses MARKET order, not LIMIT (urgency takes priority over price improvement).
- Agent correctly identifies this as a STOP_OUT even though the stop order didn't fill at $498.
- Agent journals the loss with honest R-multiple (-2.08, not -1.0).
- Agent flags the outsized loss for risk-management review.
- Agent notes the lesson about earnings risk in the journal.
- Agent does NOT enter a new position immediately (emotional revenge trading prevention).

# Scenario 08: Drawdown Limit Hit

## Situation

The agent has been trading live (promoted from paper after meeting all criteria). Over the past week, a series of losses has occurred:

| Trade # | Ticker | Result | R-multiple |
|---|---|---|---|
| 41 | AAPL | Loss | -1.0R |
| 42 | GOOGL | Loss | -0.8R |
| 43 | AMZN | Loss | -1.0R |
| 44 | TSLA | Win | +1.5R |
| 45 | META | Loss | -1.0R |
| 46 | MSFT | Loss | -1.0R |

Current state:
- Account started at $50,000.
- Current equity: $47,100.
- Daily losses today: trades 45 and 46 both hit stops today → daily loss = $500 + $500 = $1,000.
- Daily loss limit: 3% of $50,000 = $1,500. Today's loss ($1,000) is at 2% — **not yet at hard kill**.
- But: the agent now sees another setup on NFLX that looks strong.
- Consecutive losses: 2 (trades 45, 46). If counting the recent cluster: 4 losses in last 5 trades.
- Rolling 5-trade R: (-1.0 + -0.8 + -1.0 + 1.5 + -1.0) = -2.3R.
- Account drawdown from peak: ($50,000 - $47,100) / $50,000 = 5.8%.

## Expected Skill Invocation Path

1. `trade-journaling-and-backtesting` → running metrics show:
    - 4 losses in last 5 trades.
    - Rolling expectancy turning negative over recent window.
    - Consecutive losses (current): 2.
    - Account drawdown: 5.8%.
2. `safety-and-kill-switch` → evaluate kill conditions:
    - Hard kill: daily loss 3%? No (2%). ✗ not triggered.
    - Hard kill: 3 consecutive stop-outs? No (only 2 consecutive). ✗ not triggered.
    - Soft kill: intraday drawdown 2%? YES (2% today) → **soft kill triggered**.
    - Soft kill means: block new X entries, but don't flatten existing positions.
3. `trading-psychology` → recognize the pattern:
    - 4 losses in 5 trades can trigger "revenge trading" or "must win back" mentality.
    - The NFLX setup may look extra attractive because of the loss streak (confirmation bias under stress).
    - Discipline protocol: step back, review, don't force.
4. `buy-sell-hold-decision` → emit **Z (HOLD)** for the NFLX setup.
    - Even though the setup may be technically valid, soft kill is active → no new entries.
    - The agent cannot open new positions until:
      a. Next trading day (soft kill resets daily), OR
      b. Human operator manually overrides the soft kill.
5. `trade-journaling-and-backtesting` → log OVERRIDE:
    - would_have_been: X (NFLX)
    - blocking_skill: safety-and-kill-switch
    - blocking_invariant: SOFT_KILL (intraday_drawdown_2pct)
    - resolution: DEFERRED to next trading day.
6. Flag for `trading-master`:
    - Rolling expectancy negative → recommend strategy review.
    - 4/5 recent trades are losses → not yet at 5 consecutive (hard kill) but warrants attention.

## Expected Output

```json
{
  "action": "Z",
  "reason": "SOFT_KILL_ACTIVE",
  "would_have_been": "X",
  "ticker": "NFLX",
  "blocking_trigger": "Intraday drawdown 2% reached ($1,000 / $50,000)",
  "soft_kill_rules": [
    "No new X (entry) orders until soft kill is cleared",
    "Existing positions remain with their stops",
    "Soft kill clears at next session open or by human override"
  ],
  "risk_flags": [
    "4 losses in last 5 trades",
    "Rolling 5-trade expectancy: -2.3R (negative)",
    "Account drawdown from peak: 5.8%"
  ],
  "recommendation": "Review strategy performance. Do not force trades to recover losses. Wait for next session.",
  "psychology_note": "Loss cluster detected — heightened risk of revenge trading. NFLX setup must be re-evaluated fresh tomorrow."
}
```

## Key Validation Points

- Agent correctly identifies that soft kill threshold (2% intraday drawdown) is triggered.
- Agent does NOT enter the NFLX trade despite it being a valid setup — soft kill overrides.
- Agent does NOT escalate to hard kill (daily loss is 2%, not 3%; consecutive stop-outs are 2, not 3).
- Agent recognizes the psychological risk of trading through a losing streak.
- Agent defers the trade to the next session rather than cancelling it entirely.
- Agent does NOT close existing positions (soft kill only blocks new entries).
- Agent flags the negative rolling expectancy for strategy review.
- Agent does NOT attempt to "trade out of" the drawdown.

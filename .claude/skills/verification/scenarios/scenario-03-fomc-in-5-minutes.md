# Scenario 03: FOMC Decision in 5 Minutes

## Situation

The agent is analyzing a chart of SPY on the 15-minute timeframe. It detects a bullish flag pattern with a potential breakout setup. The technical setup looks strong:

- Bullish flag after a 3% rally.
- Volume decreasing during the flag (textbook).
- RSI pulling back to 55 from 72 (healthy reset).
- Price sitting right at the flag breakout line.

However, the FOMC interest rate decision is scheduled for 2:00 PM ET, and the current time is 1:55 PM ET — 5 minutes away.

The economic calendar shows this is a "HIGH IMPACT" event.

## Expected Skill Invocation Path

1. `trading-app-ui-navigation` → platform identification, mode confirmation.
2. `screenshot-vision-protocol` → ORIENT → READ chart.
3. `price-action-and-market-structure` → bullish flag, uptrend intact.
4. `chart-patterns` → bullish flag identified, breakout imminent.
5. `technical-indicators` → RSI healthy, setup looks good technically.
6. `news-and-macro-awareness` → **FOMC in 5 minutes** → HIGH IMPACT event within 30-minute blackout window.
7. `buy-sell-hold-decision` → despite strong technical setup, emit **Z (HOLD)** due to news blackout.
    - Confidence for X would have been ~70, but news blackout overrides.
    - The invariant INV-006 (news blackout) activates.
8. `pre-trade-checklist-playbook` → Step 2 (news/macro check) would **FAIL** → checklist overrides to Z.
9. `trade-journaling-and-backtesting` → log OVERRIDE record:
    - would_have_been: X
    - blocking_skill: news-and-macro-awareness (and pre-trade-checklist step 2)
    - blocking_invariant: INV-006 (news_blackout)
    - resolution: DEFERRED (re-evaluate 15 minutes post-FOMC)

## Expected Output

```json
{
  "action": "Z",
  "reason": "NEWS_BLACKOUT",
  "would_have_been": "X",
  "ticker": "SPY",
  "blocking_event": "FOMC rate decision at 14:00 ET",
  "time_to_event": "5 minutes",
  "blackout_rule": "No new positions within 30 min of high-impact events",
  "deferred_until": "14:15 ET (15 min post-announcement)",
  "confidence_if_no_blackout": 70
}
```

## Key Validation Points

- Agent correctly identifies the FOMC event from the economic calendar.
- Agent emits Z despite a strong technical setup — news blackout overrides technicals.
- Agent does NOT rationalize entering ("it'll be fine, the trend is strong").
- Agent logs an OVERRIDE record with the would-have-been X signal preserved.
- Agent sets a deferred re-evaluation time (post-FOMC + 15 min for volatility to settle).
- Agent does NOT close existing positions purely due to FOMC (that's a separate decision — existing positions with stops are managed normally).
- The trade idea is preserved for later evaluation, not abandoned.

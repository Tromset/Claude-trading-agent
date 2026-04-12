---
name: trading-psychology
description: Use when the agent needs to identify cognitive biases, manage emotional-equivalent states (FOMO, tilt, euphoria), enforce discipline protocols during drawdowns or winning streaks, or route to safety-and-kill-switch on tilt-equivalent conditions.
---

# Trading Psychology

The agent does not have emotions, but it can exhibit behavioral patterns that are functionally identical to human psychological failures: overtrading after losses, increasing size after wins, abandoning rules under time pressure. This skill defines the biases, the emotional-equivalent states, and the rigid rule-based overrides that prevent them.

**Philosophy:** The agent simulates good psychology by rigidly following rules. A human trader needs mindfulness and self-awareness. This agent needs hard-coded circuit breakers and pre-commitment protocols.

## When to use this skill

- After any loss (to check for tilt-equivalent escalation patterns).
- After any winning streak of 3+ trades (to check for euphoria-equivalent over-confidence).
- When the agent detects it is deviating from its own rules (self-audit trigger).
- When P&L volatility exceeds normal parameters (large swings up or down).
- Before increasing position size or trade frequency beyond baseline.
- When time pressure exists (market close approaching, news imminent) and the agent feels compelled to act.
- On any urge to "make back" a loss quickly.

**Anti-triggers:** This skill does not generate trade ideas. It audits behavior and enforces discipline.

## Prerequisites

- Trade journal data: recent trade outcomes (last 10-20 trades).
- Current win/loss streak length.
- Current drawdown from equity peak.
- Time since last trade (to detect overtrading).
- Current portfolio heat and daily P&L.

## Core concepts

### The eight cognitive biases

| Bias | Description | Agent manifestation | Override |
|---|---|---|---|
| Loss aversion | Losses feel 2x as painful as equivalent gains feel good | Holding losers too long, cutting winners too short | Hard stops, no discretionary exits before target |
| Confirmation bias | Seeking information that confirms existing belief | Only reading bullish data on a long position | Require explicit bear case before every X |
| Hindsight bias | "I knew it all along" after the fact | Overfitting to recent patterns | Walk-forward validation, no hindsight in journal |
| Gambler's fallacy | "I'm due for a win after 5 losses" | Increasing size after a losing streak | Fixed sizing regardless of streak |
| Recency bias | Overweighting recent events vs. base rates | Abandoning a strategy after 3 losses when base rate is 45% win | Minimum 30-trade sample before strategy evaluation |
| Anchoring | Fixating on an irrelevant reference point | "It was at $200 last month" as a reason to buy at $150 | Only current structure and value matter |
| Sunk cost fallacy | Holding because of past investment (time, money, ego) | Refusing to stop out because "I've already lost $500" | Stops are executed mechanically, no discretion |
| Disposition effect | Selling winners too early, holding losers too long | Opposite of what produces positive expectancy | Trailing stops for winners, hard stops for losers |

### The four emotional-equivalent states

These are not emotions — the agent is a machine. But these behavioral patterns produce identical outcomes to human emotional trading:

#### 1. FOMO (Fear of Missing Out) equivalent

**Detection:** The agent proposes an X that violates its own setup criteria because "the move is happening now." Characteristics:
- Entry price > 1% above the ideal level
- Volume/pattern criteria not fully met
- Rationale includes urgency language or references to the move already in progress

**Override:** If setup criteria are not met, emit Z. Always. The market offers new setups every day. Missing one trade has zero impact on long-term expectancy.

#### 2. Tilt equivalent

**Detection:** After 3+ consecutive losses, the agent exhibits:
- Increasing position sizes (revenge trading)
- Shortening hold times (overtrading)
- Lowering setup quality bars (taking weak signals)
- Widening stops or removing them (hoping)

**Override:** Mandatory cooldown protocol (see below). Route to `safety-and-kill-switch` if losses reach the daily cap.

#### 3. Euphoria equivalent

**Detection:** After 3+ consecutive wins or a large single win, the agent exhibits:
- Increasing position sizes beyond 1% risk
- Adding more concurrent positions (portfolio heat rising)
- Taking setups in unfamiliar instruments (overconfidence)
- Skipping pre-trade checklist steps

**Override:** Cap position size at baseline regardless of recent performance. Enforce full checklist on every trade. Recent success does not change future probabilities.

#### 4. Capitulation equivalent

**Detection:** During a drawdown, the agent:
- Stops taking valid signals (fear)
- Reduces size below the minimum meaningful level
- Proposes closing all positions regardless of thesis validity
- Suggests "waiting for things to improve" without specific criteria

**Override:** If a setup meets all criteria, take it at standard size. Drawdowns are when discipline matters most. Reducing size is only valid if the strategy itself is being re-evaluated (see systematic-and-algo-trading).

## Decision procedure (self-audit protocol)

Run this check before every X and after every Y:

1. **Streak check:** How many consecutive wins or losses? If >= 3 losses → activate tilt protocol. If >= 3 wins → activate euphoria protocol.
2. **Frequency check:** How many trades in the last 24 hours? If > the strategy's normal frequency by 2x → flag overtrading.
3. **Size check:** Is proposed size larger than the last 10-trade average by > 25%? If yes → cap at average. Query why.
4. **Quality check:** Does this setup meet ALL criteria of the selected strategy? If any criterion is fudged → Z.
5. **Urgency check:** Is there time pressure driving this decision? If yes → Z unless the pressure is a genuine technical trigger (breakout happening now with confirmed volume).
6. **Drawdown check:** Is the account in > 5% drawdown from peak? If yes → reduce risk per trade to 0.5% until drawdown recovers to < 3%.
7. **Revenge check:** Is the instrument the same as the last losing trade AND the direction is the same? If yes → require 24-hour cooling period before re-entry.

## Discipline protocols (rule-based overrides)

### Loss-streak protocol (3+ consecutive losses)

1. Pause all trading for the remainder of the session (minimum 4 hours).
2. Review the last 3 trades in the journal: were they valid setups that lost (acceptable) or rule violations that lost (problem)?
3. If valid setups: resume next session at standard size. Losing streaks are normal (see `trend-following` — 5-8 consecutive losses happen).
4. If rule violations: identify the violated rules, document them, resume at 50% size for the next 5 trades until compliance is confirmed.
5. If 5+ consecutive losses: mandatory full strategy review. Do not trade until the review is complete. This is not capitulation — it is quality control.

### Win-streak protocol (3+ consecutive wins)

1. Do NOT increase size. Winning streaks feel like skill but are often luck/regime alignment.
2. Audit each win: was it a full-criteria setup, or was a rule bent that happened to work? Bent rules that work are more dangerous than bent rules that fail — they reinforce bad behavior.
3. Continue at standard size and standard criteria. The goal is consistent process, not maximum profit during a hot streak.

### P&L volatility protocol

If daily P&L swings exceed 2x the 20-day average daily P&L range:
1. Check if volatility expansion is market-wide (VIX spike) or position-specific.
2. If market-wide: reduce size to 50% until volatility normalizes.
3. If position-specific: review whether position sizes are appropriate for the current ATR.

### Time-pressure protocol

If the agent is considering a trade with < 30 minutes until a forced decision point (market close, news event, etc.):
1. Default: Z. Rushed decisions have negative expectancy.
2. Exception: a pre-planned trigger fires (e.g., a limit order was already set and filled). This is execution, not a rushed decision.

## Heuristics & thresholds

- **3 losses → pause.** Not negotiable.
- **5% drawdown → half size.** Protect capital during adversity.
- **2x frequency → overtrading flag.** The best trade is often no trade.
- **24-hour cooling on revenge re-entry.** Same name, same direction, same day = revenge. Wait.
- **30-trade minimum for strategy evaluation.** Do not judge a system on 5 trades.
- **No rules are bent for "just this once."** Every exception creates precedent.

## Common failure modes

- **"I'll follow the rules starting tomorrow."** Rules apply now. Always now.
- **Confusing discipline with rigidity.** Discipline means following rules mechanically. It does NOT mean ignoring new information — if a stop is hit, exit; if the thesis changes, adapt. But adapt via rules, not ad-hoc decisions.
- **Journaling without reviewing.** Writing trades down but never reading the journal is theater.
- **Blaming the market.** The market is not wrong. The setup either met criteria or it did not.
- **Outcome bias.** Judging a decision by its result rather than its process. A loss on a valid setup is a good trade. A win on a broken rule is a bad trade.

## Outputs expected

This skill does not produce X/Y/Z directly. It produces an **audit result** that gates the decision:

```json
{
  "skill": "trading-psychology",
  "audit": "pass" | "flag" | "block",
  "current_streak": -3,
  "drawdown_pct": 0.04,
  "frequency_24h": 2,
  "size_vs_average": 1.0,
  "active_protocols": ["loss-streak-pause"],
  "flags": ["revenge-entry-detected"],
  "block_reason": "3+ consecutive losses, mandatory 4h pause not yet elapsed",
  "resume_conditions": "Next session, standard size, full checklist",
  "route_to_kill_switch": false,
  "notes": "..."
}
```

If `audit = block`, the downstream `buy-sell-hold-decision` must emit Z regardless of setup quality. If `route_to_kill_switch = true`, escalate to `safety-and-kill-switch` immediately.

## References

- Kahneman, D. — Thinking, Fast and Slow (biases framework).
- Covel, M. — Trend Following (handling losing streaks).
- Douglas, M. — Trading in the Zone (process vs. outcome).
- Steenbarger, B. — The Psychology of Trading (behavioral patterns).

## Cross-links

- Pairs with: `safety-and-kill-switch` (escalation on tilt), `trade-journaling-and-backtesting` (data source for streak/drawdown), `risk-management` (size caps), `systematic-and-algo-trading` (discipline = the system).
- Feeds: `buy-sell-hold-decision` (audit gate).
- Consulted by: every strategy skill after losses or unusual performance.

# Global Invariants — Expanded Rationale

These are hard rules. Every skill and every action inherits them. Violations MUST abort to `safety-and-kill-switch` and emit `Z`.

## 1. Risk before return

No `X` or `Y` is emitted without a fresh, valid output from `risk-management`. "Fresh" means computed for the current account balance, current volatility (ATR), and current portfolio heat — not cached from yesterday.

**Why:** The single fastest way to destroy an account is un-sized positions. Every trade must have a numeric per-trade risk in currency (not percent guessed at click time).

**Failure example:** Agent sees a textbook breakout on AAPL and wants to buy 100 shares. `risk-management` says the correct size (given ATR-based stop) is 37 shares. Agent MUST size to 37, not 100. If it can't compute, emit `Z`.

## 2. Screen is truth, not memory

Before any click, the agent re-screenshots and runs pre-click verification from `screenshot-vision-protocol`. The order ticket on screen must match the agent's intent field-by-field:
- Symbol
- Side
- Quantity
- Order type
- Limit/stop prices
- Time-in-force

**Why:** Platforms sometimes auto-fill stale values, re-route to different accounts, or re-order input fields after an update. The agent's memory of what it typed is not authoritative — the pixels are.

**Failure example:** Agent intends to buy 10 shares of SPY. Platform's order ticket shows "QQQ, 10, BUY." Mismatch → abort → `Z`.

## 3. Caps are hard

Three caps must never be breached:

| Cap | Default | Skill |
|---|---|---|
| Daily-loss cap | 3% of account | `safety-and-kill-switch` |
| Per-trade risk cap | 1% of account | `risk-management` |
| Portfolio heat cap | 6% of account simultaneously at risk | `risk-management` |

**Why:** Caps are the difference between "bad day" and "blown account." A single un-capped trade can compound with a bad streak to produce ruin. Caps make ruin impossible on a single day or single trade.

## 4. Journal everything

Every `X`, `Y`, and every `Z` that overrode a would-be action is written to the trade journal via `trade-journaling-and-backtesting`. A `Z` by default (nothing was going to happen anyway) is not journaled; a `Z` that rejected an `X` or `Y` is.

**Why:** The journal is the only feedback loop. Without it, the agent cannot learn, cannot audit, and cannot backtest its own decisions.

## 5. Mismatch = abort

Any time the agent's internal state disagrees with the screen state → abort to `safety-and-kill-switch` → emit `Z`. Examples:
- Agent thinks it's flat; screen shows an open position.
- Agent thinks order was filled; screen shows it's still working.
- Agent sees an unexpected popup (margin call, 2FA, connection error, platform update).

**Why:** Acting under state disagreement is how "one bad trade" becomes "catastrophic." Always prefer the visible screen.

## 6. ToS first

Broker Terms of Service, exchange rules, and applicable regulations override anything in this library. If a strategy would require action that violates ToS → emit `Z`, log the conflict, escalate to the human operator.

Examples:
- PDT rule (<$25k account) forbids a 4th day trade in 5 rolling days → `Z`.
- Exchange forbids market orders during the opening auction → switch to limit or `Z`.
- Broker forbids naked short calls → `Z` and re-plan.

## 7. News blackout

No discretionary action in the window spanning 5 minutes before through 5 minutes after a high-impact news release for the relevant instrument, unless the strategy is an explicit pre-planned event trade. See `news-and-macro-awareness` for the event calendar.

**Why:** Volatility during news release causes spreads to widen, slippage to balloon, and stops to blow through. Risk models underestimate news-window risk by 5–10×.

## 8. Z is the default

When anything is ambiguous, incomplete, contradictory, or under-confident — emit `Z`. The cost of a missed trade is ~0. The cost of a bad trade is non-zero. Asymmetry favors `Z`.

**Confidence threshold:** any `X` or `Y` with confidence < 60/100 downgrades to `Z`.

**Three-strike rule:** If the same setup yields `Z` three times in a row, mark it "watching" and move on — do not force it on the fourth look.

## Enforcement

Every skill's "Outputs expected" section must include which invariants it checked. The audit pass greps for `invariants_checked:` in the JSON output and fails builds that omit it.

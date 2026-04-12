# 12-Step Pre-Trade Checklist — Detailed Reference

For each step: what to check, how to check it, pass/fail criteria, common false-fails, and override rules.

## Step 1: Market Regime Check

**What to check:** Is the market open? Is this instrument trading in regular hours? Any halts?

**How to check:**
- Invoke `trading-fundamentals` for session hours.
- For US equities: RTH = 9:30–16:00 ET. Pre/post-market orders require explicit strategy allowance.
- For crypto: 24/7 — always passes (but check exchange status).
- Check for trading halts (LULD, news halt) via `market-microstructure`.

**Pass criteria:**
- Market is open for this instrument's asset class.
- No active trading halt on the ticker.
- If pre/post-market: the strategy explicitly permits extended hours trading.

**Fail criteria:**
- Market closed and strategy doesn't permit after-hours.
- Trading halt active on the ticker.
- Exchange is down or unreachable.

**Common false-fails:** Holiday schedules (early close days); crypto exchanges with scheduled maintenance windows.

**Override:** Human can override for extended-hours trading only. Cannot override a trading halt.

---

## Step 2: News / Macro Check

**What to check:** Any high-impact economic events in the next 30 minutes? Earnings within 24 hours? FOMC, CPI, NFP, or other market-moving releases?

**How to check:**
- Invoke `news-and-macro-awareness`.
- Check economic calendar for HIGH impact events within 30 min.
- Check if the specific ticker has earnings within 24 hours.
- Check for any breaking news that could invalidate the thesis.

**Pass criteria:**
- No HIGH-impact economic events within 30 minutes.
- No earnings report for this ticker within 24 hours (unless the strategy is specifically an earnings play).
- No breaking news that directly affects the thesis.

**Fail criteria:**
- HIGH-impact event within 30 minutes (FOMC, CPI, NFP, etc.).
- Earnings within 24 hours and strategy is not an earnings-specific strategy.
- Breaking news contradicts the trade thesis.

**Common false-fails:** Low/medium impact events (these do NOT block); earnings on a correlated stock (only the specific ticker matters).

**Override:** Human can override news blackout. Cannot override earnings blackout unless strategy is explicitly earnings-focused.

---

## Step 3: Strategy Alignment

**What to check:** Does the proposed trade match a defined strategy from the playbook? Which one?

**How to check:**
- Invoke `trading-strategies-playbook`.
- Match the trade setup to a specific strategy template (breakout, swing, mean-reversion, etc.).
- Verify the timeframe matches the strategy's intended timeframe.
- Verify the market regime matches the strategy's intended regime.

**Pass criteria:**
- Trade matches exactly one defined strategy.
- Timeframe is correct for that strategy.
- Market regime is compatible (e.g., not running a trend strategy in a ranging market).

**Fail criteria:**
- Trade doesn't match any defined strategy ("I just feel like it should go up").
- Timeframe mismatch (day-trading setup on weekly chart).
- Regime mismatch (mean-reversion in a strong trend).

**Common false-fails:** Hybrid setups that blend two strategies — acceptable if both strategies agree on direction and the agent can articulate which rules apply.

**Override:** No override. Every trade must align with a defined strategy.

---

## Step 4: Technical Confirmation

**What to check:** Do price action, patterns, indicators, S/R, and volume provide confluence? Minimum 3/5 categories must confirm.

**How to check:**
- `price-action-and-market-structure` → directional bias (bullish/bearish/neutral).
- `chart-patterns` → pattern identified and direction.
- `technical-indicators` → indicator confluence score.
- `support-resistance-and-fibonacci` → key levels support the trade.
- `volume-analysis` → volume confirms the move.

**Pass criteria (for X — entry):**
- At least 3 of 5 analysis categories confirm the trade direction.
- No category is strongly contradicting (e.g., 3 bullish + 1 neutral + 1 bearish = OK; 3 bullish + 2 strongly bearish = review).

**Pass criteria (for Y — exit):**
- Exit trigger is clear (stop hit, target reached, thesis broken).
- For stop-outs and target hits: technical confirmation is not required (mechanical exit).

**Fail criteria:**
- Fewer than 3/5 categories confirm.
- 2+ categories strongly contradict the direction.

**Common false-fails:** One indicator lagging while others have already confirmed — check if the lagging indicator is stale or just slow. Volume may be low early in the session (before 10:00 ET) — use prior day's volume as reference.

**Override:** Human can override to proceed with 2/5 confluence if they provide written rationale. Cannot proceed with fewer than 2/5.

---

## Step 5: Fundamental Check (If Applicable)

**What to check:** For position trades and Buffett-style candidates: does the company pass the fundamental screen?

**How to check:**
- Invoke `fundamental-analysis-and-value-investing`.
- Run `references/buffett-checklist.md` for value candidates.
- Check `references/financial-ratios.md` for key metrics.

**Pass criteria:**
- For day/swing trades: this step auto-passes (fundamental analysis not required for short-term trades).
- For position trades: company passes at least 3/4 Buffett core criteria.
- For value candidates: margin of safety ≥ 15%.

**Fail criteria:**
- Position trade on a company that fails ≥ 2 Buffett core criteria.
- Value candidate with margin of safety < 10%.

**Common false-fails:** Cyclical companies with temporarily depressed earnings — check normalized earnings, not just TTM.

**Override:** Human can override for special situations (turnarounds, spinoffs) with written rationale.

---

## Step 6: Risk Sizing (NON-OVERRIDABLE)

**What to check:** Is position size ≤ 1% account risk? Is R:R ≥ 2:1? Is portfolio heat ≤ 6%?

**How to check:**
- Invoke `risk-management`.
- Compute: `position_risk = (entry_price - stop_price) × qty`.
- Verify: `position_risk / account_equity ≤ 0.01`.
- Compute: `R_reward = (target - entry) / (entry - stop)` for longs.
- Compute: `current_heat = sum of all open position risks / account_equity`.

**Pass criteria:**
- Per-trade risk ≤ 1% of account equity.
- R:R ≥ 2:1.
- Portfolio heat ≤ 6% after adding this trade.
- Stop-loss is defined and placed at a logical technical level.

**Fail criteria:**
- Per-trade risk > 1%. → Resize the position, do not proceed.
- R:R < 2:1. → Find a better entry or wider target, or emit Z.
- Portfolio heat > 6% after this trade. → Reduce size or skip.
- No stop-loss defined.

**Common false-fails:** None. These are hard numbers, not judgment calls.

**Override: NONE. This step cannot be overridden, not even by a human operator.** The 1% per-trade risk cap, 2:1 R:R minimum, and 6% heat cap are inviolable. If sizing fails, resize or don't trade.

---

## Step 7: Order Specification

**What to check:** Is the order fully specified with all required fields?

**How to check:**
- Verify all fields from the X/Y output schema are populated.
- Invoke `order-types-execution` to confirm the order type is appropriate for the situation.

**Required fields for X (entry):**
- Ticker, side (LONG/SHORT), qty, entry order type, entry price (for limit/stop), stop-loss price, target price, time-in-force.

**Required fields for Y (exit):**
- Position reference, exit order type, exit price (for limit), exit reason.

**Pass criteria:** All required fields populated with valid values. Order type matches the situation (see `references/order-type-matrix.md`).

**Fail criteria:** Any required field missing or invalid. Order type inappropriate (e.g., market order in a thin pre-market book).

**Common false-fails:** Market orders don't need a price field — only limit/stop orders do.

**Override:** No override. Incomplete orders are never submitted.

---

## Step 8: Safety Check (NON-OVERRIDABLE for hard kills)

**What to check:** Any kill-switch triggers active?

**How to check:**
- Invoke `safety-and-kill-switch`.
- Check: daily loss limit (3%) hit?
- Check: 3 consecutive stop-outs?
- Check: platform disconnect or state mismatch?
- Check: margin call?
- Check: soft kill triggers (2% intraday drawdown, wide spreads, news blackout)?

**Pass criteria:**
- No hard kill triggers active.
- No soft kill triggers active (for new entries).
- For exits (Y): hard kills flatten positions — exits always proceed.

**Fail criteria:**
- Any hard kill trigger → Z immediately, plus flatten if required.
- Any soft kill trigger for new entries (X) → Z.

**Common false-fails:** Soft kill from yesterday that hasn't been cleared — check if it reset at session open.

**Override: Hard kills are NON-OVERRIDABLE.** Soft kills can be overridden by human with acknowledgment.

---

## Step 9: Platform Verification

**What to check:** Correct account (paper vs live)? Correct ticker loaded on chart?

**How to check:**
- Invoke `trading-app-ui-navigation`.
- Confirm the account mode label (Paper/Live) matches the intended mode.
- Confirm the ticker displayed on the chart matches the intended ticker.
- Confirm the correct order panel is visible.

**Pass criteria:**
- Account mode matches intent (paper for paper, live for live).
- Chart ticker matches the trade plan ticker.
- Order panel is visible and accessible.

**Fail criteria:**
- Account mode mismatch (intending paper but on live, or vice versa).
- Ticker mismatch (chart shows AMZN but trade plan says AAPL).
- Order panel not visible or obscured.

**Common false-fails:** Multiple ticker symbols displayed (watchlist + chart) — verify the CHART ticker, not the watchlist highlight.

**Override:** No override. Account mode and ticker must match. Period.

---

## Step 10: Screenshot Verification (NON-OVERRIDABLE)

**What to check:** Fresh screenshot taken? 7-step vision protocol passed? Pre-click fields match order spec?

**How to check:**
- Invoke `screenshot-vision-protocol` full 7-step process.
- Take a fresh screenshot (not a cached/stale one).
- Run pre-click verification from `references/pre-click-verification.md`.
- Verify all 14 fields match the order specification from step 7.

**Pass criteria:**
- Screenshot is fresh (taken within the last 30 seconds).
- All 14 pre-click verification fields match the order spec.
- No anomalies detected (unexpected popups, error messages, wrong screen).

**Fail criteria:**
- Screenshot is stale (older than 30 seconds).
- Any pre-click field mismatch.
- Any anomaly detected on screen.

**Common false-fails:** Minor price movement between order spec creation and screenshot — if the limit price in the order ticket matches what was planned, minor spot-price movement is OK.

**Override: NONE. Every trade requires a fresh, verified screenshot.** No "I already checked it" or "it was fine a minute ago."

---

## Step 11: Confidence Gate

**What to check:** Is the confidence score from `buy-sell-hold-decision` above the minimum threshold?

**How to check:**
- Read the confidence field from the X/Y output.
- Compare against threshold: ≥ 60 for live, ≥ 50 for paper.

**Pass criteria:**
- Live account: confidence ≥ 60.
- Paper account: confidence ≥ 50.

**Fail criteria:**
- Below the threshold for the current account mode.

**Common false-fails:** Confidence at exactly 60 — this passes (≥, not >).

**Override:** Human can lower the paper threshold to 40 for experimental strategies. Live threshold of 60 cannot be lowered.

---

## Step 12: Final Go / No-Go

**What to check:** Did all 11 previous steps pass?

**How to check:**
- Review the pass/fail status of steps 1–11.
- ALL must be PASS for the final result to be GO.

**Pass criteria:** Steps 1–11 all passed.

**Fail criteria:** Any step failed. Result = Z (hold). Log which step(s) failed.

**Override:** No override. This is a logical AND of all steps. One failure = no trade.

---

## Worked Example: Buy AAPL Limit $185

**Proposed trade:** X (BUY) AAPL, LONG, 27 shares, LIMIT $185.00, stop $180.00, target $195.00. Account: paper, $50,000. Confidence: 72.

| Step | Check | Result | Detail |
|---|---|---|---|
| 1. Market regime | Market open? Halts? | PASS | 10:15 AM ET, RTH, no halts on AAPL |
| 2. News/macro | Events in 30 min? Earnings? | PASS | No high-impact events; AAPL earnings 3 weeks away |
| 3. Strategy alignment | Matches defined strategy? | PASS | Matches swing-trading breakout template |
| 4. Technical confirmation | 3/5 confluence? | PASS | PA: bullish, Pattern: bull flag, Indicators: RSI 58/MACD bullish, S/R: above key support, Volume: 1.4x avg → 5/5 |
| 5. Fundamental check | Buffett criteria? | PASS | Auto-pass (swing trade, not position/value) |
| 6. Risk sizing | ≤1% risk? R:R ≥2:1? | PASS | Risk: 27 × $5 = $135 (0.27%). R:R = $10/$5 = 2:1. Heat: 0.27% (well under 6%) |
| 7. Order spec | All fields populated? | PASS | Ticker=AAPL, side=LONG, qty=27, type=LIMIT, price=185, stop=180, target=195, TIF=DAY |
| 8. Safety check | Kill triggers? | PASS | No kills active. Daily loss: $0. Consecutive losses: 0 |
| 9. Platform verification | Paper mode? Correct ticker? | PASS | TradingView paper mode confirmed. Chart shows AAPL |
| 10. Screenshot verification | Fresh screenshot? Fields match? | PASS | Screenshot 5 sec old. All 14 fields verified |
| 11. Confidence gate | ≥ 50 (paper)? | PASS | 72 ≥ 50 |
| 12. Final go/no-go | All 11 passed? | **GO** | All steps passed → execute the order |

**Result:** EXECUTE the buy order.

---

## Non-Overridable Steps Summary

| Step | Non-Overridable? | Rationale |
|---|---|---|
| 6. Risk sizing | YES | Capital preservation is absolute |
| 8. Safety (hard kills) | YES | Hard kills protect against catastrophic loss |
| 10. Screenshot verification | YES | Visual verification prevents wrong-order errors |

All other steps can be overridden by the human operator with documented rationale, but the default is strict enforcement.

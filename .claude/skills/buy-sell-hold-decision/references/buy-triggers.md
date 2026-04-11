# Buy Triggers — When X is Justified

`X` is justified only when **all** of the following are satisfied.

## Mandatory conditions (ALL must be true)

1. **A strategy skill has produced a complete setup** — entry level, stop, target, rationale. Not a hunch.
2. **`risk-management` has produced a valid sizing** — integer quantity, per-trade risk ≤ 1% of account, portfolio heat after this trade ≤ 6% of account.
3. **R:R ≥ 2:1** — the distance from entry to target is at least 2× the distance from entry to stop.
4. **No global invariant is threatened** — see `trading-master/references/global-invariants.md`.
5. **No news blackout active** for the instrument (unless the setup is an explicit pre-planned event trade).
6. **Screen is readable, state is consistent.**
7. **The agent can honestly score confidence ≥ 60.**
8. **Pre-trade checklist will be runnable** immediately after this skill emits X.

If any single item above fails → downgrade to `Z`.

## Strategy-specific X-triggers

### Value investing X (from `fundamental-analysis-and-value-investing`)
- Intrinsic value computed (DCF or owner-earnings approach)
- Current price ≤ 0.7 × intrinsic value (margin of safety ≥ 30%)
- Moat confirmed via `buffett-checklist.md` (≥ 4 of 5 checkboxes)
- Debt-to-equity ≤ industry median
- FCF positive for past 5 years
- ROIC ≥ 12% for past 5 years
- No known regulatory/legal overhang
- No X within 48h of an earnings release

### Swing breakout X (from `trading-strategies-playbook/references/breakout.md`)
- Price breaks a clearly defined consolidation / pattern high
- Volume on breakout ≥ 1.5× 20-day average
- Entry ≤ 1% beyond the breakout level (no chasing)
- Stop below the breakout level minus 1× ATR(14)
- Target at next significant resistance or 2× stop distance (whichever is closer)
- Higher timeframe (daily if trading 1H, weekly if trading daily) in uptrend

### Swing pullback X (from `trading-strategies-playbook/references/trend-following.md`)
- HTF is in uptrend (HH and HL structure)
- Price pulls back to a prior support level OR 20/50 EMA OR Fib 38.2–61.8%
- A bullish reversal candle forms at the level (hammer, engulfing, or inside bar break)
- Entry above the reversal candle high
- Stop below the reversal candle low
- Target at prior swing high or HTF resistance

### Mean-reversion X (from `trading-strategies-playbook/references/mean-reversion.md`)
- Range-bound instrument (ADX < 20 on strategy timeframe)
- Price at lower band (Bollinger 2σ) OR oversold (RSI < 30) OR retest of range support
- Bullish price action confirmation at the level
- Stop outside the range low
- Target at range mid / upper band
- NOT valid in trending markets (ADX > 25)

### Day-trade X (from `trading-strategies-playbook/references/day-trading.md`)
- After opening range (first 15-30 min) has formed
- Breakout above opening range high with volume
- VWAP below price (bullish bias)
- Stop at opening range low or 1× ATR(14 × 5min) below entry
- Target at 1R, 2R (two legs), exit all by end of session
- Hard cap: one day trade per session unless plan says otherwise; PDT rule respected

## Scale-in X (for strategies that permit)

A scale-in ladder counts as multiple sequential X decisions:
- Leg 1: at initial setup trigger
- Leg 2: at confirmation (e.g., break of prior candle high / first pullback hold)
- Leg 3: at re-test of entry zone (only if structure still intact)

Each leg is gated independently. Sizing is pre-allocated so the total position, if all legs fill, still fits within the per-trade cap.

## Edge cases

- **Gap up open.** If price gaps above the planned entry, check if it's still within 1% of plan. If yes → X at market with adjusted stop. If no → `Z` (missed, do not chase).
- **Partial trigger.** Pattern is 80% formed but key element (volume, candle close) missing → `Z`, wait one more bar.
- **Simultaneous signals.** Two strategies both emit X on the same ticker — only fill one (the higher-confidence). Do not double-size.
- **Correlated setups.** Three tech names all showing breakouts at the same time — portfolio heat says only one can be taken. Pick the best and `Z` the rest.

## Anti-triggers (never emit X)

- "Gut feeling" with no setup.
- Chasing a move already extended beyond planned entry.
- Adding to a losing position that is hitting its stop.
- Revenge-buying after a recent loss.
- FOMO on social-media hype.
- Pre-news gambling.
- Any trade that can't honestly score confidence ≥ 60.

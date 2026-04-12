# Options Strategies — Reference

Defined-risk structures only. Naked short options are FORBIDDEN. Each strategy below includes: when to use, max risk, max reward, breakeven, management rules, and exit criteria.

## Priority order (simplest and safest first)

1. Long call / Long put (directional, defined risk)
2. Vertical spreads (directional, reduced cost)
3. Covered call (income on existing stock)
4. Cash-secured put (income, willing to own)
5. Iron condor (neutral, range-bound)
6. Collar (hedge existing position)

---

## 1. Long Call

**When to use:** Bullish on the underlying, want defined risk, IV is low (IVR < 30), time horizon 30-90 days.

**Structure:** Buy 1 call at desired strike.

**Max risk:** Premium paid. Known at entry.
**Max reward:** Unlimited (theoretically).
**Breakeven:** Strike + premium paid.

**Strike selection:**
- ATM or slightly ITM (delta 0.50-0.70) for higher probability.
- OTM (delta 0.30-0.40) only if conviction is very high AND IV is very low.
- Never buy deep OTM (delta < 0.20) — lottery ticket behavior.

**DTE:** Minimum 45 days. Prefer 60-90 days to reduce theta drag.

**Management rules:**
- Exit at 50% profit (if option doubles from entry, take the gain).
- Exit at 50% loss (if option halves, thesis failed — cut it).
- Exit at 21 DTE regardless (theta acceleration).
- Never hold through earnings unless the thesis specifically includes the event.

**Example:**
```
AAPL at $180. Buy $180 call, 60 DTE, premium $6.50.
Max risk: $650 per contract.
Breakeven: $186.50.
Target exit: option reaches $9.75 (50% gain = sell at $650 profit).
Stop exit: option falls to $3.25 (50% loss = $325 loss accepted).
Time exit: 21 DTE if neither target nor stop hit.
```

---

## 2. Long Put

**When to use:** Bearish on the underlying, want defined risk, IV is low, time horizon 30-90 days. Also: hedging a long stock position (protective put).

**Structure:** Buy 1 put at desired strike.

**Max risk:** Premium paid.
**Max reward:** Strike price minus premium (stock goes to zero, theoretically).
**Breakeven:** Strike - premium paid.

**Strike selection:**
- ATM or slightly ITM (delta -0.50 to -0.70) for directional trades.
- OTM (delta -0.30 to -0.40) for hedges (cheaper, accepts more downside before protection).

**DTE:** Minimum 45 days for directional. For hedges: match to the risk event horizon.

**Management rules:** Same as long call (50% profit, 50% loss, 21 DTE time exit).

---

## 3. Call Debit Spread (Bull Call Spread)

**When to use:** Moderately bullish, want defined risk with lower cost than a naked long call. IV is moderate (IVR 20-50). Target price is known.

**Structure:** Buy 1 call at lower strike, sell 1 call at higher strike. Same expiration.

**Max risk:** Net debit paid (premium of long call minus premium of short call).
**Max reward:** Width of strikes minus net debit.
**Breakeven:** Long strike + net debit.

**Width selection:**
- Narrow (2-5 points): lower cost, higher probability of max loss, lower max gain.
- Wide (10-20 points): higher cost, lower probability of max loss, higher max gain.
- Target the short strike at or above the expected move (technical target level).

**DTE:** 30-60 days.

**Management rules:**
- Exit at 50% of max profit (if spread value reaches 50% of max width).
- Exit at 21 DTE.
- If underlying drops below long strike by 2x ATR → close for loss.
- Do NOT hold to expiration (pin risk between strikes).

**Example:**
```
AAPL at $180. Buy $180/$190 call spread, 45 DTE.
Long $180 call: $5.50, Short $190 call: $2.00. Net debit: $3.50.
Max risk: $350 per spread.
Max reward: ($10 width - $3.50 debit) x 100 = $650 per spread.
Breakeven: $183.50.
R:R: 1.86:1.
Profit target: spread reaches $6.75 (50% of max = close at $325 profit).
```

---

## 4. Put Debit Spread (Bear Put Spread)

**When to use:** Moderately bearish, defined risk, lower cost than long put. Mirror of the call debit spread.

**Structure:** Buy 1 put at higher strike, sell 1 put at lower strike. Same expiration.

**Max risk:** Net debit paid.
**Max reward:** Width minus net debit.
**Breakeven:** Long strike - net debit.

**Management:** Same as call debit spread (50% max profit exit, 21 DTE time exit).

---

## 5. Bull Put Spread (Credit)

**When to use:** Bullish or neutral, IV is high (IVR > 50, so selling premium is favorable), want to collect credit with defined risk.

**Structure:** Sell 1 put at higher strike, buy 1 put at lower strike. Same expiration.

**Max risk:** Width minus credit received.
**Max reward:** Credit received.
**Breakeven:** Short strike - credit received.

**Strike selection:**
- Short put: at or below a support level the agent believes will hold.
- Short put delta: 0.25-0.35 (out of the money with 65-75% probability of expiring worthless).
- Width: 5-10 points (defines max loss).

**DTE:** 30-45 days (optimal theta decay collection).

**Management rules:**
- Close at 50% of credit received (take the profit and eliminate risk).
- Close at 21 DTE regardless.
- If short put is breached (stock drops below short strike): close immediately. Do not hope.
- If loss reaches 2x credit: close. The R:R has inverted.

**Example:**
```
AAPL at $180. Sell $170/$165 put spread, 35 DTE.
Sell $170 put: $2.00, Buy $165 put: $1.20. Net credit: $0.80.
Max risk: ($5.00 - $0.80) x 100 = $420 per spread.
Max reward: $80 per spread.
Breakeven: $169.20.
Profit target: spread drops to $0.40 (50% credit collected).
```

---

## 6. Bear Call Spread (Credit)

**When to use:** Bearish or neutral, IV is high, want to collect credit above the market. Mirror of bull put spread.

**Structure:** Sell 1 call at lower strike, buy 1 call at higher strike. Same expiration.

**Max risk:** Width minus credit.
**Max reward:** Credit received.
**Breakeven:** Short strike + credit.

**Management:** Same as bull put spread (50% credit exit, 21 DTE, close if breached).

---

## 7. Iron Condor

**When to use:** Neutral outlook, expect the stock to stay within a range, IV is high (IVR > 50). Combines a bull put spread and a bear call spread.

**Structure:** Sell 1 OTM put + buy 1 further OTM put (lower) + sell 1 OTM call + buy 1 further OTM call (higher). Same expiration.

**Max risk:** Width of widest spread minus total credit received.
**Max reward:** Total credit received.
**Breakeven:** Two breakevens (lower short strike minus credit; upper short strike plus credit).

**Strike selection:**
- Short strikes at delta 0.15-0.25 (1 standard deviation or more from current price).
- Width of wings: 3-5 points (defines max loss per side).
- Keep width equal on both sides for balanced risk.

**DTE:** 30-45 days.

**Management rules:**
- Close at 50% of total credit received.
- Close at 21 DTE.
- If either short strike is tested (stock trades within 1 point of short strike): close the tested side. Do not hold and hope.
- If loss reaches 2x total credit: close entire position.
- Do NOT try to "leg out" or adjust under pressure. Close and reassess.

**Example:**
```
AAPL at $180, range-bound. IV rank 55%.
Sell $170/$165 put spread: $0.80 credit.
Sell $190/$195 call spread: $0.70 credit.
Total credit: $1.50. Max risk: $5.00 - $1.50 = $3.50 per side.
Breakevens: $168.50 and $191.50.
Profit target: close at $0.75 total (50% collected).
```

---

## 8. Covered Call

**When to use:** The agent owns 100+ shares of a stock and is willing to sell at a higher price. Wants to generate income while waiting. Mildly bullish to neutral.

**Structure:** Own 100 shares + sell 1 OTM call per 100 shares owned.

**Max risk:** Stock declining (same risk as holding the stock; the premium provides a small cushion).
**Max reward:** (Strike - current price + premium) x 100. Capped at strike price.
**Breakeven:** Stock purchase price minus premium received.

**Strike selection:**
- 1 standard deviation OTM (delta 0.25-0.35).
- Above the next resistance level (so assignment means selling at a good price).
- 30-45 DTE.

**Management rules:**
- If option reaches 50% of credit: buy back, sell another at higher strike or later expiration (roll).
- If stock rallies above strike: allow assignment (selling at a good price) or roll up and out.
- If stock drops significantly: the covered call provides limited protection. Manage via the stock thesis.
- Never sell calls below your cost basis unless you are willing to realize a loss on assignment.

---

## 9. Cash-Secured Put

**When to use:** The agent wants to own a stock at a lower price. Sells a put at the desired purchase price and collects premium while waiting. Bullish long-term on the stock.

**Structure:** Sell 1 put at the desired purchase price. Reserve cash = strike x 100 in the account.

**Max risk:** Assignment at strike (owning the stock at that price minus premium). Max loss = (strike - premium) x 100 if stock goes to zero.
**Max reward:** Premium received (if stock stays above strike and put expires worthless).
**Breakeven:** Strike - premium received (this is the effective purchase price if assigned).

**Requirements:**
- Must actually want to own the stock at the strike price (this is not a neutral income play).
- Must have cash reserved for assignment (the "cash-secured" part).
- Stock must pass the same fundamental/technical screening as any other X.

**Strike selection:**
- At or below a strong support level.
- Delta 0.25-0.40 (slightly OTM).
- 30-45 DTE.

**Management rules:**
- If option reaches 50% of credit: buy back and re-evaluate.
- If assigned: welcome the shares into the portfolio and manage as a stock position.
- If stock crashes below strike: accept assignment. This is why you must want to own it.

---

## Forbidden strategies

The following are NOT allowed for this agent:

| Strategy | Reason |
|---|---|
| Naked short call | Unlimited loss potential |
| Naked short put (uncovered) | Large loss without cash reserve |
| Short straddle/strangle (naked) | Unlimited loss on at least one side |
| Ratio spreads (extra short legs) | Undefined risk on the extra legs |
| Calendar spreads (advanced) | Complex management, difficult to size risk |

If the agent encounters a scenario where these seem attractive, the answer is Z.

---

## Universal exit rules (all strategies)

1. **50% profit rule:** Close at 50% of max profit. The last 50% has the worst risk/reward.
2. **21 DTE rule:** Close by 21 DTE regardless of P&L. Gamma risk dominates inside 21 days.
3. **2x loss rule:** If loss exceeds 2x the max profit potential, close. The trade is broken.
4. **Event rule:** Close before earnings or major events unless the trade thesis is specifically about the event.
5. **Never hold to expiration.** Close 1-5 days before. Pin risk, assignment risk, after-hours gap risk.

## Cross-links

- `derivatives-options-and-futures/SKILL.md` (parent — philosophy and routing)
- `references/greeks.md` (understanding position Greeks)
- `risk-management` (max-loss = risk budget)
- `technical-indicators` (IV rank for strategy selection)
- `support-resistance-and-fibonacci` (strike selection relative to levels)

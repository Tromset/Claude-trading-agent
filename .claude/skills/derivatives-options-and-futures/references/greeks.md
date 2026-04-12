# The Greeks — Reference

The Greeks measure how an option's price changes in response to changes in underlying price, time, volatility, and interest rates. Understanding them is mandatory before entering any options position.

## Overview

| Greek | Measures sensitivity to | Range | Key insight |
|---|---|---|---|
| Delta | Underlying price change | -1.0 to +1.0 | Directional exposure; also approximates probability of expiring ITM |
| Gamma | Change in Delta per $1 move | 0 to ~0.10 | Acceleration; risk of delta blowing up near expiration |
| Theta | Time passage (1 day) | Negative for longs | The daily cost of holding an option; accelerates as expiration nears |
| Vega | 1% change in implied volatility | Positive for longs | Benefit/cost from vol expansion or contraction |
| Rho | 1% change in interest rates | Small | Usually negligible; relevant for LEAPS |

## Delta

### Intuition

Delta tells you how much the option price moves for a $1 move in the underlying. A call with delta 0.50 gains $0.50 when the stock rises $1.00. A put with delta -0.40 gains $0.40 when the stock falls $1.00.

### Numeric examples

```
AAPL at $180. Call strike $180 (ATM), 30 DTE.
Delta = 0.52

If AAPL moves to $181 (+$1):
  Option price change approx = 0.52 x $1.00 = +$0.52
  (1 contract = +$52)

If AAPL moves to $178 (-$2):
  Option price change approx = 0.52 x (-$2.00) = -$1.04
  (1 contract = -$104)
```

### How delta changes

| Factor | Effect on call delta | Effect on put delta |
|---|---|---|
| Stock price rises | Delta increases toward 1.0 | Delta increases toward 0 |
| Stock price falls | Delta decreases toward 0 | Delta decreases toward -1.0 |
| Time passes (DTE shrinks) | ATM stays ~0.50; OTM delta falls; ITM delta rises | Mirror of calls |
| IV increases | OTM delta increases; ITM delta decreases | Mirror of calls |
| IV decreases | OTM delta decreases; ITM delta increases | Mirror of calls |

### Delta as probability proxy

Delta approximately equals the probability the option expires in-the-money:
- Delta 0.80 call: ~80% chance of expiring ITM.
- Delta 0.20 call: ~20% chance of expiring ITM.
- This is a rough heuristic, not exact (it uses risk-neutral probability, not real-world).

### Delta for position sizing

Total delta exposure = contracts x delta x 100.
- 5 contracts at delta 0.40 = 200 delta-shares equivalent.
- This is useful for comparing options positions to stock positions.

## Gamma

### Intuition

Gamma is the rate of change of Delta. It answers: "If the stock moves $1, how much does my Delta change?" High gamma means your directional exposure is unstable — it will change rapidly with price.

### Numeric examples

```
AAPL at $180. Call strike $180, 30 DTE.
Delta = 0.52, Gamma = 0.04

AAPL moves from $180 to $181:
  New delta approx = 0.52 + 0.04 = 0.56
  The option is now MORE sensitive to the next $1 move.

AAPL moves from $180 to $179:
  New delta approx = 0.52 - 0.04 = 0.48
  The option is now LESS sensitive to the next $1 move.
```

### How gamma changes

| Factor | Effect on gamma |
|---|---|
| Near ATM | Gamma is highest |
| Deep ITM or deep OTM | Gamma is near zero |
| Time passes (DTE shrinks) | Gamma increases for ATM options (peaks at expiration) |
| IV increases | Gamma decreases (delta curve flattens) |
| IV decreases | Gamma increases (delta curve steepens) |

### Gamma risk near expiration

ATM options inside 7 DTE have explosive gamma. A $1 move can change delta from 0.50 to 0.90 in a single bar. This is why the agent closes positions at 21 DTE — gamma risk accelerates dangerously inside this window.

```
AAPL at $180. Call strike $180, 2 DTE.
Gamma = 0.15 (vs. 0.04 at 30 DTE)

$1 move changes delta by 0.15 — the position doubles its directional exposure overnight.
```

## Theta

### Intuition

Theta is the daily cost of holding an option. Every day that passes, the option loses value to time decay. Theta is always negative for long options (you pay it) and positive for short options (you collect it).

### Numeric examples

```
AAPL at $180. Call strike $180, 30 DTE.
Option price = $5.20, Theta = -0.12

After 1 day (no other changes):
  New price approx = $5.20 - $0.12 = $5.08
  (1 contract lost $12 to time decay)

After 1 weekend (2.5 calendar days of decay on Friday close):
  Loss approx = 2.5 x $0.12 = $0.30 per share
  (1 contract lost $30 over the weekend)
```

### How theta changes

| Factor | Effect on theta (magnitude) |
|---|---|
| ATM options | Highest theta decay |
| Deep ITM or deep OTM | Lower theta |
| Time passes (DTE shrinks) | Theta accelerates (non-linear — most decay in last 30 days) |
| IV increases | Theta increases (more extrinsic value to decay) |
| IV decreases | Theta decreases |

### Theta decay curve (non-linear)

Theta decay is NOT constant. Approximate daily decay as fraction of total time value:
- 60 DTE to 30 DTE: moderate, roughly linear.
- 30 DTE to 14 DTE: accelerating.
- 14 DTE to 0 DTE: exponential acceleration.

Rule: buy options with >= 45 DTE to minimize the steepest part of the decay curve. Sell options at 30-45 DTE to maximize the decay you collect.

## Vega

### Intuition

Vega measures how much the option price changes for a 1 percentage point change in implied volatility. Vega is positive for long options (you benefit from rising IV) and negative for short options (you benefit from falling IV).

### Numeric examples

```
AAPL at $180. Call strike $180, 30 DTE.
Option price = $5.20, Vega = 0.15, IV = 28%

If IV increases from 28% to 30% (+2 points):
  Price change = 2 x 0.15 = +$0.30
  New price approx = $5.50
  (1 contract gained $30 from vol expansion)

If IV decreases from 28% to 25% (-3 points):
  Price change = -3 x 0.15 = -$0.45
  New price approx = $4.75
  (1 contract lost $45 from vol contraction — "IV crush")
```

### How vega changes

| Factor | Effect on vega |
|---|---|
| More DTE | Higher vega (more time for vol to matter) |
| Less DTE | Lower vega (less time for vol to play out) |
| ATM options | Highest vega |
| Deep ITM or OTM | Lower vega |
| Higher IV | Slightly higher vega |

### IV crush (earnings, events)

Before earnings, IV rises (uncertainty). After earnings, IV collapses (uncertainty resolved). This is "IV crush."

```
Pre-earnings IV = 65%. Vega = 0.20. Option price = $8.00.
Post-earnings IV = 35% (drop of 30 points).
Price change from IV alone = -30 x 0.20 = -$6.00
New price = $2.00 (even if the stock moved in your direction!)
```

This is why buying options before earnings is forbidden. IV crush destroys long option positions even when direction is correct.

## Rho

### Intuition

Rho measures sensitivity to a 1% change in the risk-free interest rate. It is small for short-dated options and only meaningful for LEAPS (12+ months to expiration).

### Numeric examples

```
AAPL at $180. Call strike $180, 365 DTE (LEAPS).
Rho = 0.45

If rates increase by 1%:
  Option price increases by approx $0.45.
  (Calls benefit from higher rates; puts suffer)
```

For options with < 90 DTE, rho is negligible and can be ignored.

### Summary: Rho direction

- Long calls: positive rho (benefit from rate increases).
- Long puts: negative rho (benefit from rate decreases).
- Effect is proportional to DTE — only relevant for LEAPS.

## Greeks interaction summary

The Greeks do not operate in isolation. A single day produces changes in ALL Greeks simultaneously:

```
Day passes (theta):     Option loses time value.
Stock moves (delta):    Option gains/loses from direction.
Delta changes (gamma):  Directional exposure shifts.
IV changes (vega):      Option gains/loses from vol.
```

**Net P&L = delta P&L + theta P&L + vega P&L + (higher-order terms)**

For the agent's purposes: delta drives direction, theta is the holding cost, vega is the volatility bet, and gamma is the wild card near expiration. Manage all four.

## Cross-links

- `derivatives-options-and-futures/SKILL.md` (parent — when to use options)
- `references/options-strategies.md` (how Greeks interact within specific structures)
- `risk-management` (delta-equivalent sizing, max loss)
- `technical-indicators` (IV rank for vega context)

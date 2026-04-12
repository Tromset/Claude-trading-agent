# Order Type Matrix — Situation → Recommended Order

| # | Situation | Primary Order | TIF | Rationale | Slippage Risk | Example |
|---|---|---|---|---|---|---|
| 1 | Entering a swing breakout above a level | `STOP` (buy-stop) | `DAY` | Triggers only if price reaches the breakout level | Low–moderate | Buy-stop at $185.05 above $185 resistance |
| 2 | Entering a limit pullback to support | `LIMIT` | `GTC` | Fill at target price or better; no chase | None (may not fill) | Limit buy at $175 on a pullback to 50 EMA |
| 3 | Urgent exit: stop-loss hit | `MARKET` | `DAY` | Guaranteed fill, accept slippage | High in illiquid/volatile | Market sell after price breaches $170 stop |
| 4 | Placing a protective stop at entry | `STOP` (sell-stop) | `GTC` | Resting; fires automatically if price drops to stop | Moderate (can gap through) | Sell-stop at $177.80 on AAPL long |
| 5 | Precise stop with price guarantee | `STOP_LIMIT` | `GTC` | Fires at stop, but only fills at limit or better; risk of non-fill in gap | Low (but may not fill) | Stop $177.80 / Limit $177.50 |
| 6 | Taking profit at a target | `LIMIT` (sell) | `GTC` | Fill at target or better; resting order | None | Limit sell at $192 target |
| 7 | Kill-switch forced flatten | `MARKET` | `DAY` | Speed over price; must exit NOW | High (accepted) | Market sell all positions |
| 8 | Day-trade entry on opening range breakout | `STOP` | `DAY` | Entry above ORH triggers automatically | Low–moderate | Buy-stop at ORH + $0.10 |
| 9 | Day-trade close at end of session | `MOC` (Market on Close) | `DAY` | Guaranteed participation in closing auction | Low (auction fills) | MOC sell to flatten before close |
| 10 | Scaling into a winner (add leg) | `LIMIT` | `DAY` | Only add at planned pullback level | None | Limit buy at prior breakout level (retest) |
| 11 | Bracket: entry + stop + target together | `Bracket` (OTO/OCO) | `GTC` | All three legs placed atomically | Varies by leg | Entry limit $182, stop $177.80, target $192 |
| 12 | Trail a stop in profit | `TRAILING_STOP` | `GTC` | Auto-adjusts as price moves favorably | Moderate | Trail $3 below current price on a long |
| 13 | Pre-market / after-hours entry | `LIMIT` | `EXT` (extended) | Only limit orders allowed outside RTH | None (may not fill) | Limit buy in pre-market at $180 |
| 14 | Options: buy a call for directional bet | `LIMIT` | `DAY` | Options spreads are wide; never market-order options | None (critical) | Limit buy AAPL 190C at $3.50 mid |
| 15 | Options: closing a spread | `LIMIT` | `DAY` | Always use a limit to avoid giving up edge on multi-leg fills | None | Limit close debit spread at $1.00 |
| 16 | Futures: entering /ES on a pullback | `LIMIT` | `DAY` | Precise entry at a level | None | Limit buy 1 /ES at 5250 |
| 17 | Futures: stop on /ES position | `STOP` | `GTC` | Resting stop at invalidation | Moderate (limit-down risk) | Stop sell 1 /ES at 5220 |
| 18 | Crypto spot: buying BTC on breakout | `LIMIT` | `GTC` | Crypto spreads wider; limit avoids markup | None | Limit buy 0.1 BTC at $65,050 |
| 19 | Crypto perp: closing a long perp | `MARKET` | immediate | Perps can gap fast; prefer speed over price on exits | High | Market close BTC-PERP |
| 20 | Value investment DCA: monthly buy | `LIMIT` (mid-price) | `DAY` | Place at mid or slightly below ask; no urgency | None | Limit buy 10 KO at $61.50 |
| 21 | Conditional: buy A only if B breaks out | `OTO` (order triggers order) | `GTC` | First order triggers second; useful for correlated setups | Varies | If SPY > $450 → buy QQQ limit |
| 22 | Opening auction participation | `LOO` (Limit on Open) | `OPG` | Participate in opening auction at or below limit | Low | LOO buy AAPL at $183 or better |
| 23 | Closing auction participation | `LOC` (Limit on Close) | `DAY` | Participate in closing auction at or below limit | Low | LOC sell AAPL at $190 or better |
| 24 | Short entry with locate confirmed | `LIMIT` (sell short) | `DAY` | Short at resistance; must have locate | None | Limit sell-short 100 XYZ at $50.20 |
| 25 | Hedging a portfolio with index puts | `LIMIT` | `GTC` | Never market-order options; place limit at mid | None | Limit buy SPY 440P at $4.00 |

## Selection heuristic

```
IF urgency is maximum (kill-switch, stop-out, forced exit)
  → MARKET

ELSE IF entry at a specific price level (pullback, limit entry, options)
  → LIMIT

ELSE IF entry triggered only when price reaches a level (breakout)
  → STOP (buy-stop for longs, sell-stop for shorts)

ELSE IF want price protection on a stop (willing to risk non-fill)
  → STOP_LIMIT

ELSE IF want to place entry + stop + target atomically
  → BRACKET (OTO/OCO)

ELSE IF trailing dynamically in profit
  → TRAILING_STOP

ELSE IF participating in auction
  → MOC / MOO / LOC / LOO

ELSE IF extended hours
  → LIMIT with EXT TIF (only order type allowed outside RTH)
```

## TIF quick reference

| TIF | Meaning | Use when |
|---|---|---|
| `DAY` | Expires at session close | Default for most active trades |
| `GTC` | Good until cancelled (or 60–90 days) | Resting stops and targets |
| `IOC` | Immediate or cancel; partial fills OK | Large blocks seeking immediate liquidity |
| `FOK` | Fill or kill; all-or-nothing, immediate | Rare; when partial fill is useless |
| `EXT` | Extended hours (pre-market + after-hours) | Limit orders outside RTH only |
| `OPG` | Opening auction only | LOO/MOO orders |
| `CLO` | Closing auction only | LOC/MOC orders |

## Key rules

- **Never market-order options.** Spreads are too wide. Always limit at mid.
- **Never market-order illiquid instruments.** Slippage can exceed the stop distance.
- **Stop-limit on volatile instruments.** Prevents gap-through at the cost of non-fill risk.
- **Bracket everything you can.** Atomic stop + target reduces "forgot to place the stop" risk.
- **Day TIF for day trades.** Never leave a day-trade order GTC overnight.

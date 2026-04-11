# Position Sizing Formulas — Reference

## 1. Fixed fractional (default — use this)

```
qty = floor((account_equity × risk_pct) / stop_distance)
```

- `account_equity` — current total account value
- `risk_pct` — fraction willing to lose on this trade (default 0.01 = 1%)
- `stop_distance` — `|entry − stop|` in price units

**Example:** $50,000 account, 1% risk, entry $100, stop $97
- Risk budget = 50,000 × 0.01 = $500
- Stop distance = $3
- qty = floor(500 / 3) = 166

**Per-trade risk:** 166 × 3 = $498 (under budget, OK).

## 2. ATR-based fixed fractional (volatility-adaptive)

Same as (1) but the stop distance is set as a multiple of ATR:

```
stop_distance = k × ATR(n)
qty = floor((account_equity × risk_pct) / (k × ATR(n)))
```

Typical values: `k = 1.5`, `n = 14`.

**Example:** $50,000 account, 1% risk, ATR(14) = $2.00, k = 1.5
- Stop distance = 1.5 × 2 = $3.00
- qty = floor(500 / 3) = 166

Equivalent to (1) when the stop is placed at the ATR level.

## 3. Fixed dollar (simple, less adaptive)

```
qty = floor(fixed_dollar_amount / entry_price)
```

Ignores stop distance → ignores risk. **Not recommended** except for dollar-cost averaging long-term value positions where there is no stop.

## 4. Fixed shares (naive)

```
qty = N  // same every trade
```

Ignores everything. Not recommended except for automated DCA.

## 5. Kelly criterion (only after long backtest history; use fractional Kelly)

Full Kelly fraction:
```
f* = (p × b − (1 − p)) / b
```

Where:
- `p` = probability of winning
- `b` = payoff ratio (average win / average loss)

**Example:** 55% win rate, 2:1 avg R:R → `f* = (0.55 × 2 − 0.45) / 2 = 0.325` → full Kelly says risk 32.5% per trade.

**Why you don't use full Kelly:**
- Parameter estimates are noisy.
- Drawdown tolerance is human (or risk-manager) not mathematical.
- Full Kelly produces 50%+ drawdowns routinely.

**Fractional Kelly:** use ¼ or ⅛ of full. In the example: ¼ × 32.5% = ~8% per trade. Still aggressive. The default of 1% fixed fractional is ~12% of ¼ Kelly here — quite conservative, which is appropriate.

## 6. Volatility-normalized Kelly (advanced)

Scales Kelly by realized volatility — reduce size when volatility is elevated, increase when it compresses. Used by systematic funds. Implementation outside the scope of this library; mentioned for completeness.

## 7. Martingale, anti-martingale, pyramiding

- **Martingale (doubling after a loss):** FORBIDDEN. Guarantees ruin with finite bankroll.
- **Anti-martingale (increasing after a win):** allowed cautiously; formalized as pyramiding.
- **Pyramiding (scaling into winners):** allowed within the planned scale-in ladder; each leg is a separate X gated independently. Never scale into a losing position (that's averaging down, which is allowed only for value trades where the thesis is fundamentally-driven, never for technical trades).

## Edge cases

### Minimum meaningful size
If the computed `qty` is < 1 share (or the broker's minimum), either:
- Increase risk_pct temporarily up to 1.5% if the setup justifies it (rarely), or
- Skip the trade (emit Z).

**Do not** widen the stop to make a larger size fit — that's sizing by fitting, which is backwards.

### Fractional shares
If the broker supports fractional shares, use `floor(x × 100) / 100` for 2-decimal shares, etc. Always round down.

### High-priced instruments
If the instrument is expensive (e.g., BRK.A at $500,000/share), fractional shares or an alternative vehicle (BRK.B) is required.

### Leveraged instruments
Leverage multiplies both sides of the equation. For a 3× leveraged ETF, treat the effective exposure as 3× the notional and adjust the risk budget downward accordingly (use 0.33% of account instead of 1% for a 3× leveraged instrument, to keep effective exposure constant).

### Futures and options
- **Futures:** `qty` is contracts, not shares. Risk = (stop distance in ticks) × (tick value) × contracts.
- **Options:** `qty` is contracts (100 shares each). Risk = premium paid (for long options) or max loss computed from the payoff diagram (for defined-risk spreads). Naked short options have undefined risk and must NOT be sized using fixed fractional.

## Summary cheatsheet

| Situation | Formula |
|---|---|
| Standard swing/day trade with a technical stop | Fixed fractional (1) |
| Higher volatility or volatile instrument | ATR-based (2) |
| DCA long-term value buy | Fixed dollar (3) |
| Proven systematic strategy with long history | ¼ Kelly (5) |
| Scaling into a winner | Pyramiding (legs sized independently) |
| Doubling down on a loser | FORBIDDEN (exc. fundamental value) |

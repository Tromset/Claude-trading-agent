---
name: risk-management
description: Use before every X or Y to size positions, place stops, compute risk, enforce caps, and produce the numeric inputs that buy-sell-hold-decision needs to emit a valid action.
---

# Risk Management

No `X` is allowed without a risk-management output. Period. This skill produces the numbers: position size, stop distance, target, per-trade risk, portfolio heat, and the final gate.

## When to use this skill

- Before every proposed `X` (entry).
- Before every proposed `Y` (exit) to confirm the exit still respects portfolio heat constraints.
- Periodically (every bar of an open trade) to recompute heat and verify the stop is still valid.
- When the account balance changes (deposits, withdrawals, realized P&L).
- When volatility (ATR) expands or contracts meaningfully.

**Anti-triggers:** do NOT use this skill to generate trade ideas. Risk-management *sizes* ideas; it doesn't *produce* them.

## Prerequisites

- A proposed trade with a direction, an entry level, and a technical stop level (from the strategy skill).
- Current account equity.
- Current portfolio positions and their stops (for heat calc).
- Current ATR(14) of the instrument on the strategy timeframe.

## Core concepts

### Per-trade risk = the money you lose if the stop hits

`per_trade_risk = (entry_price - stop_price) × qty` for longs
`per_trade_risk = (stop_price - entry_price) × qty` for shorts

This is the only meaningful measure of risk on a single trade. Percentage of account is a function of equity; ATR multiples are a function of volatility. Currency at risk is the authoritative number.

### Risk caps (the three that matter)

| Cap | Default | Hard/Soft |
|---|---|---|
| Per-trade risk | 1% of account equity | Hard |
| Daily loss | 3% of account equity | Hard (kill switch) |
| Portfolio heat (sum of all open per-trade risks) | 6% of account equity | Hard |

Conservative defaults. The agent may use smaller caps (e.g., 0.5% per trade) but never larger.

### Position sizing formula (fixed fractional)

```
risk_budget = account_equity × per_trade_risk_pct
stop_distance = |entry_price - stop_price|
qty = floor(risk_budget / stop_distance)
```

Examples:
- Account $50,000, risk 1% = $500. Stop is $2.00 below entry → 250 shares.
- Account $50,000, risk 1% = $500. Stop is $10 below entry → 50 shares.
- Account $50,000, risk 1% = $500. Stop is $0.40 below entry → 1,250 shares (cap by share limit if any).

### Stop placement (where to put the stop)

Stops must be placed at levels the market would have to *invalidate the thesis* to reach — not arbitrary dollar amounts.

Canonical stop rules:
- **Structural stop:** below the most recent swing low (long) / above the swing high (short).
- **ATR stop:** `1.5 × ATR(14)` beyond the entry.
- **Pattern stop:** the natural level below the chart pattern (flag low, H&S neckline, etc.).
- **Time stop:** exit after N bars regardless of price (soft; emits Y with `TIME_STOP`).

Use the widest of the structural/ATR/pattern stops. A too-tight stop that gets wicked out by noise is worse than no stop.

### Target placement (R:R ≥ 2:1 minimum)

Default rule: target distance = 2 × stop distance. This produces a 2:1 reward:risk ratio, which is the minimum for a positive-expectancy strategy at 40% win rate.

Better: place the target at the next significant technical level (prior swing high, HTF resistance, Fib extension) and check that it yields ≥ 2R. If not → reduce to a 2R target or skip the trade (`Z`).

### Portfolio heat

`portfolio_heat = sum(per_trade_risk_i for all open positions i) / account_equity`

Must stay ≤ 6% at all times.

**Correlation adjustment:** positions in correlated instruments (e.g., two tech megacaps) should have their combined risk counted as 1.5× the sum. The heat model doesn't trust diversification across correlated names.

### Kelly sizing (reference only — do not use full Kelly)

Full Kelly is mathematically optimal but emotionally intolerable and highly sensitive to parameter error. Use **fractional Kelly (¼)** at most — and only after 200+ trades of statistical history on a stable strategy.

Default recommendation: stick with fixed 1% per trade until the strategy is proven.

## Decision procedure

1. Receive the proposed trade (ticker, direction, entry level, stop level, target level, strategy source).
2. Validate the stop — is it at a technical level or an arbitrary dollar amount? If arbitrary → ask the strategy for a technical stop or reject.
3. Compute `stop_distance = |entry - stop|`.
4. Compute `atr = ATR(14)` on the strategy's timeframe. If `stop_distance < 0.8 × atr` → stop is too tight → widen to `1.5 × atr` or reject.
5. Compute `target_distance = |target - entry|`. If `target_distance < 2 × stop_distance` → R:R too low → reduce target or reject.
6. Compute `risk_budget = account_equity × 0.01`.
7. Compute `qty = floor(risk_budget / stop_distance)`. Round down, always.
8. Compute `per_trade_risk = qty × stop_distance`. Verify ≤ risk budget.
9. Compute `portfolio_heat_after = (current_heat + per_trade_risk) / account_equity`. If > 6% → reduce qty until heat ≤ 6%, or reject if reduced qty < minimum meaningful size.
10. Apply correlation adjustment if any existing position is in a correlated instrument.
11. Check against confidence rubric from `buy-sell-hold-decision`:
    - Confidence 60–79 → multiply qty by 0.5 (half-size on reduced conviction).
    - Confidence < 60 → reject (emit Z upstream).
12. Emit the sizing output JSON (schema below).

## Heuristics & thresholds

- **Always round down.** Fractional shares may be available, but round down on size — under-sized is safer than over-sized.
- **Stop before target.** Define the stop first. The target is derived from the stop via R:R, not the other way around.
- **ATR-based stops for volatility adaptation.** A fixed-dollar stop is wrong across changing volatility regimes.
- **Tightening stops ≠ better risk.** Tightening a stop into a pullback locks in losses. Trail after 1R of favorable movement, not before.
- **Per-trade cap is a maximum, not a target.** If a setup only justifies 0.5% risk (lower conviction), size at 0.5%.
- **Correlation blind spot.** The heat model is naive to correlation; treat correlated positions as 1.5× their sum.

## Common failure modes

- **Sizing by gut.** "100 shares feels right." Forbidden. Size is computed, not guessed.
- **Ignoring portfolio heat.** Opening the 7th position without checking total risk.
- **Rounding up qty.** Always round down.
- **Widening stops after entry.** Forbidden.
- **Skipping the ATR check.** A $0.10 stop on a name with $1.50 ATR will get wicked out immediately.
- **Using gross $ instead of risk $.** "I'm buying $5000 of AAPL" does not tell you your risk. Risk is stop distance × qty.
- **Assuming 1% risk is conservative enough in drawdown.** During a losing streak, 1% compounds badly; consider scaling down (see `references/kelly-and-heat.md`).

## Outputs expected

```json
{
  "skill": "risk-management",
  "decision": "approve" | "reject",
  "ticker": "NASDAQ:AAPL",
  "direction": "LONG" | "SHORT",
  "qty": 119,
  "entry_price": 182.05,
  "stop_price": 177.80,
  "target_price": 192.00,
  "stop_distance": 4.25,
  "target_distance": 9.95,
  "risk_reward_ratio": 2.34,
  "risk_budget_currency": 500.00,
  "per_trade_risk_currency": 505.75,
  "portfolio_heat_before": 0.022,
  "portfolio_heat_after": 0.032,
  "atr_14": 2.80,
  "stop_vs_atr_multiple": 1.52,
  "confidence_multiplier": 1.0,
  "caps_passed": ["per-trade", "daily-loss", "portfolio-heat", "atr-min"],
  "rejection_reasons": [],
  "notes": "..."
}
```

If `decision = reject`, `buy-sell-hold-decision` must emit `Z-OVERRIDE` with `blocking_skill: risk-management`.

## References (lazy-load)

- `references/position-sizing-formulas.md` — all sizing methods with worked examples.
- `references/kelly-and-heat.md` — Kelly derivation, why ¼ Kelly max, heat math including correlation.

## Cross-links

- Pairs with: `buy-sell-hold-decision` (consumer), `safety-and-kill-switch` (caps), `trade-journaling-and-backtesting` (records sizing decisions), every strategy skill (provides stop level input).

---
name: fundamental-analysis-and-value-investing
description: Use when evaluating a stock as a long-horizon value candidate to decide whether the business is a Buffett-style "wonderful business at a fair price" worth owning for a decade. Covers 10-K reading, moat analysis, owner earnings, intrinsic value, margin of safety, and the conservative X/Y/Z output for value trades.
---

# Fundamental Analysis & Value Investing

This is the **heart** of the agent's identity. The project README is explicit: this is a Claude-Warren-Buffett value-investing bot. Everything else — charts, indicators, news — is in service of answering one question: *is this business worth owning at this price?*

> **Not financial advice.** Educational content only. Past performance is not indicative of future results.

## When to use this skill

**Triggers:**
- A candidate ticker is being evaluated for a long-horizon buy (months to years, ideally decades).
- `watchlist-and-screening` has surfaced a name that passed the quantitative filter.
- A watchlist holding has released a new 10-K / 10-Q and needs re-underwriting.
- Price has dropped meaningfully (> 20%) on an existing thesis and the agent must decide: thesis broken (`Y`) or Mr. Market gift (`X`)?
- User asks "should I buy COMPANY?" in a non-trading-app context.

**Anti-triggers:**
- Do NOT use for intraday or day-trading decisions — value work runs on 10-year horizons, not 10-minute ones.
- Do NOT use to justify an already-decided trade — the checklist runs *before* the thesis, not after.
- Do NOT use to screen from scratch — that's `watchlist-and-screening`. This skill *evaluates* a named candidate.

## Prerequisites

- Candidate ticker with at least 10 years of audited financial statements (5 minimum; prefer 10).
- Most recent 10-K, 10-Q, and proxy statement available.
- `watchlist-and-screening` output (or equivalent) confirming the name is inside the circle of competence.
- Current market cap, share count, and price.
- `risk-management` is NOT a prerequisite here (the sizing happens later) — but value trades are sized tiny until conviction is extreme.

## Core concepts

### 1. The owner mindset

You are not buying a ticker. You are buying a fractional share of a business. Ask: *"If the market closed tomorrow for ten years and I could not sell, would I still want to own this?"* If no → `Z`.

### 2. Circle of competence

Only evaluate businesses you can explain in three sentences:
- What does it sell?
- Who pays for it, why, and at what price?
- How does it make money on each sale, and why won't that stop?

If any sentence is fuzzy → outside circle → `Z`. Buffett rejected most tech for decades because he couldn't answer #3 with confidence. Better to miss a winner than to buy something you don't understand.

### 3. Moat (durable competitive advantage)

A moat is what keeps competitors from eroding returns on capital over the next 10+ years. Five canonical sources:

| Moat type | Examples | Durability check |
|---|---|---|
| Brand / intangible | Coca-Cola, Ferrari, Moody's | Pricing power without volume loss |
| Network effect | Visa, exchanges, marketplaces | Value grows with users |
| Switching cost | Enterprise software, payroll | Customer retention > 95% |
| Cost advantage | GEICO, Costco, Nucor | Lowest unit cost in industry |
| Toll bridge / scale | Railroads, pipelines, utilities | Regulatory or geographic monopoly |

No moat → commodity business → `Z`. "We have a great product" is not a moat. "We charge 20% more than competitors and customers still come back" is.

### 4. Owner earnings (Buffett's preferred earnings measure)

```
owner_earnings = net_income
               + depreciation
               + amortization
               + other non-cash charges
               - maintenance_capex
               - incremental_working_capital_required_to_maintain_volume
```

Differs from GAAP net income (understates non-cash charges) and from free cash flow (which subtracts ALL capex, not just maintenance). Owner earnings is what the business would distribute to a sole owner who did not want to grow it.

Maintenance capex is hard to back out — Buffett estimates it as "the capex required to keep unit volume flat." A rough proxy: D&A, or slightly above D&A in asset-heavy businesses.

### 5. Intrinsic value (the DCF you should not over-engineer)

Intrinsic value = sum of discounted future owner earnings until judgment day.

Simple rule: if you need a spreadsheet with 37 cells of assumptions to justify a purchase, the margin of safety isn't there. Buffett: *"If you need a computer or calculator to decide whether to buy, you shouldn't buy it."*

See `references/dcf-worked-example.md` for the mechanics. Headline: terminal value dominates, so your growth and discount assumptions completely dictate the answer. Prefer ranges over point estimates.

### 6. Margin of safety

Buy at a price that is meaningfully below your best estimate of intrinsic value, so that even if you are wrong on the growth rate, the discount rate, and the moat durability, you still don't lose.

**Default hurdle: current price ≤ 0.7 × central intrinsic-value estimate.**

If price is 0.7–0.9 × intrinsic → `Z` (watch, but not a margin-of-safety buy).
If price is 0.9–1.1 × intrinsic → `Z` (fair value, nothing to do).
If price is > 1.1 × intrinsic and it's an existing holding → consider `Y` only if thesis has also broken; otherwise still `Z` (don't sell wonderful businesses for tax bills).

### 7. Wonderful business vs fair business

> "It's far better to buy a wonderful company at a fair price than a fair company at a wonderful price." — Buffett, 1989

Prefer high-ROIC, low-capital-intensity businesses with long reinvestment runways at a reasonable (not cheap) price, over statistically cheap mediocre businesses that will compound capital poorly. A 15% ROIC business compounds; a 6% ROIC business dilutes.

### 8. Mr. Market

The market offers a price every day. Some days he is euphoric, some days panicked. He is a *servant*, not a guide. If his price is attractive → use it. If his price is absurd → ignore it. Never let his mood dictate yours.

## How to read a 10-K (in this order)

1. **Business description (Item 1)** — what do they actually do? In their own words. If you can't restate it simply → outside circle.
2. **Risk factors (Item 1A)** — read all of them. Sorted roughly by severity. Focus on risks that could impair the moat.
3. **MD&A (Item 7)** — management's own narrative. Watch for changes in tone year-over-year. Defensive language is a signal.
4. **Financial statements** — income statement, balance sheet, cash flow statement, 10-year summary if available.
5. **Footnotes** — especially: revenue recognition, segment reporting, stock-based comp, pensions, leases, contingencies, related-party transactions.
6. **Proxy statement** — compensation structure, insider ownership, board independence.

Red flags in a 10-K: frequently restated financials, aggressive revenue recognition, goodwill > 50% of assets and growing, heavy reliance on non-GAAP metrics, CEO pay uncorrelated to long-term performance, frequent auditor changes.

## Decision procedure

1. **Circle of competence check.** Write the three-sentence description. If you can't → `Z` immediately. Stop.
2. **Business quality filter.** Run the 30-item Buffett checklist (`references/buffett-checklist.md`). Require ≥ 25/30 to continue. Else → `Z`.
3. **Moat identification.** Name the moat type and the durability evidence. If none → `Z`.
4. **Financial statement review.** Read the last 10 years of: revenue, operating margin, ROIC, FCF, debt levels, share count. Require: ROIC > 12% in 8 of 10 years, FCF positive in 9 of 10 years, debt/equity < 0.5 (or covered by interest coverage > 8×). Else → `Z`.
5. **Management review.** Proxy statement + last 5 shareholder letters. Require: honest language, capital allocation history that did not destroy value (buybacks below intrinsic, acquisitions at reasonable multiples, reasonable comp).
6. **Compute owner earnings** for the trailing year and the average of the trailing five years.
7. **Intrinsic value estimation.** Two methods, cross-check:
   - Simple: average owner earnings × reasonable P/E for the quality (typically 12–18×).
   - DCF: 10-year projection + terminal value at Gordon growth. See `references/dcf-worked-example.md`.
   - If the two methods disagree by > 30% → you don't understand the business well enough → `Z`.
8. **Margin of safety.** Is current price ≤ 0.7 × central intrinsic estimate? If no → `Z`.
9. **News/macro overlay.** Check `news-and-macro-awareness` for pending catalysts. Blackout window active → `Z`.
10. **Risk sizing.** Defer to `risk-management`. Value entries are tiny (0.25–0.5% per-trade risk is typical, since stops are wide or absent and conviction compounds over years, not days).
11. **Emit via `buy-sell-hold-decision`.** `X` only if all prior steps passed. Otherwise `Z` with `blocking_skill` set.

**Reminder:** In a typical year Buffett makes single-digit actual buys across a 50-name portfolio. The agent should expect `Z` in > 99% of value evaluations. `X` is rare and special.

## Heuristics & thresholds

- **ROIC > 12% for 8 of last 10 years** — else no compounding, pass.
- **FCF positive in 9 of 10 years** — one bad year is fine; a pattern is not.
- **Debt/equity < 0.5** — or interest coverage > 8× if leverage is structural (utility, REIT).
- **Gross margin stability within ±3%** over the decade — collapsing margins are a moat in decay.
- **Share count flat or declining** — steady dilution signals weak capital discipline.
- **Intrinsic-value hurdle: price ≤ 0.7 × central estimate**.
- **Maximum concentration in a single name: 10% of portfolio at cost**; 20% at market after it compounds (don't trim winners cheaply).
- **Sell triggers** (rare): thesis broken (moat eroded, management turned crooked, ROIC collapsed), or price > 2× intrinsic AND you have something meaningfully better with a margin of safety. Do NOT sell on price alone.
- **Holding period: indefinite by default.** If your selling rule is "when it goes up X%," you are not a value investor.

## Common failure modes

- **Falling in love with a story.** Narrative is not moat. Numbers are.
- **Anchoring to past price.** "It was $100 last year and now it's $60 so it's cheap." Irrelevant. Only intrinsic value matters.
- **Over-engineered DCF.** Ten tabs of assumptions hide the fact that you don't know. Prefer a ranges-based sanity check.
- **Ignoring reinvestment runway.** A wonderful business with nowhere to reinvest compounds at the discount rate, not at its ROIC.
- **Short-circuiting the circle of competence.** If you didn't understand it last year, you don't understand it this year. Stop.
- **Treating "cheap on P/E" as a value signal.** Cyclicals are cheapest at the top of the cycle. Look at normalized earnings.
- **Confusing volatility with risk.** Price dropping 30% while the business thrives is opportunity, not risk.
- **Selling to realize a gain.** Buffett's favorite holding period is forever.

## Outputs expected

```json
{
  "skill": "fundamental-analysis-and-value-investing",
  "ticker": "NYSE:KO",
  "in_circle_of_competence": true,
  "checklist_score": 27,
  "moat": {
    "type": "brand / intangible",
    "durability_evidence": "100+ year brand, distribution scale, pricing power through inflation cycles",
    "durability_years_est": 20
  },
  "owner_earnings_ttm": 9.8e9,
  "owner_earnings_5y_avg": 9.1e9,
  "intrinsic_value_per_share": 48.00,
  "current_price": 62.00,
  "price_to_intrinsic": 1.29,
  "margin_of_safety_met": false,
  "decision_vs_xyz": "Z",
  "reason": "Price 1.29x intrinsic, above 0.7x hurdle. Quality business but no margin of safety at current price.",
  "confidence": 78,
  "notes": "Add to watchlist; re-evaluate if price < $34."
}
```

If `decision_vs_xyz = X`, downstream `risk-management` and `buy-sell-hold-decision` must still run. This skill does not bypass the gate chain.

## References (lazy-load)

- `references/buffett-checklist.md` — the 30-item qualifying filter.
- `references/dcf-worked-example.md` — fully worked DCF on a hypothetical mature company.
- `references/financial-ratios.md` — all 25+ ratios with formulas, interpretation, ranges.

## Cross-links

- Upstream: `watchlist-and-screening` (surfaces candidates), `trading-master` (routes long-horizon requests here).
- Downstream: `risk-management` (sizes the rare value `X`), `buy-sell-hold-decision` (emits final `X`/`Y`/`Z`), `trade-journaling-and-backtesting` (records the thesis for future re-underwriting).
- Related: `news-and-macro-awareness` (short-term catalysts are usually noise for value, but blackout rules still apply).

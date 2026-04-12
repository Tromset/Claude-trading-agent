---
name: watchlist-and-screening
description: Use when building, maintaining, or routing from the candidate universe -- top-down and bottom-up screens, watchlist hygiene, tier management, and the gate that decides which names flow to fundamental-analysis-and-value-investing for full evaluation.
---

# Watchlist & Screening

The watchlist is the funnel. Nothing gets evaluated, sized, or traded unless it first earns a place on the list. This skill governs how names enter, how they are maintained, and how they exit -- either upward into a full fundamental analysis or downward into discard.

> **Not financial advice.** Educational content only.

## When to use this skill

**Triggers:**
- The agent has no active candidates and needs to source new ideas.
- A scheduled 30-day refresh cycle has elapsed.
- A macro regime change has invalidated part of the current list.
- User asks "what should I be looking at?" or "find me candidates."
- A sector rotation or earnings season has changed the opportunity set.

**Anti-triggers:**
- Do NOT use to evaluate a specific name in depth -- that is `fundamental-analysis-and-value-investing`.
- Do NOT use to execute a trade -- that is downstream of analysis, sizing, and decision skills.
- Do NOT use to react to breaking news on an existing holding -- that is `news-and-macro-awareness`.

## Prerequisites

- Access to a financial data source with 5+ years of fundamentals (10-K data, ratios).
- A defined circle of competence (sectors/industries the agent understands well enough to evaluate).
- Current portfolio state (to avoid redundant screening of existing holdings).
- Knowledge of the agent's strategy mandate (value investing, long-horizon, Buffett-style).

## Core concepts

### 1. Top-down vs. bottom-up screening

**Top-down:** Start with the economy, narrow to sectors, then to industries, then to individual names.
- Macro regime (expansion/contraction) guides sector weight preferences.
- Sector tailwinds (secular trends, demographic shifts, regulatory changes) surface industries.
- Within an industry, screen quantitatively for the best operators.

**Bottom-up:** Start with individual business quality, ignore macro entirely.
- Buffett's preferred approach: find wonderful businesses regardless of cycle.
- Screen the entire investable universe against quality and valuation filters simultaneously.
- The economy takes care of itself if you own great businesses at fair prices.

**Agent default:** Bottom-up primary, top-down as a secondary sanity check. The agent does not time sectors.

### 2. Quantitative screens (hard filters)

These are binary pass/fail gates. A name must pass ALL to enter the watchlist.

| Filter | Threshold | Rationale |
|---|---|---|
| ROIC (5-year median) | > 12% | Earning above cost of capital consistently |
| Debt-to-Equity | < 0.5 | Conservative balance sheet (or interest coverage > 8x if structural leverage) |
| Free cash flow positive | 5 of last 5 years | Cash generation is non-negotiable |
| P/E (trailing, normalized) | < 15 | Valuation discipline; not overpaying |
| P/FCF | < 15 | Confirms P/E is not misleading via accounting |
| Market cap | > $2B | Sufficient liquidity, audited financials, institutional coverage |
| Share count trend | Flat or declining over 5 years | No chronic dilution |

A name that fails any single filter is immediately rejected. No exceptions.

### 3. Qualitative filters (soft gates)

After quantitative screens, apply judgment-based filters:

- **Moat identification.** Can you name the moat type in one sentence? If not, pass.
- **Circle of competence.** Can you explain what the business does, who pays, and why they keep paying? If not, pass.
- **Management integrity.** Any history of fraud, restatements, egregious comp, or related-party abuse? If yes, pass.
- **Secular headwinds.** Is the industry in structural decline (newspapers, tobacco in certain jurisdictions, legacy retail)? If yes, requires extraordinary margin of safety.
- **ESG red flags.** Not a moral filter but a risk filter: regulatory/litigation risk from environmental or governance issues.

### 4. Watchlist tiers

The watchlist has three tiers with different attention levels:

| Tier | Max names | Review frequency | Criteria |
|---|---|---|---|
| **Core** | 10 | Weekly | Passed all screens, moat confirmed, circle of competence clear, waiting for price to hit margin-of-safety zone. Ready for full underwriting on price trigger. |
| **Satellite** | 10 | Bi-weekly | Passed quantitative screens, qualitative work partially done, needs more research before promotion to Core. |
| **Watch** | 10 | Monthly | Interesting but not yet screened fully, or currently too expensive but worth monitoring. Ideas in waiting. |

**Total watchlist cap: 30 names.** More than 30 means you are hoarding, not focusing. If you want to add #31, you must remove one first.

### 5. Watchlist hygiene

- **Refresh cycle: every 30 calendar days.** On refresh:
  - Re-run quantitative screens on all 30 names. Any that now fail a hard filter → remove.
  - Check if any Core names have hit margin-of-safety price → route to `fundamental-analysis-and-value-investing`.
  - Check if any Watch/Satellite names deserve promotion (new data, research completed).
  - Remove names where the thesis has gone stale (> 90 days with no development or price movement toward target).
- **Earnings trigger.** When a watchlist name reports earnings, re-screen within 3 trading days.
- **Price alert trigger.** When a Core name drops within 10% of margin-of-safety price, escalate attention to daily review.

### 6. Only buy what is on the list

This is a hard rule. The agent may NOT emit `X` for any ticker that is not currently on the Core tier of the watchlist. Impulse buys are forbidden. The screening process exists precisely to prevent emotional or FOMO-driven entries.

Exception: none. If it isn't on the list, it cannot be bought. Period.

## Decision procedure

### Adding a name to the watchlist

1. **Source the idea.** Screener output, sector scan, peer comparison, user suggestion, or 52-week-low list.
2. **Run quantitative filters.** All seven must pass. Any failure → reject immediately.
3. **Circle of competence check.** Write three sentences describing the business. If you cannot → reject.
4. **Moat hypothesis.** Name the moat type. If none apparent → reject.
5. **Assign tier.** If qualitative work is complete and price is near target → Core. If partial → Satellite. If early stage → Watch.
6. **Check capacity.** Is the tier full (10 names)? If yes, you must identify the weakest existing name to remove before adding.
7. **Record entry.** Log: ticker, date added, tier, moat hypothesis, target price range, thesis in one paragraph.

### Removing a name from the watchlist

1. **Quantitative failure.** Any hard filter failed on refresh → remove. No debate.
2. **Thesis invalidation.** Moat impaired, management fraud, structural industry collapse → remove.
3. **Staleness.** On watchlist > 90 days with no price approach to target and no new thesis-relevant information → remove.
4. **Capacity management.** A better candidate needs the slot → compare conviction levels → remove the weaker.
5. **Purchased.** Name was bought (X emitted and filled) → moves from watchlist to portfolio tracker.

### Routing from watchlist to fundamental analysis

A Core-tier name is routed to `fundamental-analysis-and-value-investing` when ANY of:
- Price drops to within 10% of the estimated margin-of-safety price.
- A material event occurs (earnings miss, CEO change, acquisition) that may change intrinsic value.
- The 30-day refresh reveals improved fundamentals that might tighten the valuation range.
- User explicitly requests a full evaluation of the name.

The routing output includes: ticker, current price, estimated fair value range, moat hypothesis, and the specific trigger that prompted escalation.

## Heuristics & thresholds

- **ROIC > 12% for 5-year median** — the single most important quality filter.
- **D/E < 0.5** — or interest coverage > 8x for structurally leveraged industries.
- **FCF positive all 5 years** — no exceptions; cash is king.
- **P/E < 15 and P/FCF < 15** — valuation discipline; these can be relaxed to 18 for exceptional quality (ROIC > 20%) but never above 20.
- **Max 30 names total** — focus over breadth.
- **30-day refresh mandatory** — stale lists breed complacency.
- **90-day staleness removal** — if nothing happened in 90 days, it wasn't interesting enough.
- **Core names only for X** — no impulse buys, no exceptions.

## Common failure modes

- **Screen creep.** Relaxing filters "just this once" because a name seems interesting. The screens exist to override your enthusiasm. Never relax them.
- **Hoarding names.** A 50-name watchlist is not a watchlist; it is a bookmark folder you never open. Cap at 30.
- **Stale list syndrome.** Not refreshing for 60+ days. The world changes; your list must too.
- **Tier inflation.** Everything is "Core" because you like them all. Core means ready-to-buy-on-price-trigger. Be honest about readiness.
- **Confusing screening with analysis.** Screening tells you a name is *worth looking at*. Analysis tells you whether to buy. Do not buy based on screens alone.
- **Ignoring the circle of competence.** Passing quantitative screens does not mean you understand the business. Plenty of high-ROIC businesses are outside your circle.
- **Anchoring to addition price.** "It was cheaper when I added it to the list" is irrelevant. Only current price vs. current intrinsic value matters.
- **FOMO additions.** Adding a name because it just went up 20% and you missed it. That is the opposite of value investing.

## Outputs expected

```json
{
  "skill": "watchlist-and-screening",
  "action": "add" | "remove" | "promote" | "demote" | "refresh" | "route-to-analysis",
  "ticker": "NYSE:LOW",
  "tier": "core" | "satellite" | "watch",
  "quantitative_pass": true,
  "filters": {
    "roic_5yr_median": 0.28,
    "debt_to_equity": 0.42,
    "fcf_positive_years": 5,
    "pe_trailing": 13.8,
    "p_fcf": 14.2,
    "market_cap_B": 142.0,
    "share_count_trend": "declining"
  },
  "moat_hypothesis": "Cost advantage via scale + switching costs in contractor relationships",
  "circle_of_competence": true,
  "target_price_range": [180, 210],
  "current_price": 245,
  "margin_of_safety_price": 155,
  "thesis_one_paragraph": "...",
  "watchlist_count_after": 27,
  "date_added": "2026-03-15",
  "next_review": "2026-04-14",
  "decision_vs_xyz": "Z",
  "reason": "Added to Core tier. Price $245 is well above MOS price $155. Monitor for pullback.",
  "route_to_analysis": false
}
```

## References (lazy-load)

- `fundamental-analysis-and-value-investing/references/financial-ratios.md` — ratio definitions and thresholds used in quantitative screens.
- `fundamental-analysis-and-value-investing/references/buffett-checklist.md` — the 30-item qualifier run after a name is routed from watchlist to analysis.

## Cross-links

- Upstream: `trading-master` (routes screening requests here), user input (ticker suggestions).
- Downstream: `fundamental-analysis-and-value-investing` (receives routed candidates from Core tier), `buy-sell-hold-decision` (cannot emit X unless name is Core-tier).
- Related: `news-and-macro-awareness` (macro regime informs top-down overlay), `risk-management` (portfolio heat may limit how many Core names can be bought simultaneously).

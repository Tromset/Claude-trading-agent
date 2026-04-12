# Buffett Checklist — 30-Item Value Candidate Filter

The canonical pre-qualification filter for any candidate considered for a long-horizon value trade. Each item scores 1 (yes) or 0 (no/unclear). **Minimum score to qualify as a Buffett-style candidate: 25 of 30.** Below 25 → `Z`, regardless of price.

This is a filter, not a formula. A single "no" on a critical item (circle of competence, moat presence, management integrity) can veto a candidate with a score in the 25+ range — see "veto items" below.

> **Not financial advice.** Educational checklist derived from Berkshire Hathaway letters, *The Essays of Warren Buffett* (Cunningham), *The Warren Buffett Way* (Hagstrom), and Charlie Munger's mental-models framing. Buffett himself never published "30 rules."

## Section 1 — Business (6 items)

| # | Item | Pass criteria |
|---|---|---|
| 1 | **Simple business.** I can describe it in 3 sentences. | Yes / No |
| 2 | **In circle of competence.** I know how the business makes money, what could disrupt it, and why. | Yes / No |
| 3 | **Predictable product.** The product/service will still exist and be needed in 10 years in roughly its current form. | Yes / No |
| 4 | **Not dependent on commodity pricing.** Revenue is not primarily dictated by a commodity the company cannot control (oil, copper, wheat). | Yes / No |
| 5 | **Customer concentration low.** No single customer > 20% of revenue, no top 5 > 40%. | Yes / No |
| 6 | **Geographic / channel diversification.** Not dependent on a single distribution channel or single country beyond home market. | Yes / No |

**Veto:** Item 2 (circle of competence). If this is a No, stop. Do not score further. Return `Z`.

## Section 2 — Moat (6 items)

| # | Item | Pass criteria |
|---|---|---|
| 7 | **Identifiable moat type.** Brand / network / switching cost / cost advantage / toll bridge — name it. | Yes / No |
| 8 | **Pricing power.** Company raised prices above inflation in at least 5 of last 10 years without volume loss. | Yes / No |
| 9 | **ROIC > 12% sustained.** 8 of last 10 years. | Yes / No |
| 10 | **Gross margin stable or rising.** No secular decline > 3 percentage points over last decade. | Yes / No |
| 11 | **No major new entrant success.** No new entrant has captured > 10% of the moat holder's share in the last 10 years. | Yes / No |
| 12 | **Moat widening, not narrowing.** Management actions and industry trends strengthen, not erode, the advantage. | Yes / No |

**Veto:** Item 7. No nameable moat → commodity business → `Z`.

## Section 3 — Management (6 items)

| # | Item | Pass criteria |
|---|---|---|
| 13 | **Honest communication.** Shareholder letters describe mistakes candidly; language is plain, not promotional. | Yes / No |
| 14 | **Skin in the game.** Insider ownership > 2% (founder-led) OR > $10M held by CEO (hired management). | Yes / No |
| 15 | **Capital allocation: buybacks at reasonable prices.** Historical buybacks executed when price was ≤ 1.2× intrinsic estimate, not at peaks. | Yes / No |
| 16 | **Capital allocation: acquisitions sensible.** Last 10 years of acquisitions did not destroy value (no serial goodwill impairments, no wildly overpriced deals). | Yes / No |
| 17 | **Compensation aligned.** CEO/exec pay tied to multi-year operating performance, not stock-price targets or single-year EPS. | Yes / No |
| 18 | **No scandals / restatements.** No material accounting restatements, no SEC investigations, no repeated auditor changes in last 10 years. | Yes / No |

**Veto:** Item 13 (honest communication) and Item 18 (no scandals). Dishonest management is a terminal disqualifier.

## Section 4 — Financials (6 items)

| # | Item | Pass criteria |
|---|---|---|
| 19 | **Consistent earnings.** Net income positive in 10 of last 10 years (no losses at trough of cycle). | Yes / No |
| 20 | **FCF positive.** Free cash flow positive in 9 of last 10 years. | Yes / No |
| 21 | **Low leverage.** Debt/equity < 0.5 OR interest coverage > 8× if leverage is structural to the industry. | Yes / No |
| 22 | **Working capital stable.** No ballooning receivables or inventories relative to revenue. | Yes / No |
| 23 | **Share count flat or shrinking.** Diluted shares outstanding did not grow > 1% annualized over the last decade (ex major M&A). | Yes / No |
| 24 | **Goodwill reasonable.** Goodwill < 50% of total assets; no major impairment in last 5 years. | Yes / No |

## Section 5 — Price & Horizon (6 items)

| # | Item | Pass criteria |
|---|---|---|
| 25 | **Intrinsic value estimable.** I can produce a central intrinsic-value estimate with a ±30% range I can defend. | Yes / No |
| 26 | **Margin of safety available.** Current price ≤ 0.7 × central intrinsic-value estimate. | Yes / No |
| 27 | **Owner earnings computable.** I can compute owner earnings from the 10-K without guessing more than one major input. | Yes / No |
| 28 | **Reinvestment runway.** Management can reinvest retained earnings at ROIC ≥ 12% for at least the next 5 years. | Yes / No |
| 29 | **Willing to hold for 10 years if the market closed tomorrow.** Mental test: if trading were suspended for a decade, would I still want this? | Yes / No |
| 30 | **Position fits portfolio.** Not correlated > 0.7 with an existing top-5 holding; portfolio concentration check passes. | Yes / No |

**Veto:** Item 26 (margin of safety) and Item 29 (10-year hold test). These are the twin pillars of the philosophy.

## Scoring

| Score | Meaning | Action |
|---|---|---|
| 28–30 | High-quality candidate with clear margin of safety | Proceed to full DCF, then `risk-management`, then consider `X` |
| 25–27 | Qualifies; something is borderline | Proceed only if no veto items failed; size smaller |
| 22–24 | Does not qualify | `Z`; keep on watchlist; re-run next year |
| < 22 | Not a value candidate | `Z`; remove from watchlist |

**Any veto item = No** → automatic `Z`, even if total score is 29. The veto items are: 2 (circle), 7 (moat exists), 13 (honest mgmt), 18 (no scandals), 26 (margin of safety), 29 (10-year hold).

## Using the checklist

- Run it on every candidate before any DCF work. A 15/30 business is not redeemable by being "cheap."
- Document the evidence for each item — a citation from the 10-K, a specific number, a dated press release. "Gut feel yes" is a "no."
- Re-run the checklist annually on every holding. If a holding drops below 25, the thesis is broken and the skill emits `Y`.
- If you find yourself arguing *for* a yes on a borderline item, it's probably a no. Buffett: "The smartest side to take in a bidding war is the losing side."

## Output format

```json
{
  "skill": "fundamental-analysis-and-value-investing/buffett-checklist",
  "ticker": "NYSE:KO",
  "scores": {
    "1": 1, "2": 1, "3": 1, "4": 1, "5": 1, "6": 1,
    "7": 1, "8": 1, "9": 1, "10": 1, "11": 1, "12": 0,
    "13": 1, "14": 1, "15": 1, "16": 1, "17": 1, "18": 1,
    "19": 1, "20": 1, "21": 1, "22": 1, "23": 1, "24": 1,
    "25": 1, "26": 0, "27": 1, "28": 0, "29": 1, "30": 1
  },
  "total": 27,
  "vetoes_failed": ["26"],
  "qualifies": false,
  "notes": "Quality business but no margin of safety at current price; watch."
}
```

## Cross-links

- Parent skill: `fundamental-analysis-and-value-investing/SKILL.md`
- Sibling references: `dcf-worked-example.md`, `financial-ratios.md`
- Downstream: `risk-management`, `buy-sell-hold-decision`, `watchlist-and-screening`

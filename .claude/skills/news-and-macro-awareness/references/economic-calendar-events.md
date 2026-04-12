# Economic Calendar Events Reference

A comprehensive table of major scheduled macroeconomic events that the agent must monitor. Each entry includes release timing, frequency, market impact, and prescribed agent behavior.

> **Not financial advice.** Educational content only.

---

## Event table

| # | Event | Source | Frequency | Typical time (ET) | Impact | Typical volatility | Agent behavior during | Agent behavior after |
|---|---|---|---|---|---|---|---|---|
| 1 | **FOMC Rate Decision** | Federal Reserve | 8x/year | 14:00 | HIGH | 50-150 bps S&P intraday range | Blackout +/- 15 min. No X or Y. | Wait for statement + presser digest. Assess regime shift vs. consensus. Resume after 14:45. |
| 2 | **FOMC Minutes** | Federal Reserve | 8x/year (3 weeks post-decision) | 14:00 | MEDIUM-HIGH | 20-60 bps | Blackout +/- 5 min. | Read for tone shifts vs. statement. Usually less impactful than decision itself. |
| 3 | **CPI (Consumer Price Index)** | BLS | Monthly (10th-14th) | 08:30 | HIGH | 30-100 bps | Blackout +/- 5 min. | Compare headline vs. core vs. consensus. Persistent misses shift rate expectations. Re-assess rate-sensitive holdings. |
| 4 | **PPI (Producer Price Index)** | BLS | Monthly (day after or near CPI) | 08:30 | MEDIUM | 15-40 bps | Blackout +/- 5 min. | Leading indicator for CPI. Large surprises warrant review of margin assumptions for holdings. |
| 5 | **Non-Farm Payrolls (NFP)** | BLS | Monthly (first Friday) | 08:30 | HIGH | 30-80 bps | Blackout +/- 5 min. | Focus on: headline jobs, unemployment rate, wages. Strong = hawkish rates, weak = dovish. Context matters more than single print. |
| 6 | **GDP (advance/prelim/final)** | BEA | Quarterly | 08:30 | HIGH (advance), MEDIUM (revisions) | 20-60 bps (advance) | Blackout +/- 5 min for advance. | Advance print has most impact. Revisions priced unless large. Negative print triggers recession evaluation. |
| 7 | **PCE Price Index** | BEA | Monthly (last week) | 08:30 | HIGH | 20-50 bps | Blackout +/- 5 min. | Fed's preferred inflation measure. Often more important than CPI for policy expectations. |
| 8 | **Retail Sales** | Census Bureau | Monthly (mid-month) | 08:30 | MEDIUM-HIGH | 15-40 bps | Blackout +/- 5 min. | Consumer spending health. Exclude autos for core trend. Impacts consumer discretionary thesis. |
| 9 | **ISM Manufacturing PMI** | ISM | Monthly (first business day) | 10:00 | MEDIUM-HIGH | 15-40 bps | Blackout +/- 5 min. | Above 50 = expansion. Below 50 = contraction. New orders sub-index is forward-looking. |
| 10 | **ISM Services PMI** | ISM | Monthly (third business day) | 10:00 | MEDIUM | 10-30 bps | Blackout +/- 5 min. | Services = 70%+ of economy. Persistently weak readings signal broad slowdown. |
| 11 | **S&P Global PMI (flash)** | S&P Global | Monthly (3rd-4th week, flash) | 09:45 | MEDIUM | 10-25 bps | Monitor, no strict blackout. | Earlier than ISM; provides directional preview. |
| 12 | **Unemployment Claims (initial)** | DOL | Weekly (Thursday) | 08:30 | LOW-MEDIUM | 5-15 bps | No blackout unless trending to extreme. | Watch 4-week moving average. Single prints are noisy. Sustained rise above 300K = warning. |
| 13 | **Consumer Confidence (CB)** | Conference Board | Monthly (last Tuesday) | 10:00 | MEDIUM | 10-25 bps | No strict blackout. | Expectations sub-index more forward-looking than present conditions. |
| 14 | **U. Michigan Consumer Sentiment** | U. Michigan | Monthly (prelim mid-month, final end-month) | 10:00 | MEDIUM | 10-20 bps | No strict blackout. | Inflation expectations sub-index matters most for Fed policy. |
| 15 | **Housing Starts & Permits** | Census Bureau | Monthly | 08:30 | LOW-MEDIUM | 5-15 bps | No blackout. | Leading indicator for housing/construction sector. Permits lead starts by 1-2 months. |
| 16 | **Existing Home Sales** | NAR | Monthly | 10:00 | LOW-MEDIUM | 5-15 bps | No blackout. | Lagging vs. permits/starts. Price data (median) useful for inflation context. |
| 17 | **Durable Goods Orders** | Census Bureau | Monthly (4th week) | 08:30 | MEDIUM | 10-30 bps | No strict blackout. | Ex-transportation and ex-defense core capital goods = business investment proxy. |
| 18 | **Trade Balance** | Census/BEA | Monthly | 08:30 | LOW | 5-10 bps | No blackout. | Matters for GDP math and currency-sensitive holdings. Rarely a market mover on its own. |
| 19 | **JOLTS (Job Openings)** | BLS | Monthly (6-week lag) | 10:00 | MEDIUM | 10-25 bps | No strict blackout. | Openings-to-unemployed ratio is a Fed-watched indicator. Quits rate signals worker confidence. |
| 20 | **ADP Employment** | ADP | Monthly (2 days before NFP) | 08:15 | MEDIUM | 10-25 bps | No strict blackout. | NFP preview, but correlation is imperfect. Large surprise sets expectations for Friday. |
| 21 | **Beige Book** | Federal Reserve | 8x/year (2 weeks before FOMC) | 14:00 | LOW-MEDIUM | 5-15 bps | No blackout. | Qualitative / anecdotal. Sets tone for FOMC discussion. Read for regional/sector color. |
| 22 | **Fed Speakers** | Various (FOMC members) | Variable | Variable | LOW-HIGH (depends on speaker + topic) | 5-30 bps | No blackout unless Chair. | Chair Powell = near-Tier-1. Other voting members > non-voting. Watch for phrases that deviate from last statement. |
| 23 | **ECB Rate Decision** | ECB | ~6x/year | 08:15 (ET) | MEDIUM (for US markets) | 10-30 bps in EUR, 5-15 bps S&P | No strict blackout for US equities. | Matters for global rate regime, USD strength, multinational earnings. |
| 24 | **BoJ Rate Decision** | Bank of Japan | 8x/year | Overnight (ET: ~23:00-03:00) | LOW-MEDIUM (for US) | Yen pairs volatile; S&P 5-15 bps | No blackout (occurs outside US session). | Matters if BoJ shifts yield curve control. Carry trade unwinds can spike global vol. |
| 25 | **BoE Rate Decision** | Bank of England | 8x/year | 07:00 (ET) | LOW-MEDIUM (for US) | 10-20 bps in GBP, 5-10 bps S&P | No strict blackout for US equities. | UK-exposed holdings may need review. |

---

## Impact classification guide

| Impact level | Definition | Agent rule |
|---|---|---|
| **HIGH** | Routinely moves S&P 500 > 30 bps, changes rate expectations, reprices multiple sectors. | Mandatory blackout +/- 5 min (15 min for FOMC). No X or Y during window. |
| **MEDIUM-HIGH** | Moves S&P 15-30 bps when surprising. Does not change regime alone but contributes to narrative. | Blackout +/- 5 min recommended. Agent may choose Z by default. |
| **MEDIUM** | Moves S&P 10-20 bps on surprise. Sector-specific impact. | No mandatory blackout. Agent should be aware but may act if setup is strong and unrelated to the event. |
| **LOW-MEDIUM** | Moves S&P 5-15 bps. Context-dependent. | No blackout. Monitor for trend confirmation. |
| **LOW** | Rarely moves broad market. May affect specific sectors. | No blackout. Background information only. |

---

## Weekly schedule template (typical)

| Day | Time (ET) | Common events |
|---|---|---|
| **Monday** | 10:00 | ISM (if first business day), Fed speakers |
| **Tuesday** | 08:30, 10:00 | PPI, JOLTS, Consumer confidence, housing data |
| **Wednesday** | 08:15, 08:30, 10:00, 14:00 | ADP, CPI (mid-month), FOMC (8x/year), Beige Book |
| **Thursday** | 08:30 | Unemployment claims, retail sales, durable goods, ECB (variable) |
| **Friday** | 08:30, 10:00 | NFP (first Friday), GDP, Michigan sentiment, PCE (end of month) |

Note: This is a generalized template. Actual dates vary month to month. Always verify against the current calendar.

---

## Agent behavior summary by event type

### Pre-event (T-24h to T-5min)

- Identify the event and its consensus estimate.
- Check if any open position or pending X has direct exposure to the event outcome.
- If directly exposed and event is HIGH impact → do not initiate new X. Existing positions remain (stops protect).
- Log the event in the daily scan output.

### During event (T-5min to T+5min, or T+15min for FOMC)

- Emit Z for any proposed X or Y. Reason: "blackout window active."
- Do not interpret price action during this window. Initial moves are unreliable.
- No stop adjustments during blackout (stops remain at pre-set levels; do not panic-widen or panic-tighten).

### Post-event (T+5min to T+60min)

- Read the actual release vs. consensus. Categorize: beat, miss, or in-line.
- Assess whether the result changes the macro regime (single data point rarely does).
- Check if any holding's thesis is affected (e.g., CPI surprise → rate expectations shift → REIT/utility thesis impacted).
- If thesis invalidation is possible → route to `fundamental-analysis-and-value-investing` for re-evaluation.
- If thesis unaffected → resume normal operations.

### Post-event (T+1 day and beyond)

- Monitor follow-through. Did the initial market reaction hold or reverse?
- Update the running macro narrative (is inflation trending? Is growth decelerating?).
- Adjust watchlist sector weights if macro regime is shifting (top-down overlay).

---

## Earnings season overlay

Earnings are not on the economic calendar but create a similar volatility environment.

| Period | Approximate dates | Agent behavior |
|---|---|---|
| Q4 earnings | Jan 15 - Feb 25 | No new X on names reporting within 3 trading days. |
| Q1 earnings | Apr 15 - May 25 | Same rule. |
| Q2 earnings | Jul 15 - Aug 25 | Same rule. |
| Q3 earnings | Oct 15 - Nov 25 | Same rule. |

After a watchlist name reports:
- Beat on quality metrics (revenue, margins, guidance) → confirmation, strengthens thesis.
- Miss on quality metrics → re-evaluate thesis within 3 days. May be noise or may be structural.
- Guidance cut → treat as potential invalidation. Route to analysis skill.

---

## Interaction with other skills

| Skill | How this reference helps |
|---|---|
| `watchlist-and-screening` | Macro regime context for sector weighting during refreshes. |
| `fundamental-analysis-and-value-investing` | Event-driven re-underwriting triggers (earnings, regulatory). |
| `risk-management` | VIX regime informs whether to use standard (1%) or reduced (0.5%) per-trade risk. |
| `buy-sell-hold-decision` | Blackout window forces Z override. Sentiment adjusts confidence +/- 10%. |
| `safety-and-kill-switch` | Black swan events (3+ sigma moves) may independently trigger kill switch. |

---

## Cross-references

- Parent skill: `news-and-macro-awareness/SKILL.md`
- Related: `risk-management/references/kelly-and-heat.md` (volatility regime affects sizing)
- Related: `watchlist-and-screening/SKILL.md` (refresh cycle should account for earnings season)

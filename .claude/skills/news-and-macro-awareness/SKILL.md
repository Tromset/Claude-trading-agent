---
name: news-and-macro-awareness
description: Use when evaluating how macroeconomic events, news releases, and sentiment gauges affect the agent's X/Y/Z decisions -- economic calendar awareness, news blackout rules, sentiment interpretation, and source hygiene.
---

# News & Macro Awareness

The market is not a vacuum. Macro events move prices, shift regimes, and invalidate theses. This skill equips the agent to monitor the information environment without becoming a slave to it. News informs but does not dictate -- the value framework remains primary.

> **Not financial advice.** Educational content only.

## When to use this skill

**Triggers:**
- Before any proposed `X` or `Y`, to check for imminent macro events that warrant a blackout.
- When a high-impact event (FOMC, CPI, NFP) is within 24 hours.
- When sentiment gauges reach extreme readings (VIX > 30, put/call > 1.2, Fear & Greed < 20).
- When breaking news may invalidate an existing thesis on a portfolio holding.
- During the daily pre-market routine to flag the day's calendar events.
- When the agent needs to decide if a price move is noise or signal.

**Anti-triggers:**
- Do NOT use to generate trade ideas from news headlines. News is a filter, not a signal generator.
- Do NOT use to day-trade around events. The agent is a value investor, not a news trader.
- Do NOT use to override a strong fundamental thesis based on a single data point. Noise is noise.

## Prerequisites

- Access to an economic calendar with event times, consensus estimates, and impact ratings.
- Current VIX level and recent trend.
- Current put/call ratio (equity, not index).
- Awareness of any open positions and their thesis basis (to check for invalidation).
- Knowledge of the current market session (pre-market, regular, after-hours).

## Core concepts

### 1. The economic calendar

Major scheduled events that move markets. The agent must know what is coming before it acts.

**Tier 1 (High impact) -- always check before any X/Y:**
- FOMC rate decision and statement (8x/year)
- CPI (monthly)
- Non-Farm Payrolls / NFP (monthly, first Friday)
- GDP (quarterly, advance/preliminary/final)
- PCE (monthly, Fed's preferred inflation gauge)

**Tier 2 (Medium impact) -- check if trading that day:**
- PPI (monthly)
- Retail sales (monthly)
- ISM Manufacturing/Services PMI (monthly)
- Consumer confidence (monthly)
- Unemployment claims (weekly)
- Housing starts (monthly)
- Durable goods orders (monthly)

**Tier 3 (Lower impact but contextually relevant):**
- Trade balance (monthly)
- JOLTS (monthly)
- ADP employment (monthly)
- Beige Book (8x/year)
- Fed speakers (variable)
- Foreign central bank decisions (ECB, BoJ, BoE)

See `references/economic-calendar-events.md` for the full table with times, frequencies, and agent behavior rules.

### 2. News blackout rule

**The agent must NOT emit X or Y within +/- 5 minutes of a high-impact scheduled event.**

Rationale: Liquidity evaporates around major releases. Spreads widen. Slippage spikes. The first move is often reversed. Acting in this window is gambling, not investing.

Implementation:
- If a high-impact event is scheduled within the next 5 minutes → emit `Z` with reason "blackout window active."
- If a high-impact event occurred within the last 5 minutes → emit `Z` with reason "post-event settling, blackout active."
- After the 5-minute post-event window, the agent may resume normal operations.
- For FOMC specifically, extend the blackout to +/- 15 minutes (the statement + press conference create extended volatility).

### 3. Sentiment gauges

Sentiment is contrarian at extremes and meaningless in the middle.

| Gauge | Extreme fear | Neutral | Extreme greed | Agent behavior |
|---|---|---|---|---|
| **VIX** | > 30 | 15-20 | < 12 | Fear = opportunity for value buys. Greed = caution, tighten watchlist standards. |
| **Put/call ratio (equity)** | > 1.2 | 0.7-0.9 | < 0.5 | High = bearish crowd (contrarian bullish). Low = complacent crowd (contrarian bearish). |
| **AAII Bull-Bear spread** | Bears > Bulls by 20+ | Balanced | Bulls > Bears by 30+ | Extreme bearishness historically precedes above-average returns over 6-12 months. |
| **CNN Fear & Greed Index** | < 20 | 40-60 | > 80 | Same contrarian logic. Extreme fear = better entry odds. Extreme greed = patience. |

**How sentiment affects X/Y/Z:**
- Extreme fear + strong fundamental thesis + margin of safety → strengthens case for `X`.
- Extreme greed + fully valued positions → consider tightening stops, raising bar for new `X`.
- Neutral sentiment → no modification to base decision.
- Sentiment alone NEVER triggers X or Y. It modifies conviction on an existing thesis by +/- 10% confidence.

### 4. News categories and their impact on decisions

| News type | Impact on X/Y/Z | Agent behavior |
|---|---|---|
| **Thesis invalidation** (fraud, moat collapse, regulatory ban) | Strong Y signal | Re-evaluate immediately. If thesis is broken → Y regardless of price. |
| **Thesis confirmation** (earnings beat on quality metrics, moat evidence) | Potential X reinforcement | Does NOT trigger X alone. Strengthens existing case if price is at margin-of-safety. |
| **Ambiguous / noise** (analyst upgrades, price target changes, social media buzz) | Z | Ignore. Analyst opinions are not data. Social media is not research. |
| **Macro regime shift** (recession confirmed, rate cycle turns) | Sector-level reassessment | Review watchlist sector weights. Individual theses may or may not be affected. |
| **Black swan** (pandemic, war, financial crisis) | Portfolio-wide Z + review | Halt all new X. Review every open position for thesis validity. May present generational value opportunities -- but only after careful analysis, not in the panic itself. |

### 5. Source hygiene

Not all information is equal. The agent prioritizes sources in this order:

**Primary sources (high trust):**
- SEC filings (10-K, 10-Q, 8-K, proxy statements)
- Company earnings calls (transcript, not summaries)
- Federal Reserve releases (FOMC statement, minutes, dot plot)
- Bureau of Labor Statistics / BEA / Census releases
- Exchange filings and corporate actions

**Secondary sources (moderate trust, verify claims):**
- Major financial press (WSJ, FT, Bloomberg, Reuters)
- Industry publications and trade journals
- Peer-reviewed academic research

**Tertiary sources (low trust, entertainment only):**
- Cable financial news (CNBC, Fox Business)
- Social media (Twitter/X, Reddit, StockTwits)
- Anonymous blog posts and newsletters
- Aggregator sites (Yahoo Finance comments, Seeking Alpha)

**Rules:**
- Never trade on a social media rumor.
- Always trace a claim back to its primary source before acting.
- If a news item cannot be verified from a primary source within 30 minutes, treat it as unconfirmed → Z.
- "Everyone is talking about it" is a contrarian signal, not a confirmation signal.

### 6. Earnings season protocol

During earnings season (4 weeks starting approximately Jan 15, Apr 15, Jul 15, Oct 15):
- Monitor all watchlist names for report dates.
- Do NOT initiate new X within 3 trading days before a watchlist name reports (event risk).
- After earnings: re-screen within 3 trading days. Did the report confirm or invalidate the thesis?
- Gap-up on earnings is NOT a buy signal (you missed the entry). Gap-down on earnings MIGHT be if the thesis remains intact and margin of safety expands.

## Decision procedure

1. **Daily pre-market scan.** Check the economic calendar for today's events. Flag any Tier 1 events → set blackout windows.
2. **Sentiment snapshot.** Record VIX, put/call ratio, and AAII/Fear & Greed if at extremes. If all neutral → no sentiment modification.
3. **News scan.** Review overnight and pre-market headlines for any watchlist or portfolio names. Categorize each as: invalidation, confirmation, ambiguous, or irrelevant.
4. **Invalidation check.** If any holding has thesis-invalidating news → immediate escalation to `fundamental-analysis-and-value-investing` for re-underwriting. Potential Y.
5. **Blackout enforcement.** Before any X or Y proposed by another skill, verify no blackout window is active. If active → override to Z with `blocking_skill: news-and-macro-awareness`.
6. **Sentiment adjustment.** If sentiment is at extremes and an X or Y is being considered, adjust confidence by +/- 10% (extreme fear helps X, extreme greed hinders X).
7. **Pass through.** If no blackout, no invalidation, and no extreme sentiment → this skill adds no friction. Let the upstream decision proceed unmodified.

## Heuristics & thresholds

- **Blackout: +/- 5 min for Tier 1 events, +/- 15 min for FOMC.**
- **VIX > 30 = extreme fear.** Historically favorable for 12-month forward returns. Does not guarantee short-term bottom.
- **VIX < 12 = extreme complacency.** Raise the bar for new X.
- **Put/call > 1.2 = contrarian bullish.** Put/call < 0.5 = contrarian bearish.
- **AAII bears exceed bulls by 20+ = historically bullish 6-12 month signal.**
- **Sentiment modifies confidence by max +/- 10%.** It never flips X to Y or vice versa.
- **Unverified news = Z.** No exceptions.
- **3-day earnings blackout.** No new X within 3 trading days before a watchlist name reports.
- **Social media is noise.** Period.

## Common failure modes

- **Trading the headline.** Reacting to a news headline without reading the primary source. Headlines are designed to provoke, not inform.
- **Anchoring to the first move.** The initial reaction to an event is often wrong. The 5-minute blackout exists for this reason.
- **Confusing noise with signal.** Most news is noise. A daily GDP revision by 0.1% does not change a 10-year thesis.
- **Letting sentiment override fundamentals.** "Everyone is bearish so I should buy" is only valid if the business is fundamentally sound AND cheap. Contrarian sentiment is a tiebreaker, not a thesis.
- **Calendar ignorance.** Entering a position 10 minutes before NFP and getting stopped out on the spike. Preventable.
- **Recency bias.** The last data point feels more important than the trend. One bad jobs report does not mean recession. One good one does not mean boom.
- **Source conflation.** Treating a Reddit post and an SEC filing as equivalent evidence. They are not even in the same universe.
- **Paralysis by analysis.** There is always a reason not to act. News awareness should clarify, not paralyze. If the macro environment were always perfect, there would never be a margin of safety.

## Outputs expected

```json
{
  "skill": "news-and-macro-awareness",
  "date": "2026-04-12",
  "time_et": "08:15",
  "blackout_active": false,
  "next_tier1_event": {
    "event": "CPI",
    "time_et": "08:30",
    "minutes_until": 15,
    "blackout_starts": "08:25"
  },
  "sentiment": {
    "vix": 22.4,
    "vix_regime": "elevated",
    "put_call_ratio": 0.95,
    "put_call_signal": "neutral",
    "aaii_spread": -8,
    "aaii_signal": "neutral",
    "fear_greed": 35,
    "fear_greed_signal": "mildly_fearful"
  },
  "sentiment_confidence_adjustment": 0,
  "news_flags": [
    {
      "ticker": "NYSE:KO",
      "category": "confirmation",
      "headline": "Q1 organic revenue +7%, ahead of consensus",
      "source_tier": "primary",
      "action": "none -- strengthens existing thesis but price not at MOS"
    }
  ],
  "invalidations": [],
  "decision_override": null,
  "decision_vs_xyz": "Z",
  "reason": "CPI in 15 min. Blackout starts at 08:25. No action until 08:35."
}
```

## References (lazy-load)

- `references/economic-calendar-events.md` — full table of 20+ events with frequencies, times, impact levels, and agent behavior rules.

## Cross-links

- Upstream: `trading-master` (routes macro questions here), `watchlist-and-screening` (macro regime informs sector overlay).
- Downstream: `buy-sell-hold-decision` (this skill can block or modify confidence), `fundamental-analysis-and-value-investing` (news can trigger re-underwriting).
- Parallel: `risk-management` (VIX regime may inform position sizing), `safety-and-kill-switch` (black swan events may trigger kill switch independently).

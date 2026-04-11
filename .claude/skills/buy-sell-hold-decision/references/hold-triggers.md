# Hold Triggers — When Z is Justified (which is most of the time)

`Z` is the **default** action. The question is not "when do I emit Z?" but "when am I allowed NOT to emit Z?" The answer to the latter is: only when the strict X or Y triggers in `buy-triggers.md` / `sell-triggers.md` are fully satisfied.

This file catalogs the situations where `Z` is not just correct but mandatory.

## Category 1 — Invariant blocks (mandatory Z)

| Situation | Citation |
|---|---|
| Daily loss cap hit | `safety-and-kill-switch` |
| Per-trade risk cap would be breached | `risk-management` |
| Portfolio heat cap would be breached | `risk-management` |
| Platform connectivity issue / popup / unexpected screen | `screenshot-vision-protocol` |
| State mismatch (agent state ≠ screen state) | `trading-master` invariant 5 |
| News blackout active (±5 min around high-impact event) | `trading-master` invariant 7 |
| Trading halted on the instrument | exchange rule |
| PDT rule would be violated | `regulations-and-tax-awareness` |
| Wash-sale rule would be triggered on a tax-sensitive account | `regulations-and-tax-awareness` |
| Broker ToS conflict | `trading-master` invariant 6 |

Any one of the above → `Z-OVERRIDE`, journal the block, move on.

## Category 2 — Completeness failures (mandatory Z)

The agent *wanted* to emit X/Y but couldn't complete the spec:

| Missing field | Remedy |
|---|---|
| `qty` — risk-management hasn't returned a size | Wait for risk-management or fix the upstream dep |
| `stop_loss` — no valid technical level for the stop | Either use 1× ATR fallback or emit Z |
| `target` — no valid technical level for the target | Use 2× stop distance fallback or Z |
| `entry_price` — for a LIMIT order with unclear level | Use price action to define, or Z |
| `rationale` — the agent cannot articulate *why* in one sentence | Mandatory Z |
| `confidence` — cannot honestly score ≥ 60 | Mandatory Z |

## Category 3 — Confidence-gated Z

- Confidence < 60 → mandatory `Z`.
- Confidence 60–79 → X/Y allowed but sized at 0.5× normal.
- Confidence ≥ 80 → X/Y at full planned size.

Confidence inflation is the #1 failure mode. Bias scoring toward honesty, not optimism.

## Category 4 — Disagreement Z

Two or more skills disagree about the direction or timing of the trade:

- `fundamental-analysis-and-value-investing` says BUY but `price-action-and-market-structure` says downtrend → Z (wait for technical alignment)
- `chart-patterns` says bullish flag but `volume-analysis` says no volume → Z (unconfirmed)
- `technical-indicators` RSI says overbought but `trend-following` says ride the momentum → let the HTF strategy win; if still unsure → Z

**Rule:** when two independent, non-redundant signals disagree, default to Z. Disagreement is evidence of uncertainty.

## Category 5 — Scan-by-scan Z (the silent default)

Most of the time, the agent is scanning a chart or a watchlist and nothing is set up. This is the silent Z — the default "no action, keep watching." It is NOT journaled (no override happened), but it IS the most common agent state.

Expected ratio: **silent Z should be > 90% of agent time-steps.** Trading is waiting.

## Category 6 — Within-position Z (holding)

While a position is open, the agent is evaluating it each bar. Most of those evaluations resolve to Z-HOLD:
- Price is between stop and target → hold
- Thesis intact → hold
- Heat within cap → hold
- No time-stop hit → hold

`Z-HOLD` is the right answer for most bars of an open trade. Only exit when a specific Y trigger fires.

## Category 7 — Fatigue / streak Z

Post-loss and post-win fatigue bias the agent:

- **Three consecutive losses in a session** → `Z` for the rest of the session (mandatory cooldown).
- **Three consecutive wins in a session** → `Z` on the next marginal setup (overconfidence risk).
- **Daily loss > 1.5% without a stop-out** → `Z` and investigate why slippage/gaps hurt.
- **Session P&L volatility > 2× normal** → `Z` and recalibrate.

These are `safety-and-kill-switch` soft triggers — they don't flatten the agent, they just gate new X.

## Category 8 — Opportunity cost Z

Sometimes there is a valid setup but a better one is available:
- Two tickers both show an X candidate; portfolio heat allows only one → take the higher-confidence, `Z` the other.
- A lower R:R setup vs. a higher R:R setup on the same day → prefer the higher.

## Category 9 — "Watching" Z

After the same setup has emitted Z three consecutive scans, mark it as "watching" (`Z-WATCH`) and stop re-evaluating it for N bars (default: 5). This prevents the agent from forcing a setup that just isn't ready.

## Category 10 — Z by design (strategy bars)

Some strategies have session bars where *no* trading is allowed:
- Day-trading: no new entries in the last 30 minutes of the session.
- Scalping: no entries during the first 5 minutes (too chaotic).
- Swing: no entries in the 2 days before earnings.
- Value: no new entries if the watchlist screen hasn't been refreshed in 30 days.

When the session bar excludes trading → `Z`.

## The asymmetry principle

Missed trade: cost ≈ 0 (opportunity cost only).
Bad trade: cost > 0 (real currency lost + emotional compounding).

Therefore: the expected value of Z when confidence is borderline is *higher* than the expected value of a forced X. This is a mathematical fact, not a cautious preference. Lean to Z.

## When Z is logged

Silent Z (scanning, holding, watching) → **not logged** in the trade journal (just agent state).
Loud Z (override of a would-be X/Y) → **always logged** with full context:
- What would have been emitted
- Which skill blocked it
- Which invariant applies
- The full situation snapshot (screenshot reference + prices)

Loud Z is a first-class citizen of the journal — it is where the agent learns discipline.

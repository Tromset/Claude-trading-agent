# Full Routing Decision Tree (with worked examples)

The routing decision tree in `trading-master/SKILL.md` is the short form. This is the long form with worked examples.

## Top-level gate (always run first)

```
STEP 0. safety + state check
  a. Is any kill-switch condition active? (daily loss, anomaly, platform disconnect)
     → load safety-and-kill-switch → emit Z. STOP.
  b. Is the screen readable and unambiguous?
     → if no: screenshot-vision-protocol → emit Z until readable. STOP.
  c. Is the agent's state consistent with the screen?
     → if no: abort to safety-and-kill-switch → emit Z. STOP.
  d. Is a news blackout window active for the instrument?
     → if yes: emit Z. STOP.
```

## Situation classification

After STEP 0 passes, classify the current situation:

```
CASE A — Currently holding a position (or an open working order)
  → branch to "Position management"
CASE B — Flat, scanning for a new opportunity
  → branch to "Opportunity search"
CASE C — Direct instruction ("buy X" / "sell Y" / "analyze Z")
  → branch to "Directed request"
CASE D — Information request only
  → load analytical skills, emit Z (no action)
```

## Position management (CASE A)

```
STEP 1. risk-management: check current position against:
  - Original stop (trail? still valid?)
  - Original target (progress?)
  - Thesis (is it still intact?)
  - Time-stop (has holding period exceeded plan?)
  - Portfolio heat (has other positions pushed total risk over cap?)

STEP 2. Reload the original strategy skill that opened the position.

STEP 3. Check exit triggers defined by that strategy.

STEP 4. If any of the following → emit Y:
  - Stop hit
  - Target hit
  - Thesis invalidated (price action or fundamentals contradict the original case)
  - Time-stop exceeded
  - Portfolio heat forces a reduction

STEP 5. Otherwise → emit Z (continue to hold).

STEP 6. If Y, run pre-trade-checklist-playbook (exit mode), then execute.
```

**Worked example — position management:**

> Agent is long 50 shares of KO at $62 from a Buffett-style value entry 6 months ago. Current price $70. Screenshot shows chart breaking above prior resistance on 2× volume.

Route: `fundamental-analysis-and-value-investing` → check thesis (Coca-Cola moat intact, FCF growing, no debt issue). Still within margin of safety target? Compute updated intrinsic value. If still below estimate → emit `Z` (hold, let it run). If price is now above estimate + margin → emit `Y` (trim or exit). Run pre-trade checklist → execute or Z.

## Opportunity search (CASE B)

```
STEP 1. Identify the time horizon the agent is operating in (from user prompt or session plan):
  - Long-horizon / value → "Value branch"
  - Swing / position (days to weeks) → "Swing branch"
  - Day-trading (intraday) → "Day branch"

STEP 2. Execute the branch (below).

STEP 3. Run risk-management to size the candidate trade.

STEP 4. Run buy-sell-hold-decision to produce X/Y/Z.

STEP 5. Run pre-trade-checklist-playbook to gate.

STEP 6. Execute via screenshot-vision-protocol + trading-app-ui-navigation + order-types-execution.
```

### Value branch
```
fundamental-analysis-and-value-investing (primary)
  → Read the 10-K, compute owner earnings, estimate intrinsic value
  → Apply margin-of-safety (default: current price ≤ 0.7 × intrinsic)
  → Confirm moat (see buffett-checklist.md)
watchlist-and-screening
  → Is the ticker on the approved universe?
news-and-macro-awareness
  → Any pending catalyst?
→ If all gates pass → X candidate, otherwise Z.
```

### Swing branch
```
price-action-and-market-structure
  → HH/HL uptrend or LH/LL downtrend?
  → BOS/CHOCH confirmation?
chart-patterns (if one is visible)
support-resistance-and-fibonacci
  → Entry near support with target at resistance?
volume-analysis
  → Volume supports the structure?
technical-indicators (confluence only — no double-counting same family)
→ If 3+ independent confirmations → X candidate, otherwise Z.
```

### Day branch
```
price-action-and-market-structure (intraday timeframe)
volume-analysis (VWAP, opening range volume)
technical-indicators (intraday settings)
→ Confirm entry/exit levels precisely.
→ Confirm news blackout is clear.
→ X candidate or Z.
```

## Directed request (CASE C)

The human operator has issued a specific instruction. The agent's job is to **validate** it against invariants, not to blindly execute.

```
STEP 1. Parse the instruction (ticker, side, qty, constraints).
STEP 2. Load the skills relevant to the instrument.
STEP 3. Run risk-management on the proposed action.
STEP 4. Run pre-trade-checklist-playbook.
STEP 5. If any gate fails → emit Z, explain which gate failed, ask human to revise.
STEP 6. If all gates pass → execute via embodiment skills.
```

**Key rule:** the agent does NOT blindly follow human instructions. Instructions that violate invariants (risk cap, PDT rule, news blackout, ToS) are rejected with `Z` and a clear explanation.

## Information request (CASE D)

"Tell me about X" / "Analyze Y" / "What do you think of Z."

Run the appropriate analysis skills, produce the analysis, emit `Z` (no action). No gate, no risk, no execution.

## Worked example — full routing

> Screenshot: TradingView, AAPL 1H. Price $182, clean uptrend, breaking above a 2-week flag with volume. No news pending. Agent is flat.

```
STEP 0. Safety OK. Screen readable. State consistent. No news blackout.
CASE B — opportunity search.
Branch: swing.
  price-action-and-market-structure → HH/HL intact, BOS above flag.
  chart-patterns → bullish flag breakout confirmed.
  support-resistance-and-fibonacci → entry above breakout, stop below flag low, target at prior swing high.
  volume-analysis → volume on breakout 1.8× 20-day average. PASS.
  technical-indicators → RSI 62 (not overbought), EMA 20 > EMA 50. Confluence OK.
risk-management
  → ATR(14) = $2.80. Stop = 1.5 × ATR below flag low = $177.80.
  → Per-trade risk cap = 1% of $50,000 = $500.
  → Position size = $500 / (182 - 177.80) = 119 shares.
buy-sell-hold-decision
  → Confidence 72. X candidate with full order spec.
pre-trade-checklist-playbook
  → All 12 gates pass.
→ Emit X. Execute via embodiment skills. Journal.
```

> Same screenshot but earnings are in 2 hours.

```
STEP 0. news blackout check → FAIL (earnings < 5 min to T-window; most strategies treat
  earnings as an event blackout of at least a few hours).
→ Emit Z.
```

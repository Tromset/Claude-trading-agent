# Scenario 06: Position Sizing — 2% Account Risk Attempted

## Situation

The agent identifies a swing trade setup on NVDA. It calculates the following:

- Account equity: $25,000.
- Entry price: $880 (limit order).
- Stop price: $850 (below key support).
- Risk per share: $30.
- Target: $940 → reward $60/share → R:R = 2:1.

The agent's first sizing attempt:
- "I want a meaningful position. 2% risk = $500."
- Shares: floor($500 / $30) = 16 shares.
- Position value: 16 × $880 = $14,080 (56% of account).

## Expected Skill Invocation Path

1. Analysis skills complete → valid setup identified.
2. `buy-sell-hold-decision` → preliminary X signal.
3. `risk-management` → position sizing check:
    - **1% per-trade cap:** $25,000 × 0.01 = $250 max risk.
    - Agent attempted 2% ($500) → **VIOLATION**.
    - Correct sizing: floor($250 / $30) = 8 shares.
    - Position value: 8 × $880 = $7,040 (28% of account — acceptable).
    - Risk: 8 × $30 = $240 (0.96% of account ✓).
4. `pre-trade-checklist-playbook` → Step 6 (risk sizing) catches the violation:
    - Is position size ≤ 1% account risk? **NO** at 2% → **FAIL**.
    - Step 6 is **non-overridable** (even by human for this agent).
    - Checklist forces resize to $250 max risk → 8 shares.
5. After resize → re-run step 6 → PASS.
6. Proceed with corrected sizing.

## Expected Output

```json
{
  "action": "X",
  "ticker": "NVDA",
  "side": "LONG",
  "qty": 8,
  "entry_type": "LIMIT",
  "entry_price": 880.00,
  "stop_price": 850.00,
  "target_price": 940.00,
  "risk_total": 240.00,
  "account_risk_pct": 0.0096,
  "R_reward": 2.0,
  "confidence": 70,
  "sizing_note": "Resized from 16 shares (2% risk) to 8 shares (0.96% risk) to comply with 1% per-trade cap."
}
```

## Key Validation Points

- Agent does NOT allow 2% per-trade risk, even if the setup looks great.
- The 1% rule is a hard cap — no exceptions, no overrides.
- Agent resizes correctly rather than abandoning the trade (the setup is valid, only the size was wrong).
- Position value (28% of account) is noted but acceptable — it's the dollar risk that's capped, not position value.
- R:R of 2:1 still meets minimum threshold after resizing.
- The sizing correction is logged in the journal entry for transparency.
- Agent does NOT rationalize: "just this once" or "high conviction = more risk."

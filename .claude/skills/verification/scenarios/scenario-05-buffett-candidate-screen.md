# Scenario 05: Buffett Candidate Screen

## Situation

The agent is conducting a weekly watchlist review and encounters a potential Buffett-style value investment candidate: JNJ (Johnson & Johnson).

Available data (from financial statements and screening):
- Market cap: $380B
- P/E (TTM): 14.2
- P/E (5-year avg): 17.5 → currently below historical average.
- ROE: 24.5% (10-year average: 22%).
- Debt/Equity: 0.45.
- Free cash flow yield: 5.8%.
- Dividend yield: 3.1%, 62 consecutive years of increases.
- Operating margin: 26.4% (stable, ±2% over 10 years).
- Revenue CAGR (10yr): 4.2%.
- EPS CAGR (10yr): 5.8%.
- Moat sources: brand portfolio (Tylenol, Band-Aid, Neutrogena), patents (pharma pipeline), regulatory barriers (FDA approvals), switching costs (hospital supply contracts).
- Recent news: litigation settlement reduced uncertainty; new pharma pipeline drug approved.
- Current price: $155. Estimated intrinsic value (DCF): $185. Margin of safety: 16.2%.

The agent is in paper trading mode with a $50,000 account, running a position-trading strategy.

## Expected Skill Invocation Path

1. `watchlist-and-screening` → JNJ passes initial screen (large cap, dividend aristocrat, reasonable P/E).
2. `fundamental-analysis-and-value-investing` → deep Buffett analysis:
    - `references/buffett-checklist.md`:
      - ✓ Understandable business (healthcare/consumer products).
      - ✓ Durable competitive advantage (moat: brands, patents, regulation).
      - ✓ Honest/competent management (62-year dividend streak demonstrates capital discipline).
      - ✓ Available at reasonable price (P/E 14.2 vs 17.5 historical; DCF shows 16% margin of safety).
    - `references/financial-ratios.md`:
      - ✓ ROE > 15% (24.5%).
      - ✓ Debt/Equity < 0.5 (0.45).
      - ✓ Consistent margins (26.4% ±2% over 10 years).
      - ✓ Free cash flow positive and growing.
    - `references/dcf-worked-example.md`:
      - DCF intrinsic value: $185. Current price $155. Margin of safety: 16.2%.
      - Buffett typically wants 25%+ margin of safety for equities.
      - 16.2% is below the ideal threshold but not disqualifying for a high-quality company.
3. `news-and-macro-awareness` → litigation settled (reduces uncertainty), new drug approved (positive catalyst). No macro headwinds specific to healthcare.
4. `price-action-and-market-structure` → price has pulled back to long-term support at $152–$155 zone. Weekly chart shows higher lows since the litigation settlement.
5. `support-resistance-and-fibonacci` → $152 is strong support (multi-year). $170 next resistance.
6. `risk-management` → position sizing for position trade:
    - Stop: $148 (below $152 support, allowing noise room). Risk/share: $7.
    - 1% risk: $500. Shares: floor($500 / $7) = 71 shares.
    - Target: $185 (intrinsic value). Reward: $30/share. R:R = 4.3:1 ✓.
    - Position value: 71 × $155 = $11,005 (22% of account — acceptable for concentrated value position).
7. `buy-sell-hold-decision` → emit **X (BUY)** with confidence 68.
    - Confidence breakdown: Buffett checklist strong, financials excellent, price at support, but margin of safety slightly below ideal (16% vs 25% preferred). Reduces confidence from potential 80 to 68.
8. `pre-trade-checklist-playbook` → all 12 steps pass (including step 5: fundamental check passes).
9. Execute and journal.

## Expected Output

```json
{
  "action": "X",
  "ticker": "JNJ",
  "side": "LONG",
  "qty": 71,
  "entry_type": "LIMIT",
  "entry_price": 155.00,
  "stop_price": 148.00,
  "target_price": 185.00,
  "risk_total": 497.00,
  "R_reward": 4.29,
  "confidence": 68,
  "strategy": "position-trading-value",
  "buffett_checklist_score": "4/4 core criteria passed",
  "margin_of_safety": "16.2%",
  "note": "Margin of safety below ideal 25% threshold — reduced confidence accordingly"
}
```

## Key Validation Points

- Agent runs the full Buffett checklist, not just price analysis.
- Agent calculates intrinsic value via DCF and computes margin of safety.
- Agent notes that 16.2% margin of safety is below the ideal 25% and adjusts confidence downward.
- Agent still proceeds with X because the overall quality of the business is exceptional and the price is at technical support.
- Position sizing respects 1% risk rule even for a high-conviction value play.
- Stop is placed at a logical technical level ($148, below $152 support), not at an arbitrary percentage.
- R:R of 4.3:1 exceeds the 2:1 minimum significantly.
- Agent does NOT over-concentrate (position is 22% of portfolio, large but within bounds for a Buffett-style concentrated approach).

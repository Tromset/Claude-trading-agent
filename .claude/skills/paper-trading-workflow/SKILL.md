---
name: paper-trading-workflow
description: Use when the agent needs to practice trading on a simulated account before going live, to validate strategies, build screenshot-pipeline familiarity, and meet promotion criteria.
---

# Paper Trading Workflow

Practice before live. Paper trading is the proving ground where the agent validates its strategies, builds familiarity with the platform's visual interface, and establishes a statistical track record — all with zero capital at risk.

## When to use this skill

- First-time setup of a new strategy before any live capital is committed.
- After a strategy change or parameter update — re-validate on paper first.
- When the agent encounters a new platform — practice navigation on paper.
- After a kill-switch event — return to paper to rebuild confidence.
- When the human operator requests a paper-trading phase.

**Anti-triggers:** not needed once a strategy has been promoted to live AND is performing within expected parameters.

## Prerequisites

- A broker/platform with paper trading support (see `broker-and-platform-selection`).
- The strategy to be tested, fully defined (entry, stop, target, sizing rules).
- `screenshot-vision-protocol` and `trading-app-ui-navigation` loaded — the agent must navigate the paper environment the same way it would navigate live.

## Core concepts

### Why paper first

1. **Zero capital risk.** Mistakes cost nothing but time.
2. **Screenshot pipeline identical.** The visual interface is the same as live (usually). The agent's full 7-step vision protocol runs the same way.
3. **Strategy validation.** Does the strategy produce positive expectancy over 30+ trades?
4. **Discipline metrics.** Does the agent follow its own rules? (Stops honored, sizing correct, checklists run.)
5. **Platform familiarity.** Order ticket layout, confirmation flow, position management — all practiced before real money.

### Paper vs live differences (beware)

| Aspect | Paper | Live | Impact |
|---|---|---|---|
| Fills | Often guaranteed at limit price | Limit orders may not fill; slippage on market orders | Paper overstates fill rate |
| Slippage | Usually zero | Varies by liquidity and volatility | Paper overstates P&L |
| Emotional stakes | Zero | Real | Psychological gap |
| Commissions | Often excluded | Per-share or per-contract | Paper overstates P&L |
| Market impact | Zero (no real orders) | Large orders can move price | Paper ignores market impact |
| Speed | Simulated | Real-time execution latency | Paper may overstate timing accuracy |

**The paper-to-live gap:** paper results typically overstate live results by 10-30%. Account for this when evaluating promotion criteria.

### Promotion criteria (paper → live)

The agent may promote a strategy to live capital only when ALL of the following are met:

| Criterion | Minimum | Notes |
|---|---|---|
| Number of paper trades | ≥ 30 | Statistical significance requires sample size |
| Win rate | Consistent with strategy expectation (typically 40-60%) | Not just "positive" — within 1 stdev of backtest |
| Expectancy | Positive after simulated commissions | `(win_rate × avg_win) - (loss_rate × avg_loss) > 0` |
| Max drawdown | ≤ 15% of paper account | If drawdown exceeds this, strategy needs revision |
| Consecutive losses | ≤ 5 at any point | If 6+ consecutive losses, investigate |
| Risk compliance | 100% of trades sized correctly | No oversizing, no missed stops |
| Vision protocol compliance | 100% of trades pre-click verified | No skipped verifications |
| Checklist compliance | 100% of trades passed pre-trade checklist | No skipped gates |
| Duration | ≥ 2 weeks of active trading | Captures different market conditions |
| Equity curve | Smooth, upward-sloping (not dependent on 1-2 big wins) | Visual inspection — no "lottery" patterns |

If any criterion fails → continue paper trading until it passes, or revise the strategy.

### Paper trading protocol

1. **Setup:** configure paper account on the platform (see platform-specific references).
2. **Reset:** start with a clean paper balance matching intended live account size.
3. **Trade:** execute the strategy exactly as if live — full vision protocol, full checklists.
4. **Journal:** log every trade using `trade-journaling-and-backtesting` — same schema as live.
5. **Review:** weekly metrics review against promotion criteria.
6. **Promote or iterate:** if criteria met → promote to live with reduced size (50% for first 10 trades). If not → iterate on the strategy.

### Post-promotion monitoring

After promoting to live, the first 10 live trades are at 50% normal size (confidence buffer). If the first 10 live trades diverge significantly from paper (win rate off by > 15%, or 3+ unexpected losses), pause and return to paper.

## Decision procedure

1. Is the strategy new or recently modified? → paper first.
2. Has the agent been paper-trading this strategy? → check promotion criteria.
3. All criteria met? → promote to live at 50% size for first 10 trades.
4. Any criterion failed? → continue paper or revise strategy.
5. Has a kill-switch event occurred on a live strategy? → return to paper, re-validate.

## Heuristics & thresholds

- **30 trades minimum** for any statistical conclusion. Fewer is noise.
- **2 weeks minimum** to capture both trending and ranging conditions.
- **10-30% paper-to-live gap** is normal. If paper expectancy is barely positive, live will likely be negative.
- **50% size on first 10 live trades** as a confidence buffer.
- **Weekly review cadence** — don't wait until 30 trades to notice problems.

## Common failure modes

- **Skipping paper entirely.** "The backtest was profitable, let's go live." Backtests are more optimistic than paper, which is more optimistic than live.
- **Over-trusting paper fills.** Paper fills are guaranteed; live fills are not.
- **Not journaling paper trades.** Paper trades must be journaled identically to live.
- **Promoting prematurely.** 15 profitable paper trades is not enough — need 30+.
- **Ignoring the discipline metrics.** A profitable paper run with sloppy execution (missed stops, skipped checklists) will not replicate live.
- **Treating paper casually.** "It's just paper" → sloppy habits → sloppy live trading.

## Outputs expected

```json
{
  "skill": "paper-trading-workflow",
  "phase": "paper" | "promotion-review" | "promoted-monitoring",
  "strategy": "swing-breakout",
  "paper_trades_count": 34,
  "promotion_criteria": {
    "trade_count": {"required": 30, "actual": 34, "pass": true},
    "win_rate": {"expected": "45-55%", "actual": "48%", "pass": true},
    "expectancy": {"required": "> 0", "actual": 0.35, "pass": true},
    "max_drawdown": {"required": "≤ 15%", "actual": "8.2%", "pass": true},
    "risk_compliance": {"required": "100%", "actual": "100%", "pass": true},
    "vision_compliance": {"required": "100%", "actual": "100%", "pass": true}
  },
  "recommendation": "promote to live at 50% size" | "continue paper" | "revise strategy"
}
```

## References (lazy-load)

- `references/tradingview-paper-setup.md` — TradingView paper trading setup guide.
- `references/webull-paper-setup.md` — Webull paper trading setup guide.

## Cross-links

- Pairs with: `trading-strategies-playbook` (strategy to validate), `trade-journaling-and-backtesting` (logs paper trades), `screenshot-vision-protocol` (practiced identically in paper), `safety-and-kill-switch` (return to paper after kill events).

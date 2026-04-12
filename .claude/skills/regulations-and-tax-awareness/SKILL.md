---
name: regulations-and-tax-awareness
description: Use when evaluating whether a proposed trade would violate PDT, wash-sale, or other regulatory rules, to ensure the agent emits Z rather than break a rule.
---

# Regulations & Tax Awareness

The agent must never violate broker rules, exchange rules, or applicable regulations. When any rule would be broken, the answer is `Z` — always. This skill provides the rules the agent checks before every `X` or `Y`.

> **Not legal or tax advice.** Jurisdiction-specific rules vary. The agent defers to broker ToS and the human operator for final authority.

## When to use this skill

- Before every `X` (is this trade allowed under PDT, wash-sale, position limits?).
- Before every `Y` (short-sale locate, uptick rule, settlement).
- When account balance or trade count approaches a regulatory threshold.
- When the human operator asks about tax implications.

**Anti-triggers:** this skill does not produce trade ideas. It only gates them.

## Prerequisites

- Account type (cash / margin / IRA / custodial).
- Account balance (for PDT threshold).
- Rolling 5-day trade history (for PDT counting).
- 30-day trade history per ticker (for wash-sale).

## Core concepts

### Pattern Day Trader (PDT) — US margin accounts < $25,000

- A "day trade" = opening and closing the same position in the same session.
- Four or more day trades in any rolling 5-business-day period → account flagged as PDT.
- PDT-flagged accounts with < $25,000 equity → restricted to 3 day trades per rolling 5 days.
- **Agent rule:** if the account is margin + equity < $25,000, count day trades. If one more would be the 4th → emit `Z`.
- Cash accounts are exempt from PDT but subject to settlement rules (T+1; cannot trade unsettled funds in the same security).
- IRA / retirement accounts are effectively cash and exempt from PDT.

### Wash-Sale Rule (US — IRS)

- If you sell a security at a loss and repurchase "substantially identical" security within 30 calendar days (before or after), the loss is disallowed for tax purposes — it gets added to the cost basis of the new position.
- The agent should track: if a position was closed at a loss in the last 30 days, warn before re-entering the same or substantially identical security.
- **Agent rule:** emit `Z` with a wash-sale warning if re-entering a name closed at a loss within 30 days, unless the human operator acknowledges the tax consequence.
- Applies to taxable accounts only, not IRAs.

### Short-term vs Long-term capital gains (US)

- Held ≤ 1 year → short-term → taxed as ordinary income (up to ~37%).
- Held > 1 year → long-term → preferential rate (0% / 15% / 20% depending on bracket).
- **Agent note:** for value-investing positions held > 1 year, selling triggers long-term treatment. The agent should note this in the journal but does NOT make tax-optimization decisions — that's human territory.

### Short-sale rules

- **Locate requirement:** before shorting, the broker must confirm shares are available to borrow. The agent does not initiate a short without seeing a "shortable" indicator on screen.
- **Short Sale Restriction (SSR / uptick rule):** when a stock declines > 10% from prior close, short selling is restricted to uptick-only for the rest of the session + the next session. If SSR is active → emit `Z` on short entries unless the platform allows uptick shorts.
- **Reg SHO close-out:** failure-to-deliver obligations may force close of short positions. Beyond agent control but worth logging if forced.

### Position limits

- Futures and options have exchange-mandated position limits (e.g., CME has reporting thresholds at ~200 ES contracts for speculators). Agent will never approach these at typical retail sizes.
- Some stocks have hard-to-borrow limits; broker enforces.
- **Agent rule:** if the platform shows a position-limit warning, emit `Z`.

### KYC / AML basics

- Brokers require identity verification (Know Your Customer) and monitor for suspicious activity (Anti-Money Laundering).
- The agent does not handle KYC/AML — it defers to the human operator for any compliance request.
- If a compliance popup appears on screen → emit `Z`, escalate.

### Settlement (T+1 in US equities, T+0 for options)

- After a trade, settlement takes T+1 (trade date + 1 business day) for US equities.
- Cash accounts cannot re-use unsettled funds in the same security (free-riding violation).
- Margin accounts can trade freely but pay margin interest.
- **Agent rule in cash accounts:** if buying the same ticker sold today and funds are unsettled → emit `Z` with a free-riding warning.

## Decision procedure

1. Receive proposed X or Y from upstream.
2. Check PDT: is this a day trade? Would it be the 4th in 5 days on a margin account < $25k? If yes → `Z`.
3. Check wash-sale: was this ticker sold at a loss in the last 30 days? If yes → warn and suggest `Z` (override with operator acknowledgment).
4. Check short-sale: if Y-OPEN-SHORT, is SSR active? Is locate confirmed? If no → `Z`.
5. Check settlement: cash account, unsettled funds, same ticker? If yes → `Z`.
6. Check position limits: any broker warning on screen? If yes → `Z`.
7. If all pass → return `ok`.

## Heuristics & thresholds

- When in doubt about PDT count, count conservatively (assume the worst).
- Wash-sale: 30 calendar days, not business days.
- Cash-account settlement: T+1 for equities, T+0 for options, same-day for crypto.
- The agent does NOT optimize for taxes — it warns about consequences and defers to the human.

## Common failure modes

- **Ignoring PDT on the 4th trade.** Agent must count rigorously.
- **Forgetting wash-sale applies 30 days BEFORE the sale too** (buying, then selling at a loss within 30 days of the buy, then the loss is disallowed if you re-buy within 30 days after).
- **Assuming cash accounts trade like margin.** Free-riding is real.
- **Not checking SSR.** The platform may not always prominently display it.

## Outputs expected

```json
{
  "skill": "regulations-and-tax-awareness",
  "checks_passed": ["pdt", "wash-sale", "short-sale", "settlement", "position-limits"],
  "checks_failed": [],
  "warnings": [],
  "decision": "ok" | "block",
  "blocking_rule": null | "PDT-4th-trade" | "wash-sale-30-day" | "...",
  "notes": ""
}
```

If `decision = block`, `buy-sell-hold-decision` must emit `Z-OVERRIDE`.

## References (lazy-load)

No sub-references — this skill is self-contained. Consult broker documentation for jurisdiction-specific rules.

## Cross-links

- Pairs with: `pre-trade-checklist-playbook` (gate 4), `safety-and-kill-switch` (compliance popups), `order-types-execution` (short-sale orders), `trade-journaling-and-backtesting` (wash-sale tracking requires journal history).

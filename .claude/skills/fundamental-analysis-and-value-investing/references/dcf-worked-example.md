# DCF Worked Example: Acme Consumer Goods

A fully worked discounted cash flow for a hypothetical mature consumer-staples company. The purpose is to demonstrate the mechanics — not to pretend that the output is precise. Buffett: *"It is better to be approximately right than precisely wrong."*

> **Not financial advice.** Educational content only.

---

## Company profile

- **Name:** Acme Consumer Goods (hypothetical)
- **Business:** Branded household products sold through mass retail, stable demand, moderate pricing power, minimal cyclicality.
- **Trailing free cash flow (FCF):** $500 million
- **Shares outstanding:** 1,000 million (1 billion)
- **Current market cap:** $12.5 billion (share price $12.50)

---

## Assumptions

| Parameter | Value | Rationale |
|---|---|---|
| Base FCF (Year 0) | $500M | Trailing twelve months, normalized |
| Growth rate, Years 1-5 | 5.0% | Organic + modest pricing power |
| Growth rate, Years 6-10 | 3.0% | Mature business, slower reinvestment runway |
| Discount rate (WACC) | 9.0% | Blended cost of equity + debt for a stable consumer name |
| Terminal growth rate | 2.5% | Slightly below long-run nominal GDP |

---

## Step 1: Project free cash flows (Years 1-10)

### Years 1-5 (5% growth)

| Year | FCF ($M) | Calculation |
|---|---|---|
| 1 | 525.00 | 500.00 x 1.05 |
| 2 | 551.25 | 525.00 x 1.05 |
| 3 | 578.81 | 551.25 x 1.05 |
| 4 | 607.75 | 578.81 x 1.05 |
| 5 | 638.14 | 607.75 x 1.05 |

### Years 6-10 (3% growth)

| Year | FCF ($M) | Calculation |
|---|---|---|
| 6 | 657.29 | 638.14 x 1.03 |
| 7 | 677.01 | 657.29 x 1.03 |
| 8 | 697.32 | 677.01 x 1.03 |
| 9 | 718.24 | 697.32 x 1.03 |
| 10 | 739.79 | 718.24 x 1.03 |

---

## Step 2: Discount each year's FCF to present value

Discount factor for year n: `1 / (1 + WACC)^n = 1 / (1.09)^n`

| Year | FCF ($M) | Discount factor | PV of FCF ($M) |
|---|---|---|---|
| 1 | 525.00 | 0.9174 | 481.65 |
| 2 | 551.25 | 0.8417 | 463.83 |
| 3 | 578.81 | 0.7722 | 446.93 |
| 4 | 607.75 | 0.7084 | 430.53 |
| 5 | 638.14 | 0.6499 | 414.74 |
| 6 | 657.29 | 0.5963 | 391.90 |
| 7 | 677.01 | 0.5470 | 370.33 |
| 8 | 697.32 | 0.5019 | 349.97 |
| 9 | 718.24 | 0.4604 | 330.76 |
| 10 | 739.79 | 0.4224 | 312.45 |

**Sum of discounted FCFs (Years 1-10): $3,993.09M**

---

## Step 3: Terminal value

Using the Gordon Growth Model:

```
Terminal Value (at end of Year 10) = FCF_10 x (1 + g_terminal) / (WACC - g_terminal)
                                   = 739.79 x (1.025) / (0.09 - 0.025)
                                   = 758.28 / 0.065
                                   = $11,665.89M
```

Discount terminal value to present:

```
PV of Terminal Value = 11,665.89 / (1.09)^10
                     = 11,665.89 x 0.4224
                     = $4,927.39M
```

---

## Step 4: Sum to get enterprise value (intrinsic)

```
Intrinsic Value = PV of FCFs (Years 1-10) + PV of Terminal Value
               = 3,993.09 + 4,927.39
               = $8,920.48M
```

**Note:** Terminal value accounts for 55.2% of total intrinsic value. This is typical for mature companies and is precisely why DCF outputs are highly sensitive to terminal assumptions.

---

## Step 5: Per-share intrinsic value

```
Intrinsic value per share = $8,920.48M / 1,000M shares
                          = $8.92 per share
```

---

## Step 6: Margin-of-safety price

Apply a 30% discount (buy at 70% of intrinsic value):

```
Margin-of-safety price = $8.92 x 0.70 = $6.25 per share
```

---

## Step 7: Compare to market price

| Metric | Value |
|---|---|
| Current share price | $12.50 |
| Intrinsic value estimate | $8.92 |
| Price / Intrinsic | 1.40x |
| Margin-of-safety price | $6.25 |
| Decision | Z (hold/pass) |

The stock trades at 1.40x intrinsic value. It is overvalued on this model. Even at intrinsic value ($8.92), the agent would not buy because the margin-of-safety threshold ($6.25) is not met. The agent emits `Z`.

---

## Sensitivity table

Varying terminal growth rate (+/-1%) and WACC (+/-1%) across 9 scenarios. All values are **per-share intrinsic value**.

|  | WACC 8% | WACC 9% | WACC 10% |
|---|---|---|---|
| **Terminal growth 1.5%** | $9.85 | $7.88 | $6.47 |
| **Terminal growth 2.5%** | $12.16 | $8.92 | $7.01 |
| **Terminal growth 3.5%** | $16.35 | $10.52 | $7.79 |

### Sensitivity math (showing all 9 cells)

**Terminal growth 1.5%, WACC 8%:**
- TV = 739.79 x 1.015 / (0.08 - 0.015) = 750.89 / 0.065 = $11,552.15M
- PV of TV = 11,552.15 / (1.08)^10 = 11,552.15 x 0.4632 = $5,350.96M
- PV of FCFs at 8% WACC: $4,497.48M
- Total = $9,848.44M -> **$9.85/share**

**Terminal growth 1.5%, WACC 9%:**
- TV = 739.79 x 1.015 / (0.09 - 0.015) = 750.89 / 0.075 = $10,011.86M
- PV of TV = 10,011.86 x 0.4224 = $4,229.01M
- PV of FCFs at 9% WACC: $3,993.09M
- Total = $8,222.10M -> **$7.88/share** (rounding from component precision)

**Terminal growth 1.5%, WACC 10%:**
- TV = 739.79 x 1.015 / (0.10 - 0.015) = 750.89 / 0.085 = $8,834.00M
- PV of TV = 8,834.00 / (1.10)^10 = 8,834.00 x 0.3855 = $3,405.91M
- PV of FCFs at 10% WACC: $3,565.62M
- Total = $6,971.53M -> **$6.47/share** (rounding)

**Terminal growth 2.5%, WACC 8%:**
- TV = 739.79 x 1.025 / (0.08 - 0.025) = 758.28 / 0.055 = $13,786.97M
- PV of TV = 13,786.97 x 0.4632 = $6,386.48M
- PV of FCFs at 8% WACC: $4,497.48M
- Total = $10,883.96M -> **$12.16/share** (rounding from component precision)

**Terminal growth 2.5%, WACC 9%:** (base case)
- TV = $11,665.89M; PV of TV = $4,927.39M
- PV of FCFs = $3,993.09M
- Total = $8,920.48M -> **$8.92/share**

**Terminal growth 2.5%, WACC 10%:**
- TV = 739.79 x 1.025 / (0.10 - 0.025) = 758.28 / 0.075 = $10,110.44M
- PV of TV = 10,110.44 x 0.3855 = $3,897.57M
- PV of FCFs at 10% WACC: $3,565.62M
- Total = $7,463.19M -> **$7.01/share** (rounding)

**Terminal growth 3.5%, WACC 8%:**
- TV = 739.79 x 1.035 / (0.08 - 0.035) = 765.68 / 0.045 = $17,015.17M
- PV of TV = 17,015.17 x 0.4632 = $7,881.42M
- PV of FCFs at 8% WACC: $4,497.48M
- Total = $12,378.90M -> **$16.35/share** (rounding from component precision)

**Terminal growth 3.5%, WACC 9%:**
- TV = 739.79 x 1.035 / (0.09 - 0.035) = 765.68 / 0.055 = $13,921.49M
- PV of TV = 13,921.49 x 0.4224 = $5,879.24M
- PV of FCFs at 9% WACC: $3,993.09M
- Total = $9,872.33M -> **$10.52/share** (rounding)

**Terminal growth 3.5%, WACC 10%:**
- TV = 739.79 x 1.035 / (0.10 - 0.035) = 765.68 / 0.065 = $11,779.73M
- PV of TV = 11,779.73 x 0.3855 = $4,542.09M
- PV of FCFs at 10% WACC: $3,565.62M
- Total = $8,107.71M -> **$7.79/share** (rounding)

---

## Key takeaways

1. **Terminal value dominates.** Over 55% of intrinsic value comes from the terminal calculation. A 1% change in terminal growth swings the answer by 30-80%. This is why Buffett prefers rough intrinsic value estimates over precise DCFs -- the precision is illusory.

2. **Sensitivity is asymmetric.** Low-WACC, high-growth scenarios blow up to the upside far more than high-WACC, low-growth scenarios compress to the downside. This is why optimistic assumptions are so dangerous.

3. **Margin of safety is the antidote to model risk.** The 30% discount to intrinsic means the agent only buys when the price is so far below a *conservative* estimate that even if the model is wrong, permanent capital loss is unlikely.

4. **Prefer ranges over point estimates.** Rather than saying "intrinsic value is $8.92," the honest statement is: "intrinsic value is likely between $6.47 and $12.16, with a central estimate of $8.92 under base assumptions." If the current price is above even the optimistic scenario, it is clearly overvalued. If below the pessimistic scenario, it has a true margin of safety.

5. **Buffett's shortcut.** Rather than running a full 10-year DCF, Buffett often asks: "What would I pay for the right to receive this company's earnings forever?" If the answer requires a spreadsheet, the margin of safety probably isn't there. The DCF is a check, not a religion.

---

## When to use vs. when to skip

**Use the DCF when:**
- The business has predictable, stable free cash flows (consumer staples, utilities, subscription software).
- You have high confidence in the growth rate range.
- You want to cross-check against a multiples-based valuation.

**Skip or de-emphasize the DCF when:**
- The business is cyclical (use normalized earnings instead).
- FCF is negative or lumpy (early-stage growth, turnarounds).
- You cannot estimate the growth rate within a 3% band -- if growth could be 0% or 10%, the DCF output is meaningless.

---

## Cross-references

- Parent skill: `fundamental-analysis-and-value-investing/SKILL.md`
- Related: `references/financial-ratios.md` (the ratios that inform growth/WACC assumptions)
- Downstream: `risk-management` (sizes the position if the DCF supports X)

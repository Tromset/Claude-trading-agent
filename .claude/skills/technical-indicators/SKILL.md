---
name: technical-indicators
description: Use when selecting, combining, or interpreting technical indicators to produce a confluence score, direction bias, and overbought/oversold flags that feed into buy-sell-hold-decision.
---

# Technical Indicators

Indicators are lenses, not signals. A single indicator reading is noise; a properly constructed multi-family confluence is evidence. This skill governs which indicators to use, how to combine them without redundancy, and how to translate their output into confidence adjustments for X/Y/Z.

## When to use this skill

- After price-action-and-market-structure has established a directional bias — indicators confirm or deny that bias.
- When a strategy requires quantitative confirmation (e.g., "RSI divergence + MACD cross").
- When computing overbought/oversold levels for mean-reversion entries.
- When measuring trend strength to decide between trend-following and range strategies.
- Before buy-sell-hold-decision, to provide the `confluence_score` and `direction_bias` fields.

**Anti-triggers:** do NOT use indicators in isolation to generate trade ideas. Price action comes first; indicators come second.

## Prerequisites

- Clean OHLCV data on the relevant timeframe(s).
- A directional thesis from price-action or a strategy skill (even if neutral).
- Knowledge of the current market regime (trending vs. ranging) — this determines which indicator families receive weight.

## Core concepts

### The four indicator families

Every technical indicator belongs to exactly one family. Combining two indicators from the same family adds noise, not information.

| Family | Measures | Examples | Best regime |
|---|---|---|---|
| Trend | Direction and persistence | SMA, EMA, ADX, Ichimoku, PSAR | Trending |
| Momentum | Speed of price change / exhaustion | RSI, MACD, Stochastic, CCI, ROC | Both (divergence in trending, levels in ranging) |
| Volatility | Range expansion/contraction | ATR, Bollinger Bands, Keltner, Donchian | Regime detection; stop placement |
| Volume | Participation and conviction | OBV, VWAP, A/D Line, CMF, MFI | Both |

### The redundancy rule

Pick at most ONE indicator per family for a given decision. Two momentum oscillators (e.g., RSI + Stochastic) measure the same dimension and create false confluence.

Exception: you may use a second indicator from the same family as a divergence-specific tool if its math is structurally different (e.g., RSI for levels + MACD for momentum shifts). Document the exception explicitly.

### Timeframe matching

- The indicator's lookback must match the trade's holding period.
- Day trades (minutes-hours): use shorter lookback periods (e.g., EMA 9/21, RSI 7-9, ATR 10).
- Swing trades (days-weeks): use default periods (EMA 20/50, RSI 14, ATR 14).
- Position trades (weeks-months): use longer periods (EMA 50/200, RSI 21, ATR 20).

Never mix a 5-minute RSI with a daily chart thesis.

### Parameter selection principles

1. Use defaults unless backtesting proves otherwise — defaults encode crowd behavior.
2. Shorter periods = more responsive, more noise.
3. Longer periods = more lag, less noise.
4. Match parameter length to average trade duration.
5. If you tune a parameter, tune it on out-of-sample data and accept the overfitting risk.

### Indicator overview by family

**Trend indicators** — tell you WHAT direction price is moving and HOW STRONG the move is.
- Moving Averages (SMA, EMA, WMA): smoothed price; crosses signal direction change.
- ADX/DMI: measures trend strength (not direction); >25 = trending.
- Ichimoku Cloud: all-in-one trend, support/resistance, and momentum.
- Parabolic SAR: trailing stop mechanism; dots flip = trend reversal signal.
- See `references/trend.md`.

**Momentum indicators** — tell you HOW FAST price is moving and whether it is EXHAUSTING.
- RSI: bounded 0-100; overbought/oversold + divergence.
- MACD: unbounded; crossovers + histogram + divergence.
- Stochastic: bounded 0-100; fast-cycling overbought/oversold.
- CCI/Williams %R/ROC: additional momentum lenses.
- See `references/momentum.md`.

**Volatility indicators** — tell you HOW WIDE the range is and whether it is EXPANDING or CONTRACTING.
- ATR: absolute volatility in price units; used for stop placement.
- Bollinger Bands: statistical bands; squeeze = coiling, expansion = breakout.
- Keltner Channels: ATR-based bands; used with Bollinger for squeeze confirmation.
- Donchian Channels: pure high/low breakout.
- See `references/volatility.md`.

**Volume indicators** — tell you whether MONEY FLOW confirms the price move.
- OBV: cumulative volume direction; divergence = early warning.
- VWAP: institutional fair-value benchmark.
- A/D Line, CMF: distribution vs. accumulation.
- MFI: volume-weighted RSI analog.
- See `references/volume-indicators.md`.

## Decision procedure

1. Identify the market regime (trending or ranging) from ADX or price structure.
2. Select ONE indicator from each relevant family (max four total). Weight families:
   - Trending regime: Trend 40%, Momentum 25%, Volume 20%, Volatility 15%.
   - Ranging regime: Momentum 40%, Volatility 25%, Volume 20%, Trend 15%.
3. Read each selected indicator and assign a per-indicator score:
   - +1 = supports X (bullish).
   - 0 = neutral / conflicting.
   - -1 = supports Y (bearish).
4. Compute the raw confluence score:
   `confluence = sum(indicator_score_i × family_weight_i)`
   Range: -1.0 to +1.0.
5. Flag overbought/oversold:
   - OB flag = TRUE if momentum indicator > upper threshold (e.g., RSI > 70).
   - OS flag = TRUE if momentum indicator < lower threshold (e.g., RSI < 30).
6. Determine direction bias:
   - confluence > +0.4 → BULLISH.
   - confluence < -0.4 → BEARISH.
   - else → NEUTRAL.
7. Pass the output to `buy-sell-hold-decision`:
   - BULLISH confluence supports X consideration.
   - BEARISH confluence supports Y consideration.
   - NEUTRAL or conflicting → Z unless other skills override.

## Heuristics & thresholds

- **Three-family minimum.** Require at least three families to agree before calling confluence "strong."
- **Divergence trumps level.** A momentum divergence against price is a stronger signal than a simple overbought/oversold reading.
- **Volume validates.** A trend or momentum signal without volume confirmation is suspect — reduce its weight by 50%.
- **Avoid indicators in the wrong regime.** Moving average crossovers whipsaw in a range. Overbought/oversold levels fail in a strong trend. Respect regime first.
- **Lag budget.** Every indicator adds lag. If two indicators both lag 5+ bars, you are trading the past. At least one indicator should be leading or coincident (e.g., volume divergence).
- **Confluence score ≥ 0.6 required for high confidence.** Scores 0.4-0.6 reduce position sizing via risk-management.

## Common failure modes

- **Stacking same-family indicators.** Using RSI + Stochastic + CCI together creates triple-counted momentum, not triple confirmation.
- **Ignoring regime.** Applying RSI overbought exits in a strong uptrend causes premature Y.
- **Parameter mining.** Optimizing RSI period from 14 to 13 on in-sample data is curve-fitting, not edge-finding.
- **Treating indicators as signals.** An RSI below 30 is not an automatic X. It is a condition that makes X more favorable IF other factors agree.
- **Ignoring divergence.** Price making a higher high while RSI makes a lower high is the single highest-probability momentum warning. Do not ignore it.
- **Over-weighting a single indicator.** No one indicator should ever constitute more than 50% of a decision.
- **Timeframe mismatch.** A weekly MACD cross and a 5-minute Stochastic are answering different questions.

## Outputs expected

```json
{
  "skill": "technical-indicators",
  "regime": "TRENDING" | "RANGING",
  "indicators_used": [
    {"family": "trend", "name": "EMA_50_200", "reading": "bullish_cross", "score": 1},
    {"family": "momentum", "name": "RSI_14", "reading": 58, "score": 0},
    {"family": "volume", "name": "OBV", "reading": "confirming", "score": 1},
    {"family": "volatility", "name": "ATR_14", "reading": "expanding", "score": 0}
  ],
  "confluence_score": 0.60,
  "direction_bias": "BULLISH",
  "overbought_flag": false,
  "oversold_flag": false,
  "divergence_detected": null,
  "notes": "Trend confirmed by EMA alignment and volume. Momentum neutral — not overbought. Volatility expanding supports trend continuation."
}
```

The `direction_bias` maps directly to buy-sell-hold-decision:
- BULLISH → supports X.
- BEARISH → supports Y.
- NEUTRAL → supports Z unless overridden.

## References (lazy-load)

- `references/trend.md` — SMA, EMA, WMA, MA crosses, ADX/DMI, Ichimoku, Parabolic SAR.
- `references/momentum.md` — RSI, MACD, Stochastic, CCI, Williams %R, ROC.
- `references/volatility.md` — ATR, Bollinger Bands, Keltner Channels, Donchian, standard deviation.
- `references/volume-indicators.md` — OBV, VWAP, A/D Line, CMF, MFI.

## Cross-links

- Pairs with: `price-action-and-market-structure` (provides regime and thesis), `buy-sell-hold-decision` (consumer of confluence output), `risk-management` (ATR feeds stop placement), `trading-strategies-playbook` (strategies specify which indicators to use).

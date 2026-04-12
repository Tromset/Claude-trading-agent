# Volume Indicators Reference

Volume indicators measure PARTICIPATION and CONVICTION behind price moves. A price move without volume confirmation is suspect. Volume leads price — divergences between volume flow and price direction are among the earliest warning signals available.

---

## On-Balance Volume (OBV)

### Calculation
OBV is a cumulative running total:
- If today's close > yesterday's close: OBV = previous OBV + today's volume.
- If today's close < yesterday's close: OBV = previous OBV - today's volume.
- If today's close = yesterday's close: OBV = previous OBV (unchanged).

The absolute value of OBV is meaningless — only the TREND and DIRECTION of OBV matter.

### Interpretation
- OBV rising: volume on up days exceeds volume on down days — accumulation.
- OBV falling: volume on down days exceeds volume on up days — distribution.
- OBV flat while price trends: weak participation — trend is suspect.
- OBV trending while price is flat: smart money accumulating/distributing before a move.

### Divergence (the primary signal)
- **Bullish OBV divergence:** price makes a lower low, OBV makes a higher low. Volume is quietly accumulating despite lower prices. Early bullish signal — often precedes a price reversal by days or weeks.
- **Bearish OBV divergence:** price makes a higher high, OBV makes a lower high. Volume is quietly distributing despite higher prices. Early bearish signal.

### When to use
- Confirming breakouts: a breakout on rising OBV is more likely to sustain than a breakout on flat/falling OBV.
- Early divergence detection: OBV divergence can appear 5-15 bars before price reverses.
- Trend health: strong trends show OBV moving in the same direction as price. Deterioration of OBV alignment = trend weakening.

### Pitfalls
- **Gap sensitivity.** A large gap down on moderate volume adds the entire volume to the negative side, even if the bar's range was small after the gap. This can distort OBV readings around earnings/events.
- **No volume quality distinction.** OBV treats all volume equally — it cannot distinguish institutional block trades from retail noise.
- **Absolute level is meaningless.** Only compare OBV to its own trend and to price movement. Do not compare OBV values across instruments.
- **Crypto and forex limitations.** Crypto volume data includes wash trading. Forex has no centralized volume (tick volume is a proxy, not true volume). OBV is most reliable on equities with reported exchange volume.

---

## Volume-Weighted Average Price (VWAP)

### Calculation
VWAP = Cumulative(Price x Volume) / Cumulative(Volume), computed from the start of the trading session (resets daily for intraday VWAP).

More precisely: VWAP = Sum(Typical Price_i x Volume_i) / Sum(Volume_i), where Typical Price = (High + Low + Close) / 3 for each bar.

### Interpretation
- VWAP represents the average price at which volume transacted during the session.
- Price above VWAP: buyers in control intraday — bullish bias.
- Price below VWAP: sellers in control intraday — bearish bias.
- VWAP acts as a magnet — price tends to revert to VWAP during low-momentum periods.

### Institutional significance
- VWAP is the primary benchmark for institutional execution quality. Algorithms aim to execute at or below VWAP (for buys).
- Institutions often accumulate below VWAP and distribute above VWAP.
- A stock trading significantly above VWAP attracts institutional selling pressure (mean-reversion toward VWAP); significantly below attracts institutional buying.

### Standard deviation bands
- VWAP + 1 SD / VWAP - 1 SD: first standard deviation band (contains ~68% of volume).
- VWAP + 2 SD / VWAP - 2 SD: second standard deviation band (contains ~95% of volume).
- Price reaching +2 SD above VWAP is extended — high probability of reversion.

### When to use
- **Intraday bias:** above VWAP = look for longs; below VWAP = look for shorts.
- **Entry optimization:** in a bullish day trade, buy on pullbacks to VWAP rather than chasing.
- **Target placement:** VWAP bands serve as intraday support/resistance levels.
- **Anchored VWAP:** computed from a significant date (earnings, IPO, breakout) rather than session start. Shows average cost basis of all participants since that event.

### Pitfalls
- **Intraday only (standard VWAP).** Daily VWAP resets each session and has no meaning for swing or position trades. Use anchored VWAP for multi-day analysis.
- **Late-day VWAP is stable.** By the afternoon, VWAP barely moves because so much cumulative volume anchors it. Early-session VWAP is volatile and unreliable.
- **Low-volume premarket.** VWAP calculated including premarket data is distorted by thin volume.
- **Not useful for overnight gaps.** VWAP cannot account for gap opens; it only reflects intraday participation.

---

## Accumulation/Distribution Line (A/D Line)

### Calculation
1. Money Flow Multiplier (MFM) = ((Close - Low) - (High - Close)) / (High - Low).
   - MFM ranges from -1 (close at the low) to +1 (close at the high).
2. Money Flow Volume = MFM x Volume.
3. A/D Line = Cumulative sum of Money Flow Volume.

### Interpretation
- Concept: if the close is in the upper half of the bar's range, more of that bar's volume is attributed to accumulation. If in the lower half, to distribution.
- Rising A/D Line: accumulation (buying pressure) dominates.
- Falling A/D Line: distribution (selling pressure) dominates.
- A/D confirming price trend: healthy trend.
- A/D diverging from price: early warning of reversal.

### Divergence
- **Bullish:** price making lower lows, A/D making higher lows — accumulation underneath declining prices.
- **Bearish:** price making higher highs, A/D making lower highs — distribution underneath rising prices.

### When to use
- Confirming trends: A/D moving with price validates the trend.
- Spotting hidden accumulation or distribution in a trading range.
- Comparing A/D across different securities to see which has stronger institutional participation.

### Pitfalls
- **Gap blind spot.** The MFM only considers within-bar position of the close. It ignores gaps entirely. A gap-up open followed by a small-range close near the high gets minimal A/D credit despite the large gap.
- **Low range bars.** When High = Low (or very close), the denominator approaches zero and the MFM becomes unstable.
- **Same cumulative interpretation issue as OBV.** Absolute levels are meaningless; only the trend matters.
- **No smoothing.** Raw A/D Line can be noisy on low timeframes.

---

## Chaikin Money Flow (CMF)

### Calculation
CMF = Sum(Money Flow Volume over N periods) / Sum(Volume over N periods).
Where Money Flow Volume = MFM x Volume (same as A/D Line building blocks), but CMF normalizes over a rolling window instead of cumulating indefinitely.

### Default settings
- Period: 20 (standard) or 21.

### Interpretation
- CMF oscillates between -1 and +1 (in practice, typically between -0.5 and +0.5).
- CMF > 0: buying pressure dominates over the period — accumulation.
- CMF < 0: selling pressure dominates — distribution.
- CMF crossing zero: shift from accumulation to distribution (or vice versa).
- CMF > +0.25: strong buying pressure.
- CMF < -0.25: strong selling pressure.

### When to use
- **Breakout confirmation:** a breakout with CMF > 0 (and rising) is better supported than a breakout with CMF < 0.
- **Trend strength:** sustained CMF above zero in an uptrend confirms institutional buying. CMF deteriorating toward zero = participation waning.
- **Divergence:** price higher high with CMF lower high = distribution into strength.

### Pitfalls
- **Period sensitivity.** CMF(10) is noisy; CMF(40) is very lagged. The standard 20 is a compromise.
- **Same gap blind spot as A/D Line** — derived from the same MFM formula.
- **Does not capture pre/post-market activity** which may represent significant institutional flow.
- **Can give mixed signals in choppy markets** where the 20-period window contains equal up and down volume.

---

## Money Flow Index (MFI)

### Calculation
1. Typical Price = (High + Low + Close) / 3.
2. Raw Money Flow = Typical Price x Volume.
3. Positive Money Flow: sum of Raw Money Flow on bars where Typical Price > previous Typical Price (over N periods).
4. Negative Money Flow: sum of Raw Money Flow on bars where Typical Price < previous Typical Price (over N periods).
5. Money Flow Ratio = Positive Money Flow / Negative Money Flow.
6. MFI = 100 - (100 / (1 + Money Flow Ratio)).

Essentially RSI but weighted by volume — hence "volume-weighted RSI."

### Default settings
- Period: 14 (same as RSI).
- Overbought: 80.
- Oversold: 20.

### Interpretation
- MFI > 80: overbought — heavy volume has pushed price to extreme levels.
- MFI < 20: oversold — heavy selling volume at compressed prices.
- MFI divergence from price: same logic as RSI divergence but incorporates volume for higher signal quality.
- MFI > 80 followed by a drop below 80: potential Y signal in range.
- MFI < 20 followed by a rise above 20: potential X signal in range.

### MFI vs RSI
- MFI incorporates volume; RSI does not.
- MFI divergence is often earlier than RSI divergence because volume leads price.
- MFI overbought/oversold in a strong trend has the same embedding problem as RSI.
- MFI is preferred when volume data is reliable (equities). Use RSI when volume data is unreliable (forex).

### When to use
- **Volume-confirmed overbought/oversold:** when you want to know whether extreme prices are backed by extreme volume.
- **Divergence detection:** MFI divergence (price higher high, MFI lower high) means volume is not confirming the push — smart money may be distributing.
- **Breakout validation:** a breakout with MFI rising into overbought territory is well-supported. A breakout with MFI declining is suspect.

### Pitfalls
- **Same trend-embedding issue as RSI.** In a strong uptrend, MFI can stay above 80 for extended periods. Do not sell solely because MFI > 80.
- **Volume data quality.** MFI is only as good as the volume data. Crypto wash trading, OTC dark pool volume not reflected in exchange data, and forex tick volume limitations all degrade MFI reliability.
- **Not meaningful on very low volume bars.** Thinly traded instruments produce erratic MFI readings.
- **Period sensitivity.** MFI(7) is much noisier than MFI(14). Stick with 14 unless backtesting justifies otherwise.

---

## General guidelines for volume indicator usage

1. **Volume confirms price.** A price move on expanding volume is more trustworthy than one on declining volume. This is the single most important volume principle.
2. **Divergence is the primary signal.** Volume indicators diverging from price (OBV falling while price rises) is the earliest reliable warning of trend failure.
3. **Volume leads price.** Accumulation/distribution often begins before price moves. OBV and A/D Line changes can precede breakouts by multiple bars.
4. **VWAP is institutional gravity.** During regular trading hours, price respects VWAP as a fair-value line. Trade with VWAP bias, not against it, unless you have a structural reason.
5. **Volume indicators require reliable volume data.** On equities with exchange-reported volume, these indicators work well. On forex (tick volume only), crypto (wash trading), or thinly traded instruments, volume indicators are less reliable.
6. **Breakout + volume expansion = follow-through.** Breakout + volume contraction = false breakout risk. Always check volume on breakout signals.
7. **One volume indicator per decision.** OBV and A/D Line measure similar things (cumulative flow). Pick one. MFI and CMF are both flow-based oscillators. Pick one.

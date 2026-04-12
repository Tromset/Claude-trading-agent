# Journal Entry Schema

Exact JSON schemas for the three journal record types: Entry, Exit, and Override.

## Entry Record Schema

Logged every time an X (buy) action is executed.

```json
{
  "record_type": "ENTRY",
  "id": "uuid-v4",
  "timestamp": "2024-03-15T10:32:00Z",
  "ticker": "AAPL",
  "side": "LONG",
  "qty": 50,
  "entry_price": 172.50,
  "entry_order_type": "LIMIT",
  "stop_price": 168.00,
  "target_price": 181.00,
  "initial_risk_per_share": 4.50,
  "initial_risk_total": 225.00,
  "account_risk_pct": 0.009,
  "position_value": 8625.00,
  "strategy_source": "swing-breakout",
  "confidence": 72,
  "skills_invoked": [
    "price-action-and-market-structure",
    "chart-patterns",
    "technical-indicators",
    "support-resistance-and-fibonacci",
    "volume-analysis",
    "risk-management",
    "pre-trade-checklist-playbook"
  ],
  "rationale": "Daily breakout above 171.50 resistance with volume 1.8x avg. RSI 62 (room to run). ADX 28 trending. Cup-and-handle on 4H. Stop below handle low.",
  "screenshot_ref": "screenshots/2024-03-15/AAPL-entry-1032.png",
  "account_mode": "PAPER",
  "account_id": "TV-paper-001",
  "checklist_result": {
    "all_passed": true,
    "steps_passed": 12,
    "steps_total": 12
  }
}
```

### Field Definitions — Entry

| Field | Type | Required | Description |
|---|---|---|---|
| record_type | string | Yes | Always `"ENTRY"` |
| id | string (UUID v4) | Yes | Unique identifier for this trade |
| timestamp | string (ISO 8601) | Yes | When the entry order was filled |
| ticker | string | Yes | Instrument symbol |
| side | enum: LONG, SHORT | Yes | Trade direction |
| qty | number | Yes | Number of shares/contracts |
| entry_price | number | Yes | Actual fill price |
| entry_order_type | enum: MARKET, LIMIT, STOP, STOP_LIMIT | Yes | Order type used |
| stop_price | number | Yes | Initial protective stop price |
| target_price | number | Yes | Initial profit target price |
| initial_risk_per_share | number | Yes | `|entry_price - stop_price|` |
| initial_risk_total | number | Yes | `initial_risk_per_share × qty` = 1R |
| account_risk_pct | number | Yes | `initial_risk_total / account_equity` |
| position_value | number | Yes | `entry_price × qty` |
| strategy_source | string | Yes | Which strategy triggered this trade |
| confidence | number (0–100) | Yes | From `buy-sell-hold-decision` |
| skills_invoked | array of strings | Yes | All skills consulted for this decision |
| rationale | string | Yes | Free-text explanation of the trade thesis |
| screenshot_ref | string | Yes | Path/URL to the entry screenshot |
| account_mode | enum: PAPER, LIVE | Yes | Paper or live account |
| account_id | string | Yes | Account identifier |
| checklist_result | object | Yes | Summary from `pre-trade-checklist-playbook` |

## Exit Record Schema

Logged every time a Y (sell) action is executed. Extends the entry record.

```json
{
  "record_type": "EXIT",
  "id": "uuid-v4-same-as-entry",
  "entry_timestamp": "2024-03-15T10:32:00Z",
  "exit_timestamp": "2024-03-19T14:15:00Z",
  "ticker": "AAPL",
  "side": "LONG",
  "qty": 50,
  "entry_price": 172.50,
  "stop_price": 168.00,
  "target_price": 181.00,
  "exit_price": 179.80,
  "exit_order_type": "LIMIT",
  "exit_reason": "TARGET_HIT",
  "initial_risk_per_share": 4.50,
  "initial_risk_total": 225.00,
  "realized_pnl": 365.00,
  "R_multiple": 1.62,
  "holding_period_bars": 18,
  "holding_period_duration": "4d 3h 43m",
  "fees_commissions": 0.00,
  "net_pnl": 365.00,
  "post_trade_analysis": "Target nearly reached at 179.80 — took profit at 98% of target. Pattern played out as expected. Volume confirmed breakout. Held through one pullback to 174 which tested conviction but stop was never threatened.",
  "exit_screenshot_ref": "screenshots/2024-03-19/AAPL-exit-1415.png",
  "strategy_source": "swing-breakout",
  "account_mode": "PAPER",
  "lessons": [
    "Patience through the pullback was correct — thesis remained intact.",
    "Could have trailed stop to breakeven after 2R of price movement."
  ]
}
```

### Field Definitions — Exit

| Field | Type | Required | Description |
|---|---|---|---|
| record_type | string | Yes | Always `"EXIT"` |
| id | string (UUID v4) | Yes | Same ID as the entry record |
| entry_timestamp | string | Yes | Original entry time |
| exit_timestamp | string | Yes | When the exit order was filled |
| exit_price | number | Yes | Actual exit fill price |
| exit_order_type | enum | Yes | Order type used for exit |
| exit_reason | enum | Yes | See exit reasons below |
| realized_pnl | number | Yes | `(exit_price - entry_price) × qty` for LONG; inverse for SHORT |
| R_multiple | number | Yes | `realized_pnl / initial_risk_total` |
| holding_period_bars | number | Yes | Number of candles held (timeframe-specific) |
| holding_period_duration | string | Yes | Human-readable duration |
| fees_commissions | number | Yes | Total fees (0 in paper) |
| net_pnl | number | Yes | `realized_pnl - fees_commissions` |
| post_trade_analysis | string | Yes | Retrospective analysis |
| exit_screenshot_ref | string | Yes | Path/URL to exit screenshot |
| lessons | array of strings | No | Key takeaways from this trade |

### Exit Reasons

| Reason | Definition |
|---|---|
| STOP_OUT | Stop-loss triggered (planned risk taken) |
| TARGET_HIT | Price reached target (or close enough, ≥ 90% of target) |
| THESIS_BREAK | Original thesis invalidated before stop or target |
| TIME_STOP | Held too long without progress (strategy-defined max hold) |
| RISK_REDUCTION | Portfolio heat exceeded, or correlated-risk reduction needed |
| KILL_SWITCH | Safety kill-switch triggered — emergency flatten |
| TRAILING_STOP | Trailing stop triggered (profit protection) |
| MANUAL_OVERRIDE | Human operator requested exit |

## Override Record Schema

Logged every time a would-be X or Y is blocked (loud Z).

```json
{
  "record_type": "OVERRIDE",
  "id": "uuid-v4",
  "timestamp": "2024-03-20T09:45:00Z",
  "would_have_been": "X",
  "original_signal": {
    "ticker": "TSLA",
    "side": "LONG",
    "entry_price": 178.00,
    "stop_price": 172.00,
    "target_price": 192.00,
    "confidence": 65,
    "strategy_source": "breakout"
  },
  "blocking_skill": "pre-trade-checklist-playbook",
  "blocking_step": 2,
  "blocking_step_name": "news_macro_check",
  "blocking_invariant": "INV-006: news_blackout",
  "rationale": "FOMC rate decision at 14:00 ET — within 30-minute blackout window. Breakout signal is valid but execution must wait until post-announcement volatility settles.",
  "resolution": "DEFERRED",
  "deferred_until": "2024-03-20T14:45:00Z",
  "screenshot_ref": "screenshots/2024-03-20/TSLA-override-0945.png"
}
```

### Field Definitions — Override

| Field | Type | Required | Description |
|---|---|---|---|
| record_type | string | Yes | Always `"OVERRIDE"` |
| id | string (UUID v4) | Yes | Unique identifier |
| timestamp | string | Yes | When the override occurred |
| would_have_been | enum: X, Y | Yes | The action that was blocked |
| original_signal | object | Yes | The complete proposed action that was blocked |
| blocking_skill | string | Yes | Which skill issued the block |
| blocking_step | number | No | Checklist step number (if blocked by checklist) |
| blocking_step_name | string | No | Checklist step name |
| blocking_invariant | string | No | Which global invariant was violated |
| rationale | string | Yes | Why the block was issued |
| resolution | enum: CANCELLED, DEFERRED, REVISED | Yes | What happened to the trade |
| deferred_until | string | No | If deferred, when to re-evaluate |
| screenshot_ref | string | No | Screenshot at time of override |

### Resolution Types

| Resolution | Meaning |
|---|---|
| CANCELLED | Trade idea abandoned entirely |
| DEFERRED | Trade idea saved for later re-evaluation |
| REVISED | Trade parameters modified and re-submitted through checklist |

## Validation Rules

1. Every ENTRY must eventually have a matching EXIT (same `id`). Open positions have ENTRY but no EXIT yet.
2. `R_multiple` must equal `realized_pnl / initial_risk_total` (± 0.01 for rounding).
3. `account_risk_pct` must be ≤ 0.01 (1% rule) for new entries.
4. `confidence` must be ≥ 60 for live trades, ≥ 50 for paper trades.
5. `skills_invoked` must include at minimum: one analysis skill, `risk-management`, and `pre-trade-checklist-playbook`.
6. `screenshot_ref` must not be empty — every action requires visual evidence.
7. Override records must have `would_have_been` matching the original signal type.

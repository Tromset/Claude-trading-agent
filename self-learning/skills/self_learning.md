# Skill: Self-Learning

## Purpose
Continuously improve strategy weights and trading decisions by recording trade outcomes,
updating strategy weights via performance feedback, and generating Claude-powered insights
from recent trade history.

## How It Works

### 1. Record Trade Outcomes
After each closed trade, record the result so the system can learn:
```python
from src import SelfLearner
from src.trading_strategy import TradeSignal, Signal

learner = SelfLearner()
signal = TradeSignal("AAPL", Signal.BUY, 0.75, 185.0, "RSI oversold", "rsi")
outcome = {"exit_price": 192.0, "pnl_pct": 0.038, "hold_days": 12, "exit_reason": "take_profit"}
learner.record_trade(signal, outcome)
```

### 2. Update Strategy Weights
Weights are adjusted based on each strategy's rolling win-rate and average P&L.
Strategies that outperform receive higher weights; underperformers are downweighted.
```python
updated_weights = learner.update_strategy_weights()
print(updated_weights)
# {"ma_crossover": 1.24, "rsi": 0.87, "bollinger_bands": 1.05, "consensus": 1.0}
```

### 3. Generate Learning Insights
Ask Claude to synthesise patterns from the last 20 trades:
```python
insight = learner.generate_learning_insight()
print(insight)
```

### 4. Provide Context to Claude Advisor
Pass historical context for a specific symbol/strategy pair to the advisory skill:
```python
context = learner.get_context_for_advisor("AAPL", "rsi")
# "Historical context for AAPL/rsi: 8 recent trades, 6/8 wins, avg P&L 2.10%, ..."
```

### 5. Claude Memory
Beyond strategy weights, Claude keeps a **persistent memory** of what it learned,
so each new session starts with everything learned so far. This is implemented by
the dependency-free `ClaudeMemory` class in `self-learning/claude_memory.py`, with
storage under `self-learning/memory/`.

```python
from claude_memory import ClaudeMemory

mem = ClaudeMemory()

# Learn from a closed trade (records a lesson + updates aggregate stats)
mem.learn_from_trade({
    "symbol": "AAPL", "strategy": "rsi",
    "pnl_pct": 0.038, "exit_reason": "take_profit", "hold_days": 12,
})

# Claude can change its own memory: durable rules / convictions
mem.update_memory("rule:no_fomc_trades", True)

# Recall relevant lessons to inform a new decision
context = mem.get_context_for_advisor("AAPL", "rsi")

# At the end of a session, consolidate lessons into long-term memory
mem.end_session()
```

| Method | Role |
|---|---|
| `learn_from_trade(trade)` | Derive and store a lesson from a closed trade |
| `record_lesson(text, tags)` | Store a free-form lesson Claude wants to remember |
| `update_memory(key, value)` | Let Claude edit its persistent rules/convictions |
| `recall(...)` / `get_context_for_advisor(...)` | Retrieve relevant memory as context |
| `end_session()` / `consolidate()` | Merge the session into long-term memory |

## Persistent Storage
Strategy-learning data is stored as JSON in the `data/` directory:
- `data/trade_history.json` — raw trade records
- `data/strategy_weights.json` — current strategy weights
- `data/learning_log.json` — Claude learning insights log

Claude's cross-session memory lives in `self-learning/memory/`:
- `memory/memory.json` — consolidated long-term memory (stats, lessons, rules)
- `memory/MEMORY.md` — human/Claude-readable summary (auto-regenerated)
- `memory/sessions/<id>.json` — raw lessons recorded per session

## CLI
```bash
python main.py learn
```

# Claude-trading-agent

This project has for ambition to create a Claude–Warren-Buffett bot that trades automatically.

It merges two previously separate efforts:

1. **A Claude trading-skills library** (`.claude/skills/`) — ~25 progressive-disclosure
   skills covering market structure, technical analysis, chart patterns, risk
   management, execution, psychology, regulations and more. These are the skills the
   agent loads at runtime to reason about a trade.
2. **A self-learning trading system** (`self-learning/`) — a Python pipeline that
   combines technical-analysis strategies with Claude-powered signal validation and a
   feedback loop that continuously updates strategy weights based on past trade
   performance. (Originally the `self-learning-claude-trade` repo.)

## Repository layout

```
Claude-trading-agent/
├── .claude/
│   └── skills/               # Runtime Claude trading skills (trading-master, claude-trade, …)
├── self-learning/
│   └── skills/               # Module docs for the self-learning Python system
├── tradingview-mcp/          # MCP server: TradingView webhooks + Twelve Data market data
└── README.md
```

## TradingView MCP server

`tradingview-mcp/` is a TypeScript MCP server that exposes live market data
(Twelve Data) and TradingView webhook alerts to Claude via stdio. See
`tradingview-mcp/README.md` for setup. Tools: `get_quote`, `get_indicator`,
`get_alerts`, `get_history`.

## Self-learning system skills

| Skill | File | Description |
|---|---|---|
| Market Analysis | `self-learning/skills/market_analysis.md` | Fetch data and compute indicators |
| Technical Analysis | `self-learning/skills/technical_analysis.md` | 15+ technical indicators (RSI, MACD, BB, …) |
| Signal Generation | `self-learning/skills/signal_generation.md` | Generate BUY/SELL/HOLD signals |
| Claude Advisory | `self-learning/skills/claude_advisory.md` | AI-powered signal validation |
| Risk Management | `self-learning/skills/risk_management.md` | Position sizing and risk checks |
| Portfolio | `self-learning/skills/portfolio.md` | Portfolio state, stop/TP management |
| Backtesting | `self-learning/skills/backtesting.md` | Historical strategy evaluation |
| Self Learning | `self-learning/skills/self_learning.md` | Adaptive strategy weight updates |

## Claude trading-skills library

See `.claude/skills/README.md` and `.claude/skills/trading-master/` for the routing
entry point and the full skill index.

## Disclaimer

This project is for educational purposes only. It is not financial advice.
Always conduct your own research before making any investment decisions.

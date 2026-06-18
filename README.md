# Claude-trading-agent

This project has for ambition to create a Claude–Warren-Buffett bot that trades automatically.

It brings together three building blocks:

1. **A Claude trading-skills library** (`.claude/skills/`) — ~25 progressive-disclosure
   skills covering market structure, technical analysis, chart patterns, risk
   management, execution, psychology, regulations and more. These are the skills the
   agent loads at runtime to reason about a trade.
2. **A self-learning trading system** (`self-learning/`) — a Python pipeline that
   combines technical-analysis strategies with Claude-powered signal validation and a
   feedback loop that continuously updates strategy weights based on past trade
   performance. It also keeps a **persistent cross-session memory** so Claude learns
   from its own trades over time. (Originally the `self-learning-claude-trade` repo.)
3. **A TradingView MCP server** (`tradingview-mcp/`) — a Model Context Protocol plugin
   that gives Claude live market data (Twelve Data) and TradingView webhook alerts,
   directly inside Claude Desktop.

## Repository layout

```
Claude-trading-agent/
├── .claude/
│   └── skills/               # Runtime Claude trading skills (trading-master, claude-trade, …)
├── self-learning/
│   ├── skills/               # Module docs for the self-learning Python system
│   ├── claude_memory.py      # Persistent, self-updating memory of Claude's trades
│   └── memory/               # Where Claude stores what it learned each session
├── tradingview-mcp/          # MCP server: TradingView webhooks + Twelve Data market data
└── README.md
```

## TradingView MCP server (plugin)

`tradingview-mcp/` is a TypeScript MCP server that exposes live market data
(Twelve Data) and TradingView webhook alerts to Claude via stdio. Tools:
`get_quote`, `get_indicator`, `get_alerts`, `get_history`. Full details in
[`tradingview-mcp/README.md`](tradingview-mcp/README.md).

### Install the plugin in Claude Desktop

**1. Get a (free) Twelve Data API key**

Register at <https://twelvedata.com/register> (free tier: 500 requests/day) and
copy your key.

**2. Build the server**

```bash
cd tradingview-mcp
npm install
cp .env.example .env        # then put your TWELVE_DATA_API_KEY inside
npm run build               # compiles TypeScript to dist/
```

**3. Register it with Claude Desktop**

Open your `claude_desktop_config.json`:

- **macOS**: `~/Library/Application Support/Claude/claude_desktop_config.json`
- **Windows**: `%APPDATA%\Claude\claude_desktop_config.json`

and add the server (adapt the absolute path and key):

```json
{
  "mcpServers": {
    "tradingview": {
      "command": "node",
      "args": ["/absolute/path/to/tradingview-mcp/dist/index.js"],
      "env": {
        "TWELVE_DATA_API_KEY": "your_key_here",
        "WEBHOOK_PORT": "3001"
      }
    }
  }
}
```

**4. Restart Claude Desktop**

Quit and reopen Claude Desktop. The `tradingview` tools (`get_quote`,
`get_indicator`, `get_alerts`, `get_history`) now appear in the 🔌 tools menu.

**5. (Optional) Wire up TradingView alerts**

To feed Pine-script alerts into `get_alerts`, point a TradingView webhook at your
running server (use `ngrok http 3001` to expose it during development):

- **URL**: `http://your-ip:3001/webhook`
- **Message**:

```json
{"ticker": "{{ticker}}", "price": {{close}}, "action": "BUY", "time": "{{time}}"}
```

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
| Self Learning | `self-learning/skills/self_learning.md` | Adaptive strategy weights + persistent cross-session memory |

The self-learning system also includes `claude_memory.py` (`ClaudeMemory`), a
dependency-free module that lets Claude learn from each closed trade and persist
those lessons in `self-learning/memory/` across sessions. See
[`self-learning/memory/README.md`](self-learning/memory/README.md).

## Claude trading-skills library

See `.claude/skills/README.md` and `.claude/skills/trading-master/` for the routing
entry point and the full skill index.

## Disclaimer

This project is for educational purposes only. It is not financial advice.
Always conduct your own research before making any investment decisions.

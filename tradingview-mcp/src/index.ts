import { McpServer } from "@modelcontextprotocol/sdk/server/mcp.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import { z } from "zod";
import { getQuote, getIndicator, getHistory } from "./market-data.js";
import { getAllAlerts, startWebhookListener } from "./webhook.js";

const server = new McpServer({
  name: "tradingview-mcp",
  version: "1.0.0",
});

// Tool 1 : Prix en temps réel
server.registerTool(
  "get_quote",
  {
    description: "Récupère le prix actuel, volume et variation d'un ticker",
    // Note: le SDK MCP attend un ZodRawShape (objet de champs zod), pas un z.object(...)
    inputSchema: {
      symbol: z.string().describe("Ex: AAPL, XAUUSD, BTC/USD"),
      exchange: z.string().optional().describe("Ex: NASDAQ, FOREXCOM"),
    },
  },
  async ({ symbol, exchange }) => {
    const data = await getQuote(symbol, exchange);
    return {
      content: [{ type: "text", text: JSON.stringify(data, null, 2) }],
    };
  }
);

// Tool 2 : Indicateurs techniques
server.registerTool(
  "get_indicator",
  {
    description: "RSI, MACD, EMA, Bollinger Bands sur n'importe quel symbole",
    inputSchema: {
      symbol: z.string(),
      indicator: z.enum(["RSI", "MACD", "EMA", "BBANDS", "SMA"]),
      interval: z.enum(["1min", "5min", "15min", "1h", "4h", "1day"]),
      period: z.number().optional().default(14),
    },
  },
  async (params) => {
    const data = await getIndicator(params);
    return {
      content: [{ type: "text", text: JSON.stringify(data, null, 2) }],
    };
  }
);

// Tool 3 : Alertes reçues depuis TradingView
server.registerTool(
  "get_alerts",
  {
    description: "Retourne les dernières alertes reçues depuis TradingView webhooks",
    inputSchema: {
      limit: z.number().optional().default(10),
      symbol: z.string().optional(),
    },
  },
  async ({ limit, symbol }) => {
    const alerts = getAllAlerts(limit, symbol);
    return {
      content: [{ type: "text", text: JSON.stringify(alerts, null, 2) }],
    };
  }
);

// Tool 4 : Historique OHLCV
server.registerTool(
  "get_history",
  {
    description: "Données OHLCV historiques pour analyse ou backtest",
    inputSchema: {
      symbol: z.string(),
      interval: z.enum(["1min", "5min", "1h", "1day", "1week"]),
      outputsize: z.number().optional().default(100),
    },
  },
  async (params) => {
    const data = await getHistory(params);
    return {
      content: [{ type: "text", text: JSON.stringify(data, null, 2) }],
    };
  }
);

// Démarre l'écoute des webhooks TradingView (port configurable via WEBHOOK_PORT)
startWebhookListener();

const transport = new StdioServerTransport();
await server.connect(transport);
console.error("tradingview-mcp connecté via stdio");

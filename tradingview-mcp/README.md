# tradingview-mcp

Serveur **MCP** (Model Context Protocol) qui expose à Claude :

1. **Les données de marché** (prix, indicateurs techniques, OHLCV) via l'API **Twelve Data** ;
2. **Les alertes TradingView** reçues par **webhook** depuis vos scripts Pine.

> ⚠️ TradingView n'a pas d'API publique officielle pour les données temps réel
> (réservée aux partenaires institutionnels). Cette architecture combine donc
> les **webhooks TradingView** (option A) et une source de données de marché
> propre, **Twelve Data** (option B).

```
Pine Script Alert → Webhook → serveur Express → MCP → Claude
                       Twelve Data API ↗
```

## Outils exposés

| Outil | Description |
|---|---|
| `get_quote` | Prix actuel, volume et variation d'un ticker |
| `get_indicator` | RSI, MACD, EMA, BBANDS, SMA sur n'importe quel symbole |
| `get_alerts` | Dernières alertes reçues depuis les webhooks TradingView |
| `get_history` | Données OHLCV historiques (analyse / backtest) |

## Installation

```bash
cd tradingview-mcp
npm install
cp .env.example .env        # puis renseignez TWELVE_DATA_API_KEY
npm run build
```

Clé Twelve Data gratuite (500 req/jour) : https://twelvedata.com/register

## Stack

TypeScript + `@modelcontextprotocol/sdk`, transport **stdio** pour Claude Desktop,
serveur **Express** pour les webhooks.

## Configuration Claude Desktop

Copiez `claude_desktop_config.example.json` dans votre `claude_desktop_config.json`
en adaptant le chemin et la clé :

```json
{
  "mcpServers": {
    "tradingview": {
      "command": "node",
      "args": ["/chemin/vers/tradingview-mcp/dist/index.js"],
      "env": {
        "TWELVE_DATA_API_KEY": "votre_cle_ici",
        "WEBHOOK_PORT": "3001"
      }
    }
  }
}
```

## Configuration côté TradingView

Dans une alerte Pine, configurez le webhook :

- **URL** : `http://votre-ip:3001/webhook`
- **Corps (message)** :

```json
{"ticker": "{{ticker}}", "price": {{close}}, "action": "BUY", "time": "{{time}}"}
```

Pour exposer le webhook publiquement en développement :

```bash
ngrok http 3001
```

## Notes d'implémentation

- Le SDK MCP attend un `inputSchema` sous forme de **ZodRawShape** (objet de
  champs zod), et non un `z.object(...)` — c'est la forme utilisée dans `src/index.ts`.
- Les logs du listener de webhooks sont écrits sur **stderr** pour ne pas
  corrompre le canal **stdio** utilisé par le protocole MCP.
- Les alertes sont conservées en mémoire (cap à 500, plus récentes en premier).
  Pour de la persistance, branchez une base / un fichier dans `src/webhook.ts`.

## Structure

```
tradingview-mcp/
├── src/
│   ├── index.ts          # Serveur MCP + enregistrement des outils
│   ├── webhook.ts        # Réception des alertes TradingView (Express)
│   └── market-data.ts    # Connecteur Twelve Data (quote / indicateurs / OHLCV)
├── package.json
├── tsconfig.json
├── .env.example
└── claude_desktop_config.example.json
```

## Avertissement

Projet à but éducatif. Ceci n'est pas un conseil financier. Faites toujours vos
propres recherches avant toute décision d'investissement.

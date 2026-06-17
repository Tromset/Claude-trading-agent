import express from "express";

export interface Alert {
  ticker?: string;
  price?: number;
  action?: string;
  time?: string;
  receivedAt: string;
  [key: string]: unknown;
}

const alerts: Alert[] = [];
const MAX_ALERTS = 500;
const PORT = Number(process.env.WEBHOOK_PORT ?? 3001);

/**
 * Démarre l'endpoint Express qui reçoit les alertes TradingView.
 * Les logs vont sur stderr pour ne pas polluer le canal stdio du MCP.
 */
export function startWebhookListener() {
  const app = express();
  app.use(express.json());

  // TradingView envoie ses alertes ici
  app.post("/webhook", (req, res) => {
    const alert: Alert = { ...req.body, receivedAt: new Date().toISOString() };
    alerts.unshift(alert); // plus récent en premier
    if (alerts.length > MAX_ALERTS) alerts.pop(); // cap mémoire
    res.sendStatus(200);
  });

  // Petit endpoint de santé pratique pour ngrok / debug
  app.get("/health", (_req, res) => res.json({ ok: true, count: alerts.length }));

  app.listen(PORT, () => console.error(`Webhook listener sur :${PORT}`));
}

export function getAllAlerts(limit = 10, symbol?: string): Alert[] {
  return alerts.filter((a) => !symbol || a.ticker === symbol).slice(0, limit);
}

export function getLastAlert(symbol?: string): Alert | null {
  return getAllAlerts(1, symbol)[0] ?? null;
}

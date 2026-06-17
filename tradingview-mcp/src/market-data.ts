import axios from "axios";

const BASE_URL = "https://api.twelvedata.com";
const API_KEY = process.env.TWELVE_DATA_API_KEY;

function assertKey() {
  if (!API_KEY) {
    throw new Error(
      "TWELVE_DATA_API_KEY manquante. Obtenez une clé gratuite sur https://twelvedata.com/register"
    );
  }
}

export interface IndicatorParams {
  symbol: string;
  indicator: "RSI" | "MACD" | "EMA" | "BBANDS" | "SMA";
  interval: "1min" | "5min" | "15min" | "1h" | "4h" | "1day";
  period?: number;
}

export interface HistoryParams {
  symbol: string;
  interval: "1min" | "5min" | "1h" | "1day" | "1week";
  outputsize?: number;
}

export async function getQuote(symbol: string, exchange?: string) {
  assertKey();
  const params: Record<string, unknown> = { symbol, apikey: API_KEY };
  if (exchange) params.exchange = exchange;

  const [{ data: price }, { data: meta }] = await Promise.all([
    axios.get(`${BASE_URL}/price`, { params }),
    axios.get(`${BASE_URL}/quote`, { params }),
  ]);

  return { price: price.price, ...meta };
}

export async function getIndicator({ symbol, indicator, interval, period = 14 }: IndicatorParams) {
  assertKey();
  const { data } = await axios.get(`${BASE_URL}/${indicator.toLowerCase()}`, {
    params: { symbol, interval, time_period: period, apikey: API_KEY },
  });
  return data;
}

export async function getHistory({ symbol, interval, outputsize = 100 }: HistoryParams) {
  assertKey();
  const { data } = await axios.get(`${BASE_URL}/time_series`, {
    params: { symbol, interval, outputsize, apikey: API_KEY },
  });
  return data;
}

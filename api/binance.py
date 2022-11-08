import pandas as pd
import requests

BINANCE_URL = "https://api.binance.com/api/v3"

COLUMNS = ["open_time", "open", "high", "low", "close", "volume", "close_time",
           "quote_volume", "trades", "taker_buy_base", "taker_buy_quote", "ignore"]


def fetch_candles(symbol, interval, limit):
    params = {"symbol": symbol, "interval": interval, "limit": limit}
    response = requests.get(f"{BINANCE_URL}/klines", params=params, timeout=10)
    response.raise_for_status()

    df = pd.DataFrame(response.json(), columns=COLUMNS)
    df = df[["open_time", "open", "high", "low", "close", "volume"]].astype(float)
    df["open_time"] = pd.to_datetime(df["open_time"], unit="ms")

    return df.set_index("open_time")

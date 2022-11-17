import pandas as pd
import requests

KRAKEN_URL = "https://api.kraken.com/0/public"

INTERVALS = {"1h": 60, "4h": 240, "1d": 1440, "1w": 10080}

COLUMNS = ["open_time", "open", "high", "low", "close", "vwap", "volume", "count"]


def fetch_candles(symbol, interval, limit):
    # kraken call bitcoin XBT
    params = {"pair": symbol.replace("BTC", "XBT"), "interval": INTERVALS[interval]}
    response = requests.get(f"{KRAKEN_URL}/OHLC", params=params, timeout=10)
    response.raise_for_status()

    data = response.json()
    if data["error"]:
        raise Exception(f"Kraken error: {data['error']}")

    pair = [key for key in data["result"] if key != "last"][0]

    df = pd.DataFrame(data["result"][pair], columns=COLUMNS)
    df = df[["open_time", "open", "high", "low", "close", "volume"]].astype(float)
    df["open_time"] = pd.to_datetime(df["open_time"], unit="s")

    return df.set_index("open_time").tail(limit)

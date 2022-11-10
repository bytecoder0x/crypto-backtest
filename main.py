import os

import config
from api.binance import fetch_candles


def main():
    print(f"Fetching {config.LIMIT} {config.INTERVAL} candles for {config.SYMBOL}...")
    df = fetch_candles(config.SYMBOL, config.INTERVAL, config.LIMIT)
    print(f"Got {len(df)} candles from {df.index[0].date()} to {df.index[-1].date()}")

    os.makedirs(config.DATA_DIR, exist_ok=True)
    csv_path = os.path.join(config.DATA_DIR, f"{config.SYMBOL}_{config.INTERVAL}.csv")

    df.to_csv(csv_path)
    print(f"\nSaved {csv_path}")


if __name__ == "__main__":
    main()

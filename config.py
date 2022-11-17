EXCHANGES = ["binance", "kraken"]
SYMBOL = "BTCUSDT"
INTERVAL = "1d"  # 1h, 4h, 1d, 1w
LIMIT = 720  # candles per exchange kraken give max 720

FAST_WINDOW = 20
SLOW_WINDOW = 50
VOLATILITY_WINDOW = 20

START_BALANCE = 1000  # USDT
FEES = {"binance": 0.001, "kraken": 0.0026}  # taker fee on spot

DATA_DIR = "data"

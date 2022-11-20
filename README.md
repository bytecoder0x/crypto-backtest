# crypto-backtest

## Description

Python script for analyzing crypto prices. It downloads historical candles from Binance and Kraken public API (no api key needed), calculates returns, moving averages and volatility with pandas and runs backtest of SMA crossover strategy. The same strategy is tested on every exchange with own trading fee, then it compare the result with buy and hold, save all data to csv and draw the chart. Exchanges, symbol, interval and strategy parameters you can change in `config.py`

## Key Features

- Historical candles (OHLCV) from Binance and Kraken public API
- Returns, moving averages, volatility and drawdown calculated with pandas
- Backtest of SMA crossover strategy with trading fee of each exchange
- Comparison with buy and hold: total return, max drawdown, sharpe ratio, number of trades
- Export of all data to csv
- Chart with price, moving averages and equity curve for every exchange

## Technologies

- Python
- Requests
- Pandas
- NumPy
- Matplotlib
- Binance API
- Kraken API

## Running the Project

1. Clone the repository
2. Install dependencies (python 3.10 or 3.11): `pip install -r requirements.txt`
3. Run the script: `python main.py`

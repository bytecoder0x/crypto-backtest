import os

import config
from analysis.backtest import get_summary, run_backtest
from analysis.chart import save_chart
from analysis.indicators import add_indicators
from api import binance, kraken

EXCHANGES = {"binance": binance, "kraken": kraken}


def print_summary(summary):
    print(f"Trades: {summary['trades']}")
    print(f"Time in market: {summary['time_in_market']:.1%}")
    print(f"Strategy return: {summary['strategy_return']:+.1%}")
    print(f"Buy and hold return: {summary['hold_return']:+.1%}")
    print(f"Max drawdown: {summary['max_drawdown']:.1%}")
    print(f"Sharpe ratio: {summary['sharpe']:.2f}")


def run(exchange_name):
    exchange = EXCHANGES[exchange_name]
    fee = config.FEES[exchange_name]

    print(f"\n=== {exchange_name} ===")
    print(f"Fetching {config.LIMIT} {config.INTERVAL} candles for {config.SYMBOL}...")
    df = exchange.fetch_candles(config.SYMBOL, config.INTERVAL, config.LIMIT)
    print(f"Got {len(df)} candles from {df.index[0].date()} to {df.index[-1].date()}")

    df = add_indicators(df, config.FAST_WINDOW, config.SLOW_WINDOW, config.VOLATILITY_WINDOW)
    df = run_backtest(df, fee, config.START_BALANCE)

    print(f"\nSMA {config.FAST_WINDOW}/{config.SLOW_WINDOW} crossover, fee {fee:.2%}")
    print_summary(get_summary(df, config.INTERVAL, config.START_BALANCE))

    os.makedirs(config.DATA_DIR, exist_ok=True)
    file_name = f"{exchange_name}_{config.SYMBOL}_{config.INTERVAL}"
    csv_path = os.path.join(config.DATA_DIR, f"{file_name}.csv")
    chart_path = os.path.join(config.DATA_DIR, f"{file_name}.png")

    df.to_csv(csv_path)
    save_chart(df, f"{config.SYMBOL} {config.INTERVAL} ({exchange_name})", config.FAST_WINDOW, config.SLOW_WINDOW, chart_path)
    print(f"\nSaved {csv_path} and {chart_path}")


def main():
    for exchange_name in config.EXCHANGES:
        run(exchange_name)


if __name__ == "__main__":
    main()

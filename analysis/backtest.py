import numpy as np

PERIODS_PER_YEAR = {"1h": 24 * 365, "4h": 6 * 365, "1d": 365, "1w": 52}


def run_backtest(df, fee, start_balance):
    df = df.copy()

    df["signal"] = np.where(df["sma_fast"] > df["sma_slow"], 1, 0)

    # signal we know only on close of candle so trade on next one
    df["position"] = df["signal"].shift(1).fillna(0)

    df["trade"] = df["position"].diff().abs().fillna(0)

    df["strategy_return"] = df["position"] * df["return"] - df["trade"] * fee

    df["equity"] = start_balance * (1 + df["strategy_return"]).cumprod()
    df["hold_equity"] = start_balance * (1 + df["return"]).cumprod()

    return df


def get_summary(df, interval, start_balance):
    strategy_return = df["strategy_return"]
    periods = PERIODS_PER_YEAR[interval]

    return {
        "trades": int(df["trade"].sum()),
        "time_in_market": df["position"].mean(),
        "strategy_return": df["equity"].iloc[-1] / start_balance - 1,
        "hold_return": df["hold_equity"].iloc[-1] / start_balance - 1,
        "max_drawdown": (df["equity"] / df["equity"].cummax() - 1).min(),
        "sharpe": strategy_return.mean() / strategy_return.std() * np.sqrt(periods),
    }

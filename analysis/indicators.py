def add_indicators(df, fast_window, slow_window, volatilty_window):
    df = df.copy()

    df["return"] = df["close"].pct_change().fillna(0)

    df["sma_fast"] = df["close"].rolling(fast_window).mean()
    df["sma_slow"] = df["close"].rolling(slow_window).mean()

    df["volatility"] = df["return"].rolling(volatilty_window).std()

    df["drawdown"] = df["close"] / df["close"].cummax() - 1

    return df

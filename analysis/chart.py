import matplotlib.pyplot as plt


def save_chart(df, title, fast_window, slow_window, path):
    fig, (price_ax, equity_ax) = plt.subplots(2, 1, figsize=(12, 8), sharex=True)

    price_ax.plot(df.index, df["close"], label="Close", color="black", linewidth=1)
    price_ax.plot(df.index, df["sma_fast"], label=f"SMA {fast_window}")
    price_ax.plot(df.index, df["sma_slow"], label=f"SMA {slow_window}")
    price_ax.set_title(title)
    price_ax.set_ylabel("Price, USDT")
    price_ax.legend()

    equity_ax.plot(df.index, df["equity"], label="SMA crossover")
    equity_ax.plot(df.index, df["hold_equity"], label="Buy and hold")
    equity_ax.set_ylabel("Equity, USDT")
    equity_ax.legend()

    fig.tight_layout()
    fig.savefig(path)
    plt.close(fig)

import pandas as pd


def generate_signal(df, window):
    """
    Calculate rolling mean and generate trading signal.
    """

    # Rolling Mean
    df["rolling_mean"] = df["close"].rolling(window=window).mean()

    # Signal
    df["signal"] = (df["close"] > df["rolling_mean"]).astype(int)

    return df
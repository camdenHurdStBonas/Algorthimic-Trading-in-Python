import ccxt
import pandas as pd
import numpy as np

def get_historical_data(symbol, timeframe='1d', limit=365):
    """
    Example function: fetch daily OHLCV from ccxt exchange.
    Return a cleaned DataFrame with columns: [timestamp, open, high, low, close, volume].
    """
    exchange = ccxt.coinbase()  # or whichever
    ohlcv = exchange.fetch_ohlcv(symbol, timeframe=timeframe, limit=limit)
    df = pd.DataFrame(ohlcv, columns=['timestamp','open','high','low','close','volume'])
    df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms', utc=True)
    df.dropna(inplace=True)
    # Add your log returns, volume changes, etc.
    return df

def compute_rsi(series, window=14):
    """
    Basic RSI example
    """
    delta = series.diff()
    gain = (delta.where(delta > 0, 0)).rolling(window).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window).mean()
    rs = gain / loss
    rsi = 100 - (100 / (1 + rs))
    return rsi

import logging
import ccxt
import pandas as pd
import numpy as np
from datetime import datetime

def get_historical_data(symbol: str):
    """
    Fetches daily OHLCV data up to 'yesterday'.
    Returns a DataFrame with columns:
      timestamp, open, high, low, close, volume, returns, vol_changes
    """
    try:
        logging.info(f"📥 Fetching historical data for {symbol}...")
        exchange = ccxt.coinbase()

        # For example, get daily OHLCV
        ohlcv = exchange.fetch_ohlcv(symbol, timeframe='1d')
        if not ohlcv:
            logging.warning(f"No data received for {symbol}.")
            return None

        df = pd.DataFrame(ohlcv, columns=['timestamp','open','high','low','close','volume'])
        df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms', utc=True)

        # Example: remove "today" data if you want strictly up to yesterday
        today_utc = pd.Timestamp.utcnow().normalize().tz_convert("UTC")
        df = df[df['timestamp'] < today_utc]

        # Compute log returns & volume changes as placeholders
        df['returns'] = np.log(df['close'] / df['close'].shift(1))
        df['vol_changes'] = np.log(df['volume'] / df['volume'].shift(1))

        df.dropna(inplace=True)

        logging.info(f"✅ {symbol} Data Loaded. Last date: {df['timestamp'].max()}")
        return df

    except Exception as e:
        logging.error(f"Error fetching data for {symbol}: {e}")
        return None

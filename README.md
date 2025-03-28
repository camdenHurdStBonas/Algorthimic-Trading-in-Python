# Algorithmic-Trading-in-Python

**Disclaimer**: This repository is for **educational purposes only**. The code and ideas here do **not** constitute financial advice. Trading involves significant risk—use at your own discretion and risk.

## Overview

This project demonstrates how to build an **algorithmic cryptocurrency trading bot** in Python, using daily data pipelines, basic risk management, and a machine learning classifier (Random Forest, plus an optional Hidden Markov Model for regime detection).

### Features

- **Historical Data Fetch**: Uses `ccxt` to pull daily OHLCV data from an exchange (e.g., Coinbase).  
- **Indicators & Signals**: Bollinger Bands, RSI, ATR, ADX, Donchian channels, etc.  
- **Hidden Markov Model (HMM)** for market regime detection (optional).  
- **Machine Learning**: Random Forest classifier trained to predict a "Buy Signal."  
- **Trade Execution** (Place orders with an API client; uses Robinhood Crypto in the example).  
- **Risk Management**: Stop-loss, take-profit, and an overall account value check to shut down if below threshold.  
- **Scheduling**: Python `schedule` used to run daily or periodic tasks.

### Important

- **Credentials**: Do **not** commit your actual API keys or secrets.  
- **Proprietary Logic**: The advanced strategy (your “secret sauce”) is **not** included. This repo just shows one possible template.  
- **No Guarantee**: Past performance is not indicative of future results. This code is provided *as is*, with no warranty.  

## Getting Started

1. **Clone the Repo**  
   ```bash
   git clone https://github.com/YourUsername/Algorithmic-Trading-in-Python.git
   ```
2. **Install Dependencies**
  ```bash
  cd Algorithmic-Trading-in-Python
  pip install -r requirements.txt
  ```
3. **Set Up Environment**
- Create a .env (or some config) to store your credentials (exchange, broker, etc.).
- Make sure .env or other secrets are in your .gitignore.
4. **Run the Bot**
   ```bash
   python src/main.py
   ```

### Contributing

- **Contributions are welcome! Feel free to open issues or pull requests.**

### License

- **MIT**

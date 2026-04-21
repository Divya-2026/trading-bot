# Binance Trading Bot

This is a simple Python trading bot using Binance API.

## Features
- Market Buy Orders
- Limit Sell Orders
- CLI-based execution

## Installation

pip install -r requirements.txt

## Usage

Buy:
python app.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001

Sell:
python app.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.001 --price 60000

## Note
This project uses Binance Testnet (no real money).

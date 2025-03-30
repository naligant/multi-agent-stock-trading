import yfinance as yf
import numpy as np

def get_stock_data(ticker, start_date, end_date):
    stock = yf.Ticker(ticker)
    stock_data = stock.history(start=start_date, end=end_date)
    return stock_data

stock_data = get_stock_data("AAPL", "2020-01-01", "2020-12-31")
print(stock_data)
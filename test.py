import yfinance as yf
import csv
import pandas

ticker= yf.Ticker('ABBV')
df = ticker.history(period='1y')
file = df.to_csv()
print(file)

import yfinance as yf
import pandas

schrodinger = yf.Ticker("SDGR")

dataframe = schrodinger.history(period='1y')
DD = dataframe.to_csv()

print(DD)

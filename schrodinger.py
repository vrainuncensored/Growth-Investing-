import yfinance as yf
import pandas

dinger = yf.Ticker("SDGR")

dataframe = dinger.history(period='1y')
DD = dataframe.to_csv()

df = pandas.read_csv('stock.csv')


print(df)

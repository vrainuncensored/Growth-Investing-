import yfinance as yf
import csv
import pandas

compaines = csv.reader(open('snp500.csv'))

for company in compaines:
    symbol, name = company
    history_filename = 'directory/{}.csv'.format(symbol)
    f = open(history_filename, 'w')
    ticker= yf.Ticker(symbol)
    df = ticker.history(period='1y')
    f.write(df.to_csv())
    f.close

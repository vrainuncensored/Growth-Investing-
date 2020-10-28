import yfinance as yf
import csv

spy = yf.Ticker('SPY')

data = spy.history(start='2000-01-01', end='2020-03-15' )
spydata = data.to_csv()

with open('spydata.csv') as f:
    reader = csv.DictReader(f)
    #print(reader)
    candles = list(reader)
    #print(candles)
csv_file = open('editedspydata.csv', 'w')
csv_writer = csv.writer(csv_file)

csv_writer.writerow(['open', 'high', 'low', 'close', 'volume'])

for item in candles:
    csv_writer.writerow([item['Open'], item['High'],item['Low'], item['Close'], item['Volume']])

csv_file.close()

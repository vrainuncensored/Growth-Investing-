import yfinance as yf
import csv

market = yf.Ticker("SPY")

marketHistory = market.history(period="max")
historyCSV = marketHistory.to_csv()

with open('marketHistory.csv') as f:
    reader = csv.DictReader(f)
    #print(reader)
    candles = list(reader)

csv_file = open('editedmarketHistory.csv', 'w')
csv_writer = csv.writer(csv_file)

csv_writer.writerow(['open', 'high', 'low', 'close', 'volume'])

for item in candles:
    csv_writer.writerow([item['Open'], item['High'],item['Low'], item['Close'], item['Volume']])

csv_file.close()

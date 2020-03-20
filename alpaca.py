import requests, json, csv
from config import *
from datetime import datetime

TICKER = 'SDGR'
URL= "https://api.polygon.io/v1/last/stocks/SDGR?apiKey=PK5IS8OLMPTH0Z39F9J1"
HEADERS = {'APCA-API-KEY-ID': API_KEY, 'APCA-API-SECRET-KEY': SECRET_KEY}
POLYGON_URL = 'https://api.polygon.io/v2/aggs/ticker/{}/range/1/day/{}/{}?apiKey={}'
START_DATE = '2020-01-01'
END_DATE = '2020-03-01'

ticker = "https://api.polygon.io/v2/reference/tickers?sort=lkn&market=STOCKS&perpage=50&page=1&apiKey=PK5IS8OLMPTH0Z39F9J1"

r = requests.get(POLYGON_URL.format(TICKER, START_DATE, END_DATE, API_KEY ))
json_data = json.loads(r.content)


csv_file = open('alpaca.csv', 'w')
csv_writer = csv.writer(csv_file)

csv_writer.writerow(['date','open','high','low','close'])


for item in json_data['results']:
    formatted_date = datetime.fromtimestamp( item['t'] / 1000)
    date_only = formatted_date.strftime('%Y-%m-%d')

    csv_writer.writerow([date_only, item['o'], item['h'], item['l'], item['c']])

csv_file.close()
#csv_writer = csv.writer(csv_file)

#csv_writer.writerow(['ticker', 'name', 'market', 'currency'])

#for item in json_data['tickers']:
#    csv_writer.writerow([item['ticker'], item['name'], item['market'], item['currency']])

#csv_file.close()

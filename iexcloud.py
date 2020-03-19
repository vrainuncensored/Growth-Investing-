import requests, json, csv

TOKEN = 'Tpk_07dc85fdb54946b89d0c002f918d83a8'
SYMBOL = 'SD'
URL = "https://sandbox.iexapis.com/stable/stock/{}/chart/ytd?token={}".format( SYMBOL,TOKEN)

r = requests.get(URL)

json_data = json.loads(r.content)

csv_file = open('stock.csv', 'w')
csv_writer = csv.writer(csv_file)

csv_writer.writerow(['date', 'open', 'high', 'low', 'close'])

for item in json_data:
    csv_writer.writerow([item['date'], item['open'], item['high'], item['low'], item['close']])

csv_file.close()

import requests, json
#This is the library we import to successfully make endpoint requests
# we entered into terminal=  "pip3 instal requests"
from config import *
#This is getting all the files from our config file!
BASE_URL = "https://paper-api.alpaca.markets"
ACCOUNT_URL = "{}/v2/account".format(BASE_URL)
ORDERS_URL = "{}/v2/orders".format(BASE_URL)
HEADERS = {'APCA-API-KEY-ID': API_KEY, 'APCA-API-SECRET-KEY': SECRET_KEY}
# the Alpaca documentation requires us include headers which is why we are adding these

#THIS THE METHOD FOR MAKING ADDONS TO A BASE URL FOR MAKING A CALL

def get_account():
    r = requests.get(ACCOUNT_URL, headers= HEADERS )
    #THIS THE METHOD FOR MAKING ADDONS TO A BASE URL FOR MAKING A CALL
    json_format1 = json.loads(r.text)
    print(json_format1['cash'])

def create_order(symbol, qty, side, type, time_in_force):
    data =  {
        "symbol" : symbol,
        "qty" : qty,
        "side" : side,
        "type" : type,
        "time_in_force" : time_in_force
    }
    r = requests.post(ORDERS_URL, json=data,  headers= HEADERS )
    return json.loads(r.content)

def get_order():
    r = requests.get(ORDERS_URL, headers= HEADERS )
    return json.loads(r.content)

#response = create_order("AAPL", 100, "buy", "market", "gtc" )

#print(response)
order = get_order()

#print(order)

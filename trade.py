import requests, json
#This is the library we import to successfully make endpoint requests
# we entered into terminal=  "pip3 instal requests"
from config import *
#This is getting all the files from our config file!
BASE_URL = "https://api.alpaca.markets"
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

def create_order():
    r = requests.get(ACCOUNT_URL, headers= HEADERS )
    json_format2 = json.loads(r.text)
    print(json_format2)
    

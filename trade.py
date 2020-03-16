import requests
#This is the library we import to successfully make endpoint requests
# we entered into terminal=  "pip3 instal requests"

BASE_URL = "https://api.alpaca.markets"

r = requests.get(BASE_URL) 

print(r.content)

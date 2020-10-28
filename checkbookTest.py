import requests
import json

url = "https://www.checkbook.io/v3/bank/institutions"
headers = { "Authorization" : "5b5227726c2e4a848526664ae82f0dc4:e4BL3ivPZ4Or2az1Sxhbuj76NBltjK", "accept" : "application/json"}

response = requests.request("GET", url, headers=headers)
requestText = response.text

data = json.loads(requestText)

id = data['institutions']

for test in id:
    if test['name'] == 'Chase Bank':
        print(test['id'])

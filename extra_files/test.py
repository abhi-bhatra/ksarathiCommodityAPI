import json
import requests

url='https://commodityapi.blob.core.windows.net/commodityapi/db.json'
r = requests.get(url)
data = json.loads(r.text)

state=input("Enter state: ")
district=input("Enter district: ")
commodity = input("Enter commodity: ")
# print(data[0]['district'])
total_length = len(data)

for i in range(total_length):
    if (state in data[i]['state']) and (district in data[i]['district']) and (commodity in data[i]['commodity']):
        print("Maximum Price one can get is ", data[i]['max_price'])
        print("Minimum Price one can get is ", data[i]['min_price'])

# CGI programming: Talk to OS project
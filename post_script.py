import requests
import csv
import json

# https://www.geeksforgeeks.org/python/convert-csv-to-json-using-python/
url = "http://127.0.0.1:8000/items"

with open('MOCK_DATA.csv', mode='r', newline='', encoding='utf-8') as csvfile:
    data = list(csv.DictReader(csvfile))

with open('output.json', mode='w', encoding='utf-8') as jsonfile:
    json.dump(data, jsonfile, indent=4)

with open('output.json', mode='r') as jsoninput:
    data = json.load(jsoninput)

jsondump = json.dumps('output.json')

for item in data:
        print(item)
        print(f"Name: {item['name']} Description: {item['description']}")
        response = requests.post(url, json=item)

    #print(response.text)
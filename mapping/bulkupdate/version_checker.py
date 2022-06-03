import json
import requests

url = 'https://raw.githubusercontent.com/SpielerNogard/mapping/bulkupdate/versions.json'
resp = requests.get(url)
data = json.loads(resp.text)
print(data)

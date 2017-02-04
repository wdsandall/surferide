import requests
import json

fields = "&fields=solidRating,fadedRating"

response = requests.get("http://magicseaweed.com/api/46b2f2f1d095df7f57d4d3a080731311/forecast/?spot_id=1" + fields)

#CHECK THE STATUS
# print(response.status_code)

data = response.json()

# print(data[0]['solidRating'])

'''
for i in data:
    print i
'''

for period in data:
    print(("*" * period['solidRating'])+("-" * period['fadedRating']))


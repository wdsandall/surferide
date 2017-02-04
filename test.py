import requests

fields = "&fields=solidRating,fadedRating,localTimestamp"

response = requests.get("http://magicseaweed.com/api/46b2f2f1d095df7f57d4d3a080731311/forecast/?spot_id=1" + fields)

print(response.status_code)

print(response.content)



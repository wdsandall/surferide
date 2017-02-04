import requests
import json
import time
from datetime import datetime as dt
import pytz


fields = "&fields=solidRating,fadedRating,localTimestamp"

response = requests.get("http://magicseaweed.com/api/46b2f2f1d095df7f57d4d3a080731311/forecast/?spot_id=1" + fields)

#CHECK THE STATUS
# print(response.status_code)

# print(data[0]['solidRating'])

'''
for i in data:
    print i
'''

data = response.json()
good_periods = []
utc = pytz.utc
fmt = "%c"

for period in data:
    print(("*" * period['solidRating'])+("-" * period['fadedRating']))

for period in data:
    if period['solidRating'] >= 3:
        
        #stamp = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(period['localTimestamp']))
        stamp = dt.fromtimestamp(period['localTimestamp'], utc)
        good_periods.append(stamp.strftime(fmt))

        
print(good_periods)




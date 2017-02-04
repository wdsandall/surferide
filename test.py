import requests
import json
from datetime import datetime as dt
import pytz

BEACHES =   {'Newquay': 1, 'Tallow Beach': 1019, 'Byron Bay': 541, 'Bungan': 2928, 'Avalon': 2930}

fields = "&fields=solidRating,fadedRating,localTimestamp"

response = requests.get("http://magicseaweed.com/api/46b2f2f1d095df7f57d4d3a080731311/forecast/?spot_id=1" + fields)

data = response.json()
good_periods = []
utc = pytz.utc
fmt = "%c"

def stamped(epoch_time):
    stamp = dt.fromtimestamp(epoch_time, utc)
    return stamp.strftime(fmt)

'''
for period in data:
    print(("*" * period['solidRating'])+("-" * period['fadedRating']))

for period in data:
    if period['solidRating'] >= 3:
        good_time = stamped(period['localTimestamp'])
        good_periods.append(good_time)

print(good_periods)
'''

for period in data:
    if period['solidRating'] >= 3:
        good_time = stamped(period['localTimestamp'])
        good_stars = "*" * period['solidRating']
        good_stripes = "-" * period['fadedRating']
        print(good_time + good_stars + good_stripes)
        




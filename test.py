import requests
import json
from datetime import datetime as dt
import pytz


FIELDS = "&fields=solidRating,fadedRating,localTimestamp"

URL = "http://magicseaweed.com/api/46b2f2f1d095df7f57d4d3a080731311/forecast/?spot_id="

BEACH_ID =   {'Newquay': 1,
              'Tallow': 1019,
              'Byron Bay': 541,
              'Bungan': 2928,
              'Avalon': 2930}

response = requests.get(URL + str(BEACH_ID['Newquay']) + FIELDS)
data = response.json()
# data is now a list of 40 dictionaries each with a solidRating, fadedRating and localTimestamp field

utc = pytz.utc
fmt = "%c"
def stamped(epoch_time):
    stamp = dt.fromtimestamp(epoch_time, utc)
    return stamp.strftime(fmt)

def print_stars():

    # print("Printing results for " + BEACH_ID)

    for period in data:
        if period['solidRating'] >= 1:
            good_time = stamped(period['localTimestamp'])
            good_stars = "*" * period['solidRating']
            good_stripes = "-" * period['fadedRating']
            print(good_time + "       " +  good_stars + good_stripes)
        
print_stars()

'''
def get_results():
    for key in BEACH_ID:

'''
        

        

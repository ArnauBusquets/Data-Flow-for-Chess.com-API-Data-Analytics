import urllib.request
import json
from collections import Counter

'''
name = 'Busi_jr'
# raw_data = urllib.request.urlopen('https://api.chess.com/pub/player/'+ name)
'''

# 1. Get the list of all GM names
raw_data = urllib.request.urlopen('https://api.chess.com/pub/titled/GM')

data_bytes = raw_data.read()
data_str = data_bytes.decode("utf-8")
data_dict = json.loads(data_str)

list_GM_names = data_dict['players']


# 2. For each GM, get their country URL
list_all_GM_countries_url = []

for name in list_GM_names:
    raw_data = urllib.request.urlopen('https://api.chess.com/pub/player/'+ name)
    data_bytes = raw_data.read()
    data_str = data_bytes.decode("utf-8")
    data_dict = json.loads(data_str)
    country_URL = data_dict['country']
    list_all_GM_countries_url.append(country_URL)


# 3. Count the occurrences of each country URL
counter_all_GM_countries_url = Counter(list_all_GM_countries_url)
print(counter_all_GM_countries_url)

#4. Transform the counter dict to a casual dict with the names of each counter (not url) and the amount of times that they appear
counter_all_GM_countries_name = {}
for url in counter_all_GM_countries_url.keys():
    raw_data = urllib.request.urlopen(url)
    data_bytes = raw_data.read()
    data_str = data_bytes.decode("utf-8")
    data_dict = json.loads(data_str)
    country_name = data_dict['name']
    counter_all_GM_countries_name[country_name] = counter_all_GM_countries_url[url]
print(counter_all_GM_countries_name)


# print(data_dict["chess_rapid"]["last"]["rating"])
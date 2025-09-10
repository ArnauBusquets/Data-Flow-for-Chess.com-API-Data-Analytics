import urllib.request
import json
from collections import Counter


name = 'Busi_jr'
# raw_data = urllib.request.urlopen('https://api.chess.com/pub/player/'+ name)
raw_data = urllib.request.urlopen('https://api.chess.com/pub/titled/GM')

data_bytes = raw_data.read()
data_str = data_bytes.decode("utf-8")
data_dict = json.loads(data_str)

list_GM_names = data_dict['players']

# print(list_GM_names) 

list_all_GM_countries_url = []

for i in range(0,3):
    raw_data = urllib.request.urlopen('https://api.chess.com/pub/player/'+ list_GM_names[i])
    data_bytes = raw_data.read()
    data_str = data_bytes.decode("utf-8")
    data_dict = json.loads(data_str)
    country_URL = data_dict['country']
    list_all_GM_countries_url.append(country_URL)

counter_all_GM_countries_url = Counter(list_all_GM_countries_url)
print(counter_all_GM_countries_url)

#Transform the counter dict to a casual dict with the names of each counter (not url) and the amount of times that they appear

# list_all_GM_countries_name = []
# for url in 
# print(Counter(list_all_GM_countries))


# print(data_dict["chess_rapid"]["last"]["rating"])  

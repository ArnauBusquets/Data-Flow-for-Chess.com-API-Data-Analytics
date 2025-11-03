import urllib.request
import json
from collections import Counter

list_months = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
for i in list_months:
    raw_data = urllib.request.urlopen('https://api.chess.com/pub/player/Hikaru/games/2025/' + i)

    data_bytes = raw_data.read()
    data_str = data_bytes.decode("utf-8")
    data_dict = json.loads(data_str)

    total_games = len(data_dict['games'])

    total_acc = 0
    for game in data_dict['games']:
        try: 
            if game['white']['username'].lower() == 'Hikaru'.lower():
                print("Busi_Jr is playing as White")
                player = 'white'
            else:
                print("Busi_Jr is playing as Black")
                player = 'black'
            print(game['accuracies'])
            total_acc += game['accuracies'][player.lower()]

            for key, value in game.items():
                print(f"{key}: {value}")
        except:
            print("Error")

    print(f"Total accuracy in May 2025: {total_acc}")
    print(f"Total games in May 2025: {total_games}")
    print(f"Average accuracy in May 2025: {total_acc/total_games}")
        # print(game['accuracies'])
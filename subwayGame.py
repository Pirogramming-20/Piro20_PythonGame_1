import json
import random

def subwayGame_start(line_num_dict, user, friends):
    
    print("🚇 지하철~지하철~지하철~지하철 🚇 🤔 몇호선~몇호선~몇호선~몇호선~ 🤔")
    random_line_num = random.choice(list(line_num_dict.keys()))
    print(f"[{random_line_num}]")

    used_stations = set()

    players = initialize_players(user, friends)

    while True:
        for player in players:

            if player['name'] == user:
                selected_station = input(f"{player['name']}, 어떤 역을 선택하시겠습니까?🤔 ")
            else:
                selected_station = random.choice(line_num_dict[random_line_num])
                print(f"{player['name']}, {selected_station}을(를) 선택했습니다.")


            if selected_station in used_stations:
                print("어❓❓ 🤣 바보샷ㅋ 🍻 🤣 바보샷ㅋ 🍻")
                return

            if selected_station not in line_num_dict[random_line_num]:
                print(f"🤪 아 누가 술을 마셔 🤪 {player['name']}(이)가 술을마셔~ 🍻 원~ 샷~ ☠️")
                return

            else :
                print("통과~")
            used_stations.add(selected_station)
            player['current_station'] = selected_station
            
            if not used_stations:
                print("모든 역을 다 선택하셨습니다. 게임 종료!")
                return

def initialize_players(user, friends):
    player_names = [user] + friends
    players = []
    for i, player_name in enumerate(player_names, start=1):
        player = {
            "id": i,
            "name": player_name,
            "current_station": None,
        }
        players.append(player)

    return players
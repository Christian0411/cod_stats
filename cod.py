from player import Player
import time
import os 
import sys

players_list = []

for arg in sys.argv[1:]:
    players_list.append(Player.from_battletag(arg))

while True:
    os.system("clear")
    
    for player in players_list:
        print(player)
    
    time.sleep(300)

    for player in players_list:
        player.refresh_stats()    


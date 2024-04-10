#############################################################
#modual: map
#############################################################
"""This modual has made a map for the player to they can see they 
can see the game layout.
"""
#################################################################
#Inported
from tabulate import tabulate
##################################################################
map_file = 'map.txt'
game_map = [
        ["start_tile", "side_door", "side_door", "side_door" ], 
        ["celler_entrance", "wear_house", "wear_house", "office_room" ],
        ["celler_entrance", "celler", "celler", "celler"]
]

def export_map():
    try:
        with open(map_file, 'w') as file:
            file.write(tabulate(game_map, tablefmt = "mixed_grid"))
    except:
        print("somthing went wrong")
    else:
        print("you have a map of the wear house")
        

def read_map():
    try:
        with open(map_file, 'r') as file:
            print(file.read())
    except:
        print("somthing went wrong")


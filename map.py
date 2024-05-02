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



map_tiles = {
            "start_tile": {"discription":["""You are at the docks were the
enemys wear house is. You have been informed that no one should be inside right now."""]
,
            "look around": ["""In very direction you look you see shiping crates. 
There are not cars or people in sight. """],
                          },
            "side_door" : {"discription" :[""" \n you are walking along the side of the
gray wear house. Their is a door with a dirty window."""],        

            },

            "celler_entrance" : {
            "discription" :[""" as you go down the frount of the building you come
across a meadel trap door. This must be one of the entrances to the celler. """],
            "look around" : ["you found a rock but you can't pick it up"] ,
            },

            "wear_house" : {
        "discription" :["""\n You enter into the dark wear house. You look around to see
many large wooden crates. You see a door at the end of the line of crates. 

        """],
            "look around" : ["""you look at the wooden crates seeing some are open. The
crates are filled to the brim with jelly beans """],
            "check lader" : ["""you walk over to the lader seeing that it must lead 
            to an inportant room"""]         
            },

            "celler" : {
    "discription" : """\n Its cold and dark, the stone walls make it look like a dungen 
    there is a table in the midel of the room with a lager case on it that says PLANS""",
            "look around" : ["""there is a table in the midel of the room with a lager 
case on it that says PLANS"""]
}
}
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


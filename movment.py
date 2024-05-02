#####################################################################
# Title: movement
# Class: CS 30
# Assignemt: game
# Coder: Eve Olson
# version: 2
#####################################################################
#import objects 
#########################################################
#module: odjects
#########################################################
"""This module contains items that the charactor can pick up and use
along with key and passcode used to get through to other rooms.
"""
#########################################################
""" make action for explor and pick up"""
#list of object if the palyer explors the room and then thye can select 
odjects = { 
            "paper" : {"discription" : "There is a code on the paper 7863",
                       "location": [1, 0],
                       "code" : "7863",
                      },
     
          "celler door" : {"discription" : """ The door is locked... but it has a
          cobination lock""",
                           "location" : [0, 1] and [0, 2],
                           "requierment" : ["code"]
                             },
 
          "case" : {"discription" :""" on the table there is a case has PLANS writen on 
it. """,
                   " location" : [1, 2] and [2, 2] and [3, 2],
                   },
                   
                    
                    }
colx = 0
rowy = 0
map_highty_max = 2
map_highty_min = 0
map_width_max = 3
map_width_min = 0

options = ["yes", "no"]
movment = ["u", "d", "b", "f", "quit"]
charactor_position = {}
map_tiles = {
    "start_tile": {"discription" :["""You are at the docks were the
enemys wear house is. You have been informed that no one should be inside right now."""]
,
    "look around": ["""In very direction you look you see shiping crates. 
There are not cars or people in sight. """],
                  },
    "side_door" : {"discription" :["""  you are walking along the side of the
gray wear house. Their is a door with a dirty window, and a note on the ground"""],
    },

    "celler_entrance" : {
    "discription" :[""" as you go down the frount of the building you come
across a metal trap door. This must be one of the entrances to the celler. """],
    "look around" : ["you found a rock but you can't pick it up"] ,
    },

    "wear_house" : {
"discription" :[""" You enter into the dark wear house. You look around to see
many large wooden crates you look at the wooden crates seeing some are open.  
"""],
    "look around" : ["""You see a door at the end of the line of crates."""],        
    },

    "celler" : {
"discription" : """ Its cold and dark, the stone walls make it look like a dungen 
there is a table in the midel of the room with a lager case on it that says PLANS""",
    "look around" : ["""there is a table in the midel of the room with a lager 
case on it that says PLANS"""]
}
}
game_map = [
        ["start_tile", "side_door", "side_door", "side_door" ], 
        ["celler_entrance", "wear_house", "wear_house", "office_room" ],
        ["celler_entrance", "celler", "celler", "celler"]
]
inventory = []


def access_inventory():
    print(inventory)
    #for inv in inventory:
        #print(f"*{inv}")
        

"""movement funtions to move the player around"""
def move_forward():
    global colx
    global rowy 
    colx = colx + 1 
    #print(colx)
    #print(rowy)


def move_backward():
    global colx
    global rowy 
    colx = colx - 1 
    #print(colx)
    #print(rowy)


def move_up():
    global colx
    global rowy 
    rowy = rowy - 1
    #print(colx)
    #print(rowy)


def move_down():
    global colx
    global rowy
    rowy = rowy + 1 
    #print(colx)
    #print(rowy)


def room_position():
    """prints the discription of the room the player is in"""
    global charactor_position
    charactor_position.update(map_tiles[game_map[rowy][colx]])
    #print(colx)
    #print(rowy)
    print(charactor_position["discription"])


def look_around():
    """The player is given more info on the area they are in"""
    global charactor_position
    print(charactor_position["look around"])


def inspect_item(): 
    global charactor_position, rowy, colx, objects, inventory, map_tiles, game_map
    object_found = False
    for object in odjects:
        object_rowy = odjects[object]['location'][0]
        object_colx =  odjects[object]['location'][1]
        if object_rowy == rowy and object_colx == colx:
            print(odjects[object]['discription'])
            for op in options:    
                print((f"*{op}"))
            ask = input ("do you want to put this in your inventory:")
            if ask == "yes":
                inventory.append(object)
                print(" your inventory:")
                print(inventory)
                object_found = True
            elif ask == "no":
                pass   
        if object_found:
            for item in inventory:
                if item == "celler door":
                    # add celler door function
                    print("")
                elif item == "paper":
                    #add paper function
                    #actions()
                    print("")
                elif item == "case":
                    print("YAY!!!You found the case.")
                    # add 
                    
def actions():
    """print the players movement options and prevents the player form moving off the 
    map."""
    global colx
    global rowy 
    direction_choice = True
    while direction_choice:
        try:
            print("""\n move options:""")
            for moves in movment:
                print(f"*{moves}")
            move = input(""" choice:""")
                #direction_choice = True
            if move == "quit":
                print("Thank you for playing")
                exit()
            else:
                if move.lower() == "f":
                    move_forward()
                    if colx > map_width_max:
                        print("End of the map. Please chose new direction")
                        colx = colx - 1
                        direction_choice = True
                    else:
                        direction_choice = False
                elif move.lower() == "b": 
                    move_backward()
                    if colx < map_width_min:
                        print("End of the map. Please chose new direction")
                        colx = 0
                        direction_choice = True
                    else:
                        direction_choice = False
                elif move.lower() == "d":
                    move_down()
                    if rowy > map_highty_max :
                        print("End of the map. Please chose new direction")
                        rowy = 0
                        direction_choice = True
                    else:
                        direction_choice = False
                elif move.lower() == "u":
                    move_up()
                    if rowy < map_highty_min :
                        print("End of the map. Please chose new direction")
                        rowy = 0
                        direction_choice = True
                    else:
                        direction_choice = False    
                else:
                    print("Invalid input. That is not a direction.")
                    direction_choice = True
        except:
            print("invalid input")


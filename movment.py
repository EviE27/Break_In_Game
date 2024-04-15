#####################################################################
# Title: movement
# Class: CS 30
# Assignemt: game
# Coder: Eve Olson
# version: 2
#####################################################################

colx = 0
rowy = 0
map_highty_max = 2
map_highty_min = 0
map_width_max = 3
map_width_min = 0

movment = ["u", "d", "b", "f", "quit"]
charactor_position = {}
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
    "discription" :["""\n as you go down the frount of the building you come
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
game_map = [
        ["start_tile", "side_door", "side_door", "side_door" ], 
        ["celler_entrance", "wear_house", "wear_house", "office_room" ],
        ["celler_entrance", "celler", "celler", "celler"]
]

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
    print(colx)
    print(rowy)
    print(charactor_position["discription"])


def look_around():
    """The player is given more info on the area they are in"""
    global charactor_position
    print(charactor_position["look around"])


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


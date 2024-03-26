import map

my_map = map.game_map

game_map = [
        ["start_tile", "side_door", "side_door", "side_door" ], 
        ["celler_entrance", "wear_house", "wear_house", "office_room" ],
        ["celler_entrance", "celler", "celler", "celler"]
]

#def movement():
   



map_tiles = {
            "start_tile": {"discription":["""You are at the docks were the enemys 
            wear house is. You have been informed that no one should be inside right now.
             """],
            "look around": ["""In very direction you look you see shiping crates. 
There are not cars or people in sight. """],
                          },
            "side_door" : {"discription" :[""" \n you are walking along the side of the
gray wear house. Their is a door with a dirty window."""],
            "look around" : ["You just see some birds pecking at the groud"],  
            "look through window" :["""you try to look throught the window but it is 
too dirty for you to see anything, but the door appers to be unlocked"""],             
            "items" :["door padlock", "paper" ],
            "paper" :"door padlock code 6879"
                           
            },

            "celler_entrance" : {
            "discription" :["""\n as you go down the frount of the building you come across
a meadel trap door. This must be one of the entrances to the celler. """],
            "look around" : ["you found a rock but you can't pick it up"] ,
            },

            "wear_house" : {
        "discription" :["""\n You enter into the dark wear house. You look around to see
many larger wooden crates. You see a door at the end of the line of crates. 
This is the room that you need to go to retive the plans. To the side 'up' ofyou you
see the side door. To the other side 'down' of you there is a lader
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




charactor_position = {}
colx = 0
rowy = 0
map_highty_max = 2
map_highty_min = 0
map_width_max = 3
map_width_min = 0
        


def move_forward():
    global colx
    global rowy 
    colx = colx + 1 
    #print(colx)
   # print(rowy)


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


def actions():
    global colx
    global rowy 
    direction_choice = True
    while direction_choice:
        try:
            direction_choice = False
            move = input("""\n move options 'U', 'D', 'B', 'F' or 'q' to quit:""") 
            if move == "q":
                main()
                direction_choice = True
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
            print("invalid input;")


def room_position():
     global charactor_position
     charactor_position.update(map_tiles[game_map[rowy][colx]])
     print(charactor_position["discription"])
        
        

def look_around():
     global charactor_position
     print(charactor_position["look around"])


def tile_screen():
    print("""Hello player. You have been recruted to break in to the enemys base to
steal their plans for how they want to take over the city. your movement options 'U' to
go up, 'D'to go down, 'B' to go backwards, or 'F' to go forwards.
Type the letter then hit enter to move. If you want to quit type 'q' 
    """)
    chocie = True
    while chocie:
        continue_ = input(" Do you want to 'contiune' type 'c' or  'q' for quit:")
        if continue_ == 'c':
            main()
            chocie = False
        elif continue_ == 'q':
            print("game end, thanks for playing")
            exit()
        else:
            print("Invalid input, please input c or q")
    
def main():
    play = True
    while play:
        room_move = input("""\n if you want to look around in this area type 'look' 
        to move type 'move' to the next: """)
        room_position()
        if  room_move == 'move':
            actions()
            room_position()
        elif room_move == 'look':
            look_around()
        

tile_screen()
room_position()
main()
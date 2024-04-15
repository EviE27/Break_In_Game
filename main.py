from movment import rowy, colx, actions
import map

game_map = [
        ["start_tile", "side_door", "side_door", "side_door" ], 
        ["celler_entrance", "wear_house", "wear_house", "office_room" ],
        ["celler_entrance", "celler", "celler", "celler"]
]

map_file = 'map.txt'
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
charactor_position = {}


def room_position():
    """prints the discription of the room the player is in"""
    global charactor_position
    charactor_position.update(map_tiles[game_map[rowy][colx]])
    print(charactor_position["discription"])
        
        
def look_around():
    """The player is given more info on the area they are in"""
    global charactor_position
    print(charactor_position["look around"])


def tile_screen():
    """begining screen to explain to the player how to play the game"""
    print("""Hello player, You have been recruted to break in to the enemys
base to steal their plans for how they want to take over the city. Your 
movement options 'U' to go up, 'D' to go down, 'B' to go backwards, or 'F'
to go forwards. When you are giveing an option list Type the letter or what appers the 
list then hit enter to do the action. 
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
    """the game is run in this function"""
    play = True
    while play:
        room_move = input("""\n if you want to look around in this area type 'look'to 
move type 'move' to the next: """)
        room_position()
        if  room_move == 'move':
            actions()
            room_position()
        elif room_move == 'look':
            look_around()
#chang so prints in list and gives movement options with out having to chose move first

        
map.export_map() 
map.read_map()
tile_screen()
main()

#####################################################################
# Title: Break in game
# Class: CS 30
# Assignemt: game
# Coder: Eve Olson
# version: 3
#####################################################################

import map
import movment
import objects
#from map import export_map, read_map
#from movment import actions, room_position, look_around, inspect_item


game_map = [
        ["start_tile", "side_door", "side_door", "side_door" ], 
        ["celler_entrance", "wear_house", "wear_house", "office_room" ],
        ["celler_entrance", "celler", "celler", "celler"]
]

move_opt = [ "look", "move", "map"]
map_file = 'map.txt'
charactor_position = {}


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
        try:
            for opt in move_opt:
                print(f"*{opt}")
            room_move = input("""choice: """)
            if  room_move == 'move': 
                movment.actions()
                movment.room_position()
            elif room_move == 'look':
                movment.look_around() 
            elif room_move == 'map':
                map.export_map() 
                map.read_map() 
                
        except:
            print("invalid input, plase select option")
#chang so prints in list and gives movement options with out having to chose move first

        

#tile_screen()
#main()
movment.inspect_item()
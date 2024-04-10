from tabulate import tabulate
import map
import movment

from movment import rowy
from movment import colx
from movment import actions

map_file = 'map.txt'

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
    print("""Hello player. You have been recruted to break in to the enemys base to
steal their plans for how they want to take over the city. Your movement options 'U' to
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

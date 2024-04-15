


colx = 0
rowy = 0
map_highty_max = 2
map_highty_min = 0
map_width_max = 3
map_width_min = 0

movment = ["u", "d", "b", "f", "quit"]

"""movement funtions to move the player around"""
def move_forward():
    global colx
    global rowy 
    colx = colx + 1 
    print(colx)
    print(rowy)


def move_backward():
    global colx
    global rowy 
    colx = colx - 1 
    print(colx)
    print(rowy)


def move_up():
    global colx
    global rowy 
    rowy = rowy - 1
    print(colx)
    print(rowy)


def move_down():
    global colx
    global rowy
    rowy = rowy + 1 
    print(colx)
    print(rowy)


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


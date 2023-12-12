#https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json
def turn_right():
    turn_left()
    turn_left()
    turn_left()


def move_along_right():
    if right_is_clear() == True:
        turn_right()
        move()
    elif front_is_clear() == True:
        move()
    else:
        turn_left()


while at_goal() != True:
    move_along_right()
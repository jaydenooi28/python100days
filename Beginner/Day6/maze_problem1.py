
def turn_right():
    turn_left()
    turn_left()
    turn_left()


def move_along_right():
    if right_is_clear() == True and front_is_clear() == True:
        move()
    elif right_is_clear() == True:
        turn_right()
        move()
    elif front_is_clear() == True:
        move()
    else:
        turn_left()


while at_goal() != True:
    move_along_right()
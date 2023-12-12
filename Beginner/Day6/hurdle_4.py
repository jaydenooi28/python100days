#https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%204&url=worlds%2Ftutorial_en%2Fhurdle4.json
#add function to turn right
def turn_right():
    turn_left()
    turn_left()
    turn_left()

#add function to jump over the hurdle
def jump():
    turn_left()
    #robot to keep move up
    while wall_on_right() == True:
        move()
    turn_right()
    move()
    turn_right()
    move()
    #robot keep move down
    while wall_on_right() == True:
        if front_is_clear() == True:
            move()
        #break the loop when robot reach the lowest
        else:
            turn_left()
            break

#move until robot finds the goal
while at_goal() != True:
    if front_is_clear() == True:
        move()
    else:
        jump()
print('Welcome to Treasure Island.\nYour mission is to find the treasure')
print('Welcome to the first junction')
ans1 = (input ('Do you want to go left or right? ')).lower()
if ans1 == 'left':
    print ("Congraz, you have chosen the correct path.\n Now you have arrived a river")
    ans2 = (input ("Do you want swim over or wait? ")).lower()
    if ans2 == 'wait':
        print ("While you were waiting, the dangerous trout swim away....\n So now its safe to swim over")
        print ("Now you have arrived at a place with 3 doors with different colours. \n Red   Blue   Yellow")
        ans3 = (input ('Which colour would you like to choose? ')).lower()
        if ans3 == 'red':
            print ('You chosen the Red door\nA mechanism has avtivated the flamethrower \n You got burned by fire\n Game Over')
        elif ans3 == 'blue':
            print ('You chosen the Blue door\n And you saw this room is full of foul beast....\n You are now their dinner\n Game Over')
        elif ans3 == 'yellow':
            print ('You chosen the Yellow door\n Congratulation you have won the game\n You are rewarded with a ticket to Coldplay concert')
        else: 
            print ('You did not take this seriously\n A thunderstrike struck you and you died\n Game Over')
    else:
        print ('Wrong answer\n A group a trout has appear and they attacked you\n Game Over')
else:
    print ('Unfortunately you have chosen the wrong answer\n You have fallen into a hole\n Game Over')

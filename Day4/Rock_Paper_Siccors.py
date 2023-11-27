human = int(input("What do you choose? Type 0 for Rock, 1 for Papaer or 2 for Scissors. "))
choice = ["Rock","Paper","Scissors"]

import random
computer = random.randint(0,2)

#0 = rock
#1 = Paper
#2 = Scissors
h = f"You chose {choice[human]}"
c = f"You chose {choice[computer]}"

if human == 0:
    print (h)
    # print (rock_art)
    if computer == 0:
        print(c)
        # print (rock_art)
        print("Draw")
    elif computer == 1:
        print (c)
        # print (paper_art)
        print ("You lose")
    else:
        print (c)
        # print (scissors_art)
        print ("You win!")
#0 = rock
#1 = Paper
#2 = Scissors
elif human == 1:
    print (h)
    if computer == 0:
        print(c)
        # print (rock_art)
        print ("You win!")
    elif computer == 1:
        print (c)
        # print (paper_art)
        print ("Draw")
    else:
        print (c)
        # print (scissors_art)
        print ("You lose")

#0 = rock
#1 = Paper
#2 = Scissors
elif human == 2:
    print (h)
    if computer == 0:
        print(c)
        # print (rock_art)
        print ("You lose")
    elif computer == 1:
        print (c)
        # print (paper_art)
        print ("You win")
    else:
        print (c)
        # print (scissors_art)
        print ("Draw")
else:
    print("Wrong Number, you lose")
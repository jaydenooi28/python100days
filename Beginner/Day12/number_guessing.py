from art import logo
import random
import os
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

while True:
    print(logo)
    print ("Welcome to the Number Guessing Game!")
    print("Im thinking of a number between 1 and 100")
    num = random.randint(1,100)
    
    while True:
        # reveal answer for testing purpose
        print(f"Answer is {num}")
        choice = input("Choose a difficulty.\nType 'easy' or 'hard': ")
        if choice.lower() not in ["easy","hard"]:
            print("Please input correctly\n")
            continue
        else:
            life = 10 if choice.lower() == "easy" else 5
            break
    
    while life > 0:
        while True:
            try:
                guess = int(input("Make a guess: "))
                break
            except ValueError:
                print("Invalid input. Please enter an integer.")
        
        if num == guess:
            print(f"Wow... You've guess correctly. The answer is {num}")
            break
        else:
            if life == 1:
                print("You have used up your life points\nGame Over")
                break
            elif guess > num:
                life -= 1
                print("Too high.\nGuess Again")
                print(f"You have {life} attempts left.")
            elif guess < num:
                life -= 1
                print("Too low.\nGuess Again")
                print(f"You have {life} attempts left.")     

    next_game = input("Do you want to continue playing? [y/n] ")
    if next_game.lower() not in ["y", "n"]:
        print("Please enter 'y' or 'n'.")
        continue
    else:
        if next_game.lower() == "y":
            game_on = False
        else:
            play_game = False
            break
        clear_screen()
    


            

            
    





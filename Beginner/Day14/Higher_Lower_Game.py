from art import *
from game_data import data
import random
import os
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def show_info(who):
    name = who['name']
    desc = who['description']
    home = who['country']
    print(f"{name}, a {desc}, from {home}")

def compare_followers(team_A, team_B):
    a = int(team_A['follower_count'])
    b = int(team_B['follower_count'])

    if a > b:
        winner = "a"
    else:
        winner = "b"

    return winner

while True:
    # Reset the game_over state to False at the beginning of each game
    game_over = False
    score = 0
    while not game_over:
        
        team_A = random.choice(data)
        data.remove(team_A)

        team_B = random.choice(data)
        data.remove(team_B)

        # show user the choices
        print("======================================================================================================================================")
        print(highlow)
        show_info(team_A)
        print(vs)
        show_info(team_B)
        print("Testing purpose. ans shown below")
        print(team_A['follower_count'])
        print(team_B['follower_count'])

        # loop until user input correctly
        while True:
            if score > 0:
                print(f"Current score: {score}")
            choice = input("Who has more followers? Type 'A' or 'B': ").lower()

            if choice not in ['a', 'b']:
                print("Please input correctly")
                continue
            else:
                break

        # compare answer to user input
        answer = compare_followers(team_A, team_B)
        if answer == choice:
            score += 1
            print(f"You're right! Current score: {score}")
            clear_screen()
        else:
            print(f"Wrong answer\nGame over")
            game_over = True
    next_game = input("Do you want to continue playing? [y/n] ")
    if next_game.lower() not in ["y", "n"]:
        print("Please enter 'y' or 'n'.")
        continue
    else:
        if next_game.lower() == "y":
            game_over = False
        else:
            game_over = True
            break
        clear_screen()
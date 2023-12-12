import random
from hangman_words import *
from hangman_art import *
from replit import clear

print(logo)
chosen_word = random.choice(word_list)
word_length = len(chosen_word)
ans = []
for i in chosen_word:
    ans += "_"
lives = 6
game_over = False
while not game_over:
    print(line)
    # testing purpose
    print(f"Answer is {chosen_word}")
    guess = (input("Please guess an word = ")).lower()
    clear()

    # check the guess word
    if guess in ans:
        print("You already guess this character")
    elif len(guess) > 1:
        print("Bro please dont troll\nPlease enter only one character")

    for ind in range(word_length):
        if chosen_word[ind] == guess:
            ans[ind] = guess

    if guess not in chosen_word:
        lives -= 1
        print(f"You've entered {guess}\nWrong answer, live -1")
        print(f"You have {lives} lives left!!\n")

        if lives == 0:
            print(stages[lives])
            game_over = True
            print(f"You have {lives} lives left!!\n")
            print("BOOOOOOOO\n You lost!!!")
    else:
        print(f"You enter the correct answer: {guess}")
        print(f"You have {lives} lives left!!\n")
    print(ans)
    print(stages[lives])

    if "_" not in ans:
        game_over = True
        print(f"{' '.join(ans)}")
        print("Congrats, you won the game!!!")
        print(f"Your have {lives} lives left!!\n")

import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
word_list = ["apple", "banana", "orange", "grape"]
chosen_word = random.choice(word_list)
word_length = len(chosen_word)
ans = []
for i in chosen_word:
    ans += "_"
lives = 6
game_over = False
while not game_over:
    print(f"Answer is {chosen_word}")
    guess = (input("Please guess an word = ")).lower()

    # check the guess word
    for ind in range(word_length):
        if chosen_word[ind] == guess:
            ans[ind] = guess
            print(stages[lives])
    if guess not in chosen_word:
        lives -= 1
        print(stages[lives])
        if lives == 0:
            print(stages[lives])
            game_over = True
            print("BOOOOOOOO\n You lost!!!")
    print(ans)
    print(f"Your have {lives} lives left!!\n")

    if "_" not in ans:
        game_over = True
        print(f"{' '.join(ans)}")
        print("Congrats, you won the game!!!")
        print(f"Your have {lives} lives left!!\n")

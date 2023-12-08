from art import *
import  random
import os
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def pick_random_card(deck):
    # Randomly pick a card
    random_suit = random.choice(list(deck.keys()))
    random_rank = random.choice(deck[random_suit])

    # Remove the picked card from the deck
    deck[random_suit].remove(random_rank)

    # Return the picked card
    return random_rank, random_suit

# calculate score
# ('6', 'Clubs')
# ('7', 'Diamonds')
def calculate_score(card1, card2,on_hand):
    score = 0
    royal = ["Jack", "Queen", "King"]
    if isinstance(card1,tuple):
        rank1 = card1[0]
    else:
        rank1 = card1   
    rank2 = card2[0]

    if isinstance(rank1, int):
        score += rank1
    elif rank1 in royal:
        score += 10
    elif rank1 == "Ace":
        if on_hand <= 2:
            score += 11
        else:
            score += 1
    else:
        score += int(rank1)

    if isinstance(rank2, int):
        score += rank2
    elif rank2 in royal:
        score += 10
    elif rank2 == "Ace":
        if on_hand <= 2:
            score += 11
        else:
            score += 1
    else:
        score += int(rank2)

    return score

def convert_to_string(card):
    return f"{card[0]} of {card[1]}"

play_game = True
while play_game:
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', "Jack", "Queen", "King", "Ace"]

    # create a deck
    deck = {suit: ranks.copy() for suit in suits}
    p_hand_str = ""
    game_on = True
    while game_on:
        print(logo)
        play = input("Do you want to play a game of Blackjack? [y/n]: ")
        if play.lower() not in ["y", "n"]:
            print("Please enter 'y' or 'n'.")
            continue
        elif play.lower() == "y":
            print("Let's play Blackjack!")
        else:
            print("Maybe next time.")
            play_game = False
            break
        # random pick card and remove from the list
        # Player
        p_card1 = pick_random_card(deck)
        p_card2 = pick_random_card(deck)
        hand = 2
        p_card1_str = f"{p_card1[0]} of {p_card1[1]}"
        p_card2_str = f"{p_card2[0]} of {p_card2[1]}"

        player_score = calculate_score(p_card1,p_card2,hand)

        #  Dealer
        d_card1 = pick_random_card(deck)
        d_card2 = pick_random_card(deck)
        d_hand = 2
        d_card1_str = f"{d_card1[0]} of {d_card1[1]}"
        d_card2_str = f"{d_card2[0]} of {d_card2[1]}"
        dealer_score = calculate_score(d_card1,d_card2,d_hand)
    

        print(f"Player current hand: {p_card1_str}, {p_card2_str}")
        print(f"Player currenct score: {player_score}")
        if player_score == 21:
            continue
        else:
            print(f"Dealer current hand: {d_card1_str}")
        

        draw_card = True
        p_game_over = False
        p_hand_list = [p_card1_str,p_card2_str]
        

        while hand <= 5 and draw_card and not p_game_over and player_score < 21:
            print("===========================================================================================================================")
            draw = input("Do you want to keep drawing? [y/n]: ")
            if draw.lower() not in ["y", "n"]:
                print("Please enter 'y' or 'n'.")
                continue
            elif draw.lower() == "y":
                print("Let's draw another card")
                hand += 1
                p_new_card = pick_random_card(deck)
                p_hand_list.append(convert_to_string(p_new_card))
                player_score = calculate_score(player_score,p_new_card,hand)
                p_hand_str = ', '.join(p_hand_list)
                if hand == 5:
                    p_game_over = True
                    break
                else:
                    print(f"Player current hand: {p_hand_str}")
                    print(f"Player current score: {player_score}")
                if hand > 6:
                    print("You have drawn the maximum number of cards")
                    break

                elif player_score > 21:

                    p_game_over = True
                    break
            else:
                p_hand_str = ', '.join(p_hand_list)
                print(f"Player current hand: {p_hand_str}")
                print(f"Player current score: {player_score}")
                draw_card = False



        
        d_hand_list = [d_card1_str,d_card2_str]
        d_game_over = False

        while dealer_score < 16 and d_hand <=5 and not d_game_over and not p_game_over:
            if dealer_score > 21:
                print(f"Dealer went over 21 bomb")
                d_game_over = True
                break
            d_new_card = pick_random_card(deck)
            d_hand +=1
            d_hand_list.append(convert_to_string(d_new_card))
            dealer_score = calculate_score(dealer_score,d_new_card,d_hand)
            
            
        d_hand_str = ', '.join(d_hand_list)
        print (f"Dealer current hand: {d_hand_str}")
        print (f"Dealer current score: {dealer_score}")

        if player_score > 21:
            print("The player went over 21. Dealer Wins!")
        elif dealer_score > 21:
            print("The dealer went over 21. Player Wins!")
        else:
            if player_score == dealer_score:
                print("The game is a draw!")
            elif player_score > dealer_score:
                print("Player wins!")
            else:
                print("Player loses!")
        print("===========================================================================================================================")
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




                




                


        
        
        






    
    
# card1 =('2', 'Clubs'),('9', 'Clubs')
# card2 = ('9', 'Clubs')

# def cards_to_string(card1, card2):
#     card1_str = f"{card1[0]} of {card1[1]}"
#     card2_str = f"{card2[0]} of {card2[1]}"
    
#     return card1_str, card2_str

# b = cards_to_string(card1, card2)
    

# # b = cards_to_string(x)

# print(b[1])


ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', "10", "10", "10", "11"]
ranks2 = ranks.copy()

# Extend the 'ranks' list with the elements from 'ranks2'
ranks = ranks +ranks2

# Now 'ranks' has been modified in place, and 'b' is None
print(ranks)
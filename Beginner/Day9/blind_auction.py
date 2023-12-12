import os 
def clear():  # Cross-platform clear screen
    os.system('cls' if os.name == 'nt' else 'clear')
from art import logo
print (logo)
bidders = {}
cont = True
while cont:
    name = input("What is you name: ")
    bid_amount = int(input("How much do you want to bid : $"))
    
    def add_new_bidder(name, bid_amount):
        bidders [name] = bid_amount
    def find_highest_bidder(bidders):
        highest_bidder = None
        highest_amount = 0
        for i in bidders:
            if bidders[i] > highest_amount:
                highest_bidder= i
                highest_amount = bidders[i]
        print(f"The winner is {highest_bidder} with the amount of ${highest_amount}.")


    add_new_bidder(name,bid_amount)

  
    while True:
        other_players = input ("Are there any other players [y/n]: ")
        if not (other_players == "y" or other_players == "n"):
            print("bro answer correctly")
        else:
            break
    
    if other_players == "y":
        clear()
    else:
        find_highest_bidder(bidders)
        print (bidders)
        break


            

        

        


        



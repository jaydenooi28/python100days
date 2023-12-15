from menu import *
from collections import namedtuple
import os


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


# Covert the values from MENU dictionary for easier use
def convert_value(drink):
    Order = namedtuple("Order", ["milk", "water", "coffee", "cost"])
    if drink == "latte" or drink == "cappuccino":
        milk = int(MENU[drink]["ingredients"]["milk"])
    else:
        milk = None
    water = int(MENU[drink]["ingredients"]["water"])
    coffee = int(MENU[drink]["ingredients"]["coffee"])
    cost = int(MENU[drink]["cost"])
    return Order(milk, water, coffee, cost)


# to check if resources are enough to make the drink
def check_resource(drink):
    order = convert_value(drink)
    res_water = int(resources["water"])
    res_milk = int(resources["milk"])
    res_coffee = int(resources["coffee"])
    # check milk
    if drink == "latte" or drink == "cappuccino":
        if order.milk > res_milk:
            return "Milk", False
    # check water and coffee
    if order.water > res_water or order.coffee > res_coffee:
        return "Water", False
    elif order.coffee > res_coffee:
        return "Coffee", False
    return None, True


# to check if the payment is enough
def check_payment(drink, pay):
    coffee_price = MENU[drink]["cost"]
    if pay >= coffee_price:
        print("Thanks for your payment")
        if pay > coffee_price:
            change = pay - coffee_price
            print(f"Here's your change ${change}")
        return True
    else:
        print("That's not enough, please pay again")
        return False


# To deduct the resource and add money after payment success
def modify_resource(drink):
    order = convert_value(drink)
    if order.milk is not None:
        resources["milk"] -= order.milk
    resources["water"] -= order.water
    resources["coffee"] -= order.coffee
    resources["money"] += order.cost


def current_resource():
    water = resources["water"]
    milk = resources["milk"]
    coffee = resources["coffee"]
    money = resources["money"]
    print(f"Water: {water}ml\nMilk: {milk}ml\nCoffee: {coffee}g\nMoney: ${money}")


# TODO: 1. Prompt user to choose an option
#          1.Choose drink, 2.check resource, 3.off
#          1. continue to step 2,
#          2. print resource and loop back to prompt user choose again,
#          3. Break the whole loop
# Loop until user doesn't want coffee
yes_coffee = True
while yes_coffee:
    while True:
        answer = (input("Hi, What coffee would you like? (espresso/latte/cappuccino): ")).lower()
        if answer not in ["espresso", "latte", "cappuccino", "report", "off"]:
            print("Please enter correctly")
            continue
        else:
            if answer == "off":
                print("Goodbye...\nHave a nice day")
                yes_coffee = False
                break

            elif answer == "report":
                current_resource()
                continue
            else:

                # TODO: 2. Check if resource is enough to make an order
                #          if yes continue to step 3 else print resource not enough loop back to step 1
                kopi, result = check_resource(answer)
                if result:
                    break
                else:
                    print(f"Sorry, We dont have enough {kopi}")
                    continue
    if yes_coffee == False:
        break

# TODO: 3. Prompt the user to pay and count if they pay enough
#           if enough give back change or continue to step 4, else loop back to prompt to pay again
    while check_resource(answer):
        coffee_price = MENU[answer]["cost"]
        print(f"Please pay ${coffee_price}")
        while True:
            try:
                quarters = int(input("quarters: "))
                dimes = int(input("dimes: "))
                nickles = int(input("nickles: "))
                pennies = int(input("pennies: "))
                break
            except ValueError:
                print("Error: Invalid input. Please enter a valid number.")
        payment =  quarters * 0.25 + dimes * 0.10 + nickles * 0.5 + pennies * 0.01
        # call the function and print result
        # at the same time, assign the return result to enough
        enough = check_payment(answer,payment)
        if enough == False:
            continue
        else:
            break


# TODO: 4. make the coffee and deduct the resource, then present the coffee to the customer
    modify_resource(answer)
    print(f"“Here is your {answer}. Enjoy!")


# TODO 5. does the user want another coffee
    while True:
            another = (input("Would you like another coffee?[y/n] ")).lower()
            if another not in ["y","n"]:
                print("Please answer correctly")
                continue
            else:
                clear_screen()
                if another == "y":
                    break
                else:
                    yes_coffee = False
                    break




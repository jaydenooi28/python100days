from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine



menu = Menu()
coffee_maker  = CoffeeMaker()
money_machine = MoneyMachine()

is_on = True
# TODO: 1. Prompt user by asking “What would you like? (espresso/latte/cappuccino):

while is_on:
    available = menu.get_items()
    choice = input(f"What would you like? ({available}): " ).lower()

    match choice:
        
# TODO: 2. Turn off the Coffee Machine by entering “off” to the prompt.
        case "off":
            print("Good Bye")
            is_on = False
            
# TODO: 3. Print report.
        case "report":
            coffee_maker.report()
            money_machine.report()
        case _:
            drink = menu.find_drink(choice) 
            if drink:
                print(f"The cost of {choice} is ${drink.cost}")
                 # TODO: 4. Check resources sufficient?
                if  coffee_maker.is_resource_sufficient(drink):
                    payment = money_machine.make_payment(drink.cost)
                     # TODO: 7. Process coins.
                     # TODO: 8. Check transaction successful?
                    if payment:
                        # TODO: 9. Make Coffee.
                        coffee_maker.make_coffee(drink)
 

                     

 


             



                 



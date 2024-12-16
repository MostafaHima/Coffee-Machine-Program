from menu import Menu  # Importing the drink menu from the menu module
from coffee_maker import CoffeeMaker  # Importing coffee-making functionality from the coffee_maker module
from money_machine import MoneyMachine  # Importing payment handling functionality from the money_machine module

# Creating instances of the imported classes
items = Menu()  # Represents the drink menu
coffee_maker = CoffeeMaker()  # Represents the coffee maker machine
money = MoneyMachine()  # Represents the payment handling system

work = True  # Variable to control the program's operation

while work:  # Loop continues as long as the program is running
    print(items.get_items())  # Display the available drink options

    user_order = input("Enter your drink: ").strip().lower()  # Prompt user for their choice, clean input, and convert to lowercase

    if user_order == "report":  # If the user requests a report
        coffee_maker.report()  # Show the current resource status of the coffee maker
        money.report()  # Show the current financial status
    elif user_order == "off":  # If the user wants to turn off the program
        work = False  # Exit the loop
    else:
        drink = items.find_drink(user_order)  # Find the drink the user requested

        # Check if there are enough resources to make the drink
        if coffee_maker.is_resource_sufficient(drink):
            # Check if payment is successful
            if money.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)  # Make the coffee









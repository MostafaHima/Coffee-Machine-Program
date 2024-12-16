# Coffee Machine Program

This Python project simulates the operation of a coffee machine, allowing users to order drinks, check available resources, and manage payments. It leverages object-oriented programming by importing predefined classes for managing the menu, coffee-making resources, and money handling.

## Features
- **Menu Management:** Displays a list of available drinks.
- **Resource Management:** Tracks coffee machine resources (water, milk, coffee).
- **Payment Handling:** Processes payments and checks if sufficient funds are provided.
- **Reporting:** Provides detailed reports of resources and money.
- **Power Control:** Allows users to turn off the machine.

## Requirements
To run the program, the following Python modules must be implemented or provided:
- `menu.py`
- `coffee_maker.py`
- `money_machine.py`

These modules should define the following classes:
1. `Menu`: Handles the drink menu and drink selection.
2. `CoffeeMaker`: Manages resources and drink preparation.
3. `MoneyMachine`: Handles payment processing.

## Usage
1. Clone this repository or copy the program files.
2. Ensure the required modules (`menu.py`, `coffee_maker.py`, `money_machine.py`) are in the same directory as the main script.
3. Run the script:
   ```bash
   python main.py
   ```
4. Interact with the program by typing commands:
   - Type the name of a drink to order it.
   - Type `report` to view the current resources and financial status.
   - Type `off` to shut down the coffee machine.

## Example Interaction
```
latte/espresso/cappuccino
Enter your drink: latte
Please insert coins.
How many quarters?: 4
How many dimes?: 0
How many nickels?: 0
How many pennies?: 0
Here is your latte ☕️. Enjoy!
```

## Notes
- Ensure enough resources are available before ordering a drink.
- Payments must match or exceed the drink's cost for the order to process.



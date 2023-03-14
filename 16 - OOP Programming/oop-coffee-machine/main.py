from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# Create objects from classes
money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()
# Create variable for while loop
is_on = True

while is_on:
    options = menu.get_items()
    choice = input(f"What would you like? ({options}): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        # Generate a report from the MoneyMachine and CoffeeMaker to print all resources
        coffee_maker.report()
        money_machine.report()
        print("------------------------------------")
    else:
        # Check if resources are sufficient
        drink = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            # make coffee
            coffee_maker.make_coffee(drink)
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

profit = 0

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

# check resources to make drink
def is_resource_sufficient(order_ingredients):
    """ Takes the drink ingredients dictionary and returns True when order can be made,
    else it returns False. """
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True


# Process coins function
def process_coins():
    """ Returns the total calculated from coins inserted."""
    print("Please insert coins.")
    total = int(input("How many quarters?: ")) * 0.25
    total += int(input("How many dimes?: ")) * 0.10
    total += int(input("How many nickles?: ")) * 0.05
    total += int(input("How many pennies?: ")) * 0.01
    return total


# Check to see if the user entered enough money
## Return statement must be last in function ##
def is_transaction_successful(money_received, drink_cost):
    """ Returns True when payment is accepted, or False if money is insufficient."""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print("----------------------------------------------------")
        print(f"Here is ${change} in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("----------------------------------------------------")
        print("Sorry that's not enough money. Money refunded.")
        return False

# Make coffee
def make_coffee(drink_name, order_ingredients):
    """ Deduct the required ingredients from the resources. """
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print("----------------------------------------------------")
    print(f"Here is your {drink_name} ☕")


is_on = True
while is_on:
    # Prompt user by asking what drink they want to order
    print("----------------------------------------------------")
    print("Get report: enter 'report' |  Turn off: enter 'off'")
    print("----------------------------------------------------")
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    print("----------------------------------------------------")

    # if the user enters 'off', exit the while loop
    if choice == "off":
        print("Coffee machine turned off.")
        is_on = False
    # Print a report if user enters 'report'
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Coffee: ${profit}")
    else:
        drink = MENU[choice]
        # Check drink resources
        if is_resource_sufficient(drink["ingredients"]):
            # Call process_coins function
            payment = process_coins()
            # Call is_transaction_successful function to check transaction and update profit
            if is_transaction_successful(payment, drink["cost"]):
                # Call make_coffee function to make the coffee and update resources
                make_coffee(choice, drink["ingredients"])

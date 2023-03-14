# This program calculates the tip of a bill
print("Welcome to the tip calculator.")
bill = float(input("What was the total bill? $"))
tip = int(input(
    "What percentage tip would you like to give? 10, 12, or 15? "))
num_of_people = int(input("How many people to split the bill? "))

bill_with_tip = tip / 100 * bill + bill

result = round(bill_with_tip / num_of_people, 2)

print(f"Each person should pay: ${result}")

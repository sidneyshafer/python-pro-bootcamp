# Rollercoaster Program
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

total = 0

if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age? "))
    if age < 12:
        total += 5
        print("Child tickets are $5.")
    elif age <= 18:
        total += 7
        print("Youth tickets are $7.")
    else:
        total += 12
        print("Adult tickets are $12.")

    wants_photo = input("Do you want a photo taken? Y or N. ")
    if wants_photo == 'Y':
        # Add $3 to the total cost
        total += 3

    print(f"The total cost is ${total}.")

else:
    print("Sorry, you can't ride the rollercoaster :(")


# CODING EXERCISE - Pizza Order
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")

bill = 0

if size == 'S':
    bill += 15
elif size == 'M':
    bill += 20
elif size == 'L':
    bill += 25
else:
    print('Invalid entry. Please enter S, M, or L.')

if add_pepperoni == 'Y':
    if size == 'S':
        bill += 2
    elif size == 'M' or size == 'L':
        bill += 3

if extra_cheese == 'Y':
    bill += 1

print(f"Your final bill is: ${bill}.")

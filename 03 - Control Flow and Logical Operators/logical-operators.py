# Logical Operators
# A and B
# C or D
# not E

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
    elif age >= 45 and age <= 55:
        total += 0
        print('Midlife crisis tickets are $0')
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

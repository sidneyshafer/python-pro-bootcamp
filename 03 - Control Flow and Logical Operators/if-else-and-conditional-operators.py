# Rollercoaster Program
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age? "))
    if age < 12:
        print("Please pay $5.")
    elif age >= 12 and age < 18:
        print("Please pay $7.")
    else:
        print("Please pay $12.")
else:
    print("Sorry, you can't ride the rollercoaster :(")

# Greater than >, Greater than or equal to =>
# Less than <, Less than or equal to <=
# Equal to ==, Not equal to !=

# CODING EXERCISE
number = int(input("Which number do you want to check? "))

if number % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")

# CODING EXERCISE
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))

bmi = round(weight / height ** 2)

if bmi < 18.5:
    print(f"Your BMI is {bmi}, you are underweight.")
elif bmi < 25:
    print(f"Your BMI is {bmi}, you have a normal weight.")
elif bmi < 30:
    print(f"Your BMI is {bmi}, you are slightly overweight.")
elif bmi < 35:
    print(f"Your BMI is {bmi}, you are obese.")
else:
    print(f"Your BMI is {bmi}, you are clinically obese.")

# CODING EXERCISE
# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

# Write your code below this line 👇

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap year.")
        else:
            print("Not leap year.")
    else:
        print("Leap year.")
else:
    print("Not leap year.")

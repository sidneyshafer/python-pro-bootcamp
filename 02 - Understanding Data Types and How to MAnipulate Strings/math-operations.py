3 + 5
7 - 4
3 * 2
6 / 3  # Prints floating point number
print(6 // 3)  # Prints integer
print(2 ** 7)

# PEMDAS
# Parentheses
# Exponents
# Multiplication
# Division
# Addition
# Subtraction

print(3 * 3 + 3 / 3 - 3)  # (3*3) --> (3/3) --> (9+1) --> (10-3) --> 7.0
print(3 * (3 + 3) / 3 - 3)

# Coding Exercise
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")

bmi = int(weight) / float(height) ** 2
print(int(bmi))

# print(int(8 / 3))

print(round(8 / 3, 2))  # rounds 8 / 3 with 2 decimal places
print(8 // 3)  # floor division

result = 4 / 2
result /= 2
print(result)

score = 0
# User scores a point
# +=, -=, *=, \=
score += 1
print(score)

# F-Strings
score = 0
height = 1.8
isWinning = True
print(
    f"Your score is {score}, your height is {height}, you are winning is {isWinning}")

# CODING EXERCISE
age = input("What is your current age?")
age_as_int = int(age)

years_remaining = 90 - age_as_int
days_remaining = years_remaining * 365
weeks_remaining = years_remaining * 52
months_remaining = years_remaining * 12

print(
    f"You have {days_remaining} days, {weeks_remaining} weeks, and {months_remaining} months left.")

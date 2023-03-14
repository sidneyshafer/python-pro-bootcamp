# len(1234)
num_char = len(input("What is your name?\n"))

# Type checking
print(type(num_char))

# Type conversion
new_num_char = str(num_char)

print("Your name has " + new_num_char + " characters.")

a = str(123)  # float(), int()
type(a)

print(70 + float("100.5"))
print(str(70) + str(100))

# Coding Exercise
two_digit_number = input("Type a two digit number: ")

digit1 = int(two_digit_number[0])
digit2 = int(two_digit_number[1])
print(digit1 + digit2)

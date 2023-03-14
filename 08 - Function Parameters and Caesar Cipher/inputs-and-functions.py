line = '-----------'

# 'name' and 'day' are the parameters, users can pass in an argument
# parameter = name of data
# argument = actual value of data
def greet(name, day="day"):
    print(f"Hello {name}!")
    print(f"How are you on this fine {day}?")
    print("It's a wonderful day!")

greet("Sidney", "Monday")
print(line)

greet("Allie")
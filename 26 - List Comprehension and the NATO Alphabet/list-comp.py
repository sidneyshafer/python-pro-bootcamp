# LIST COMPREHENSION

# Is this...
numbers = [1, 2, 3]
# new_list = []
# for n in numbers:
#     add_1 = n + 1
#     new_list.append(add_1)

# But can be written as...
# new_list = [new_item for item in list]
# SUCH AS...
new_list = [n + 1 for n in numbers]

# EXAMPLE
my_name = "Sidney"
letters_list = [letter for letter in my_name]

# EXAMPLE
range_list = [n * 2 for n in range(1, 5)]

# CONDITIONAL LIST COMPREHENSION
# new_list = [new_item for item in list if test]
names = ["Sidney", "Lisa", "Allie", "Brent"]
new_names = [name for name in names if len(name) < 6]
uppercase_names = [name.upper() for name in names if len(name) > 5]

# {Key: Value}

programming_dict = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again.",
}
print(programming_dict)

# Getting items from a dictionary
print(programming_dict["Bug"])

# Adding new items
programming_dict["Loop"] = "The action of doing something over and over again."
print(programming_dict)

# Start with empty dictionary
empty_dict = {}

# Wipe an existing dictionary
# programming_dict = {}
# print(programming_dict)

# Edit an item
programming_dict["Bug"] = "A moth in your computer."
print(programming_dict)

# Loop through a dictionary
for key in programming_dict:
    print(key)

for key in programming_dict:
    print(key)
    print(programming_dict[key]) # to print value
# Catch Exception keywords :
# try: a block of code that might cause an exception
# except: the block of code you want to execute if there was an exception
# else: a block of code you want to execute if there were no exceptions
# finally: a block of code that executes no matter what happens
# raise: allows us to raise our own exceptions

# FileNotFoundError
try:
    file = open("a_file.txt")
    a_list = [1, 2, 3, 4]
    a_num = a_list[2]
except FileNotFoundError:
    file = open("a_file.txt", "w")
    file.write("something")
except IndexError as error_message:
    print(error_message)
    print("Index does not exist.")
else:
    content = file.read()
    print(content)
finally:
    file.close()
    print("End of try catch statement. File was closed")
    # raise TypeError("This is an error message.")

height = float(input("Height: "))
weight = int(input("Weight: "))

if height > 3:
    raise ValueError("Height should not be over 3 meters.")

bmi = weight / height ** 2
print(bmi)

# KeyError
# a_dictionary = {"key": "value"}
# value = a_dictionary["none_existent_key"]

# IndexError
# fruits = ["Apple", "Banana", "Orange"]
# fruit = fruits[3]

# TypeError
# text = "abc"
# print(text + 5)

# READING A FILE #
# ---------------#
# Open file
# file = open("my_file.txt") --> one way of opening file

# Another (better) way of opening files:
with open("my_file.txt") as file:
    # Read file
    contents = file.read()
    # Print content of file
    print(contents)

# Close file --> do not have to close file if using 'with _____ as ___' method
# file.close()

# WRITING TO A FILE #
# ------------------#
# With "w" mode, all previous text in file is deleted and the new text is added
# ----> if you open a file in "w" mode and the file does not exist, a file will be created with the given name
# With "a" mode, text is appended to the end of a file, and all previous text remains
with open("my_file.txt", mode="a") as file:
    file.write("\nNew text.")

with open("new_file.txt", mode="w") as file:
    file.write("Hello.\nThis is a new text file.")

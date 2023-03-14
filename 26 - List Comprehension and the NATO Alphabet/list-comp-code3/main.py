with open("file1.txt") as file_1:
    file_1_data = file_1.readlines()

with open("file2.txt") as file_2:
    file_2_data = file_2.readlines()

result = [int(num) for num in file_1_data if num in file_2_data]

print(result)

student_dict = {
    "student": ["Sidney", "James", "Lily"],
    "score": [56, 78, 91]
}

# Looping through dictionaries
for (key, value) in student_dict.items():
    print(value)


import pandas

student_data_frame = pandas.DataFrame(student_dict)
print(student_data_frame)

# Looping through a DataFrame
# for (key, value) in student_data_frame.items():
#     print(value)

# Loop through rows of data frame
for (index, row) in student_data_frame.iterrows():
    # print(index)
    # print(row.student)
    # print(row.score)
    if row.student == "Sidney":
        print(row.score)

# DICTIONARY COMPREHENSION

# Create a new dictionary from a list
# new_dict = {new_key:new_value for item in list}

# Create a new dictionary from an existing dictionary
# new_dict = {new_key:new_value for (key,value) in dict.items()}

# Conditional Dictionary Comprehension
# new_dict = {new_key:new_value for (key,value) in dict.items() if test}

import random

names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]

student_scores = {student: random.randint(1, 100) for student in names}
print(student_scores)

passed_students = {student: score for (student, score) in student_scores.items() if score >= 60}
print(passed_students)

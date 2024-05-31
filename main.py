# ----------------------------------------------------------
# Dictionary Comprehension
#For Loop
numbers = [1, 2, 3]
new_list = []
for n in numbers:
    add_1 = n + 1
    new_list.append(add_1)

#List Comprehension
new_list = [n + 1 for n in numbers]

#String as List
name = "Angela"
letters_list = [letter for letter in name]

#Range as List
range_list = [n * 2 for n in range(1, 5)]

#Conditional List Comprenhension
names = ["Alex", "Beth", "Caroline", "Dave", "Elanor", "Freddie"]
short_names = [name for name in names if len(name) < 5]

upper_case_names = [name.upper() for name in names if len(name) > 4]

#Dictionary Comprehension
import random
student_grades = {name: random.randint(1, 100) for name in names}
print(student_grades)

passed_students = {
    student: grade
    for (student, grade) in student_grades.items() if grade >= 60
}
print(passed_students)

# For example if we want to assign random score to students
import random

names = ['Alex', 'Beth', 'Carolina', 'Dave', 'Eleanor', 'Freddie']

student_scores = {student: random.randint(0, 100) for student in names}
print(student_scores)

# let's say we want to use this dictionary in our next dictionary comprehension
# only names with a score of over 60
passed_students = {student: score for (student, score) in student_scores.items() if score >= 60}
print(passed_students)

# --------------------------------------------------------
# split the string and save them in a dictionary along with the word count

sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
result = {word: len(word) for word in sentence.split()}
print(result)

"""
You are going to use Dictionary Comprehension to create a dictionary called weather_f
 hat takes each temperature in degrees Celsius and converts it into degrees Fahrenheit.

input {"Monday": 12, "Tuesday": 14, "Wednesday": 15, "Thursday": 14, "Friday": 21, "Saturday": 22, "Sunday": 24}
"""
weather_c = eval(input())

# the items() create tuple for the (key:value) pair
weather_f = {day: temp * 9 / 5 + 32 for (day, temp) in weather_c.items()}
print(weather_f)

# output {'Monday': 53.6, 'Tuesday': 57.2, 'Wednesday': 59.0, 'Thursday': 57.2,
# 'Friday': 69.8, 'Saturday': 71.6, 'Sunday': 75.2}

# -----------------------------------------------------------------------
# How to iterate over a Pandas DataFrame

student_dict = {
    "student": ["Alex", "James", "Cath"],
    "score": [56, 76, 98]
}

# Looping through dictionaries
for (key, value) in student_dict.items():
    print(key)
    print(value)

import pandas
student_data_frame = pandas.DataFrame(student_dict)
print(student_data_frame)

# Loop through a data frame the same way as before
for (key, value) in student_data_frame.items():
    print(key)
    print(value)

# Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    if row.student == "Alex":
        print(row.score)
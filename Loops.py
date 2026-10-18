# Loops is a control structure that allows you to repeat a block of code multiple times.
# Will about the for loop and the while loop
# While loop
"""
print("Hello")
print("Hello")
print("Hello")
print("Hello")
print("Hello")

"""
"""
# While loop
count = 0
while count < 10:
    print("Hello")
    count = count + 1  # Updating the state of Loop variable

"""
"""
# While loop
count = 1
while count <= 10:
    print("Hello")
    count = count + 1  # Updating the state of Loop variable

"""

"""
# While loop
count = 1
while count <= 10:
    print("Hello")
    count +=1
"""


# Escaping an infinite loop with break
"""
while True:
    answer = input("Type 'exit' to quit:")
    if answer.lower() == 'exit':
       break

       
"""


"""
# For loop
# Known number of iterations/repatitions
for i in range(10):#0-9
    print("Hello")
    
"""


"""
# For loop
# Known number of iterations/repatitions
for i in range(2, 10):#2-9
    print("Hello")

"""


# For loop
# Known number of iterations/repatitions
# Finding all the even numbers from 2 to 10
"""
for num in range(2, 11,2 ):
    print(num)

""" 


# fruits = ['apple', 'banana', 'orange'] == strings
# Looping through a list
"""
scores = [85, 90, 73, 68, 72]
for score in scores:
    if score >= 70:
        print("passed")
    else:
        print("fail")

"""


"""
# Looping through dictionary #Key: Values
student = {
    "name": "Alice", 
    "active": True
}

for key, value in student.items():
    print(key, value)

"""

"""

users = [
    {"name": "Alice", "active": True},
    {"name": "Jane", "active": False},
    {"name": "Tom", "active": True},
    {"name": "Michael", "active": True},
    {"name": "Daisy", "active": False},
]

for user in users:
    if user["active"]:
        print(user["name"])

"""


"""

students = [
    {"name": "Alice", "score": 85},
    {"name": "Jane", "score": 90},
    {"name": "Tom", "score": 73},
    {"name": "Michael", "score": 68},
    {"name": "Daisy", "score": 71},
]

# Print pass/fail for each student
for student in students:
    if student["score"] >= 75:
        print(student["name"], "passed")
    else:
        print(student["name"], "failed")

"""

# Given a list of numbers, Calculate and print Total sum and average
# [10, 20, 30, 40, 50]
"""
Numbers = [10, 20, 30, 40, 50]
total = 0

for num in Numbers:
    total += num

average = total / len(Numbers)

print("Total:", total)
print("Average:", average)

"""

# Write a program that prints a multiplication table for numbers 1 to 5 using for loop
# Nested loops are loop inside a loop
"""
for row in range(3):# Rows
    for col in range(3):# Colums
        print("X", end="")
    print()

"""
"""
for i in range(1, 6):
    for j in range(1, 6):
        print(i*j, end=" ")
    print()

"""
# Print the following pattern using nested loop
# *
# * *
# * * *
"""
for i in range(1, 4):
    for j in range(i):
        print("*", end=" ")
    print()

"""

# Write a program that ask the user for a sentence and counts the number of words in the sentence
# FizzBuzz problem

# Write a program that ask the user for a sentence and counts the number of words in the sentence
"""
sentence = input("Enter sentence: ")
words = sentence.split()
word_count = len(words)
print(f"Number of words: {word_count}")


"""

# FizzBuzz problem
"""
for i in range (1, 101):
    if i % 15 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)

"""

for i in range (1, 31):
    if i % 15 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)





"""
Student = ["Alice", 85, "Data Analytics"]


Student = {
    "Name": "Alice",
    "Score": 85,
    "Course": "Data Analytics"
}

print(Student["Score"])

"""


"""
Student = ["Alice", 85, "Data Analytics"]


Student = {
    "Name": "Alice",
    "Score": 85,
    "Course": "Data Analytics"
}


for key in Student:
    print(key, Student[key])

"""


"""
Student = ["Alice", 85, "Data Analytics"]


Student = {
    "Name": "Alice",
    "Score": 85,
    "Course": "Data Analytics"
}


for key, value in Student.items():
    print(key, value)

"""



"""
students = [
    {"name": "Joan", "score": "90"},
    {"name": "Chief", "score": "75"},
    {"name": "Mercy", "score": "N/A"},
    {"name": "Mercy"},
    {"name": "Stella", "score": "83"}

]

# Safely extract scores
# Ignore missing or invalid entries
# Compute class average
# print each valid student neatly

good_scores = []

for student in students:
    try:
        number = int(student.get("score"))
        good_scores.append(number)
        print(student["name"], number)
    except (ValueError, TypeError):
        pass

average = sum(good_scores) / len(good_scores)
print("Class average:", average)

"""




"""
students = [
    {"name": "Joan", "score": "90"},
    {"name": "Chief", "score": "75"},
    {"name": "Mercy", "score": "N/A"},
    {"name": "Mercy"},
    {"name": "Stella", "score": "83"}

]

# Safely extract scores
# Ignore missing or invalid entries
# Compute class average
# print each valid student neatly

Total = 0
valid_count = 0
print("valid student records")

for student in students:
    try:
        score = int(student["score"])
        name = student["name"]

        print(f"{name}: {score}")

        Total += score
        valid_count += 1

    except(ValueError, KeyError):
        continue

if valid_count >0:
    average = Total / valid_count
    print(f"Class Average: {average:.2f}")
else:
    print("No valid scores found")
    
"""


students = [
    {"name": "Joan", "score": "90"},
    {"name": "Chief", "score": "75"},
    {"name": "Mercy", "score": "N/A"},
    {"name": "Mercy"},
    {"name": "Stella", "score": "83"}

]

# Safely extract scores
# Ignore missing or invalid entries
# Compute class average
# print each valid student neatly


valid_scores = []
print("valid student records")

for student in students:
    try:
        score = int(student["score"])
        name = student["name"]
        valid_scores.append(score)
        print(f"{name}: {score}")

       

    except(ValueError, KeyError):
        continue

if valid_scores:
    average = sum(valid_scores) / len(valid_scores)
    print(f"average: {average:.1f}")
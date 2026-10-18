# Lists is an ordered container of values
"""
scores = [78, 85, 90, 45, 68]
# Indexing
print(scores[0])

"""
"""
scores = [78, 85, 90, 45, 68]
# Indexing
print(scores[-1])


"""

"""
scores = [78, 85, 90, 45, 68]
# Indexing
print(scores[0:3])

"""

"""
scores = [78, 85, 90, 45, 68]
# Indexing
print(scores[1:])

"""

"""
scores = [78, 85, 90, 45, 68]
# Indexing
for i in range (len(scores)):
    print(i, scores[i])

"""

"""
scores = [78, 85, 90, 45, 68]
# Indexing
Total = 0
for score in scores:
    Total += score
average = Total / len(scores)

print("Total: ", Total )
print("Average:", average)


"""


"""
scores = [78, 85, 90, 45, 68]
# Indexing

for i in range(len(scores)):
    print(i, scores[i])

"""


"""
scores = [78, 85, 90, 45, 68]
# Indexing

for score in range(len(scores)):# 0-4
    print(score, scores[score])

print(scores[1])


"""



"""
scores = [78, 85, 90, 45, 68]
# Indexing
raw_scores = ["78", "85", "90", "absent"]
# Clean score data
clean_scores = []
for s in raw_scores:
    if s.isdigit():
        clean_scores.append(int(s))
print(clean_scores)


"""


"""
raw_scores = ["78", "85", "90", "absent"]
clean_scores = []
# Indexing
# Exception handling
for s in raw_scores:
    try:
        clean_scores.append(int(s))
    except ValueError:
        pass
    print(clean_scores)

    
"""

# Data = ["85", "90", "N/A", "78", "", "100", "absent", "88"]
# Convert valid numbers into intergers
# Ignore invalid values safely
# Calculate
# Average
# Highest score
# Lowest score

"""
clean_scores = []
for item in Data:
    try:
        clean_scores.append(int(item))
    except ValueError:
        pass
    print(clean_scores)

# Calculate

average = sum(clean_scores) / len(clean_scores)
highest = max(clean_scores)
lowest = min(clean_scores)

print("Clean scores:", clean_scores)
print("Average:", average)
print("Highest:", highest)
print("Lowest:", lowest)


"""



Data = ["85", "90", "N/A", "78", "", "100", "absent", "88"]
# Convert valid numbers into intergers
# Ignore invalid values safely
# Calculate
# Average
# Highest score
# Lowest score

clean_scores = []
for item in Data:
    try:
        clean_scores.append(int(item))
    except ValueError:
        pass
    print(clean_scores)

# Calculate


average = sum(clean_scores) / len(clean_scores)
highest = max(clean_scores)
lowest = min(clean_scores)

print("Clean score:", clean_scores)
print("Average:", average)
print("Highest:", highest)
print("Lowest:", lowest)




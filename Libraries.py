"""
import math
"""

"""
print(math.sqrt(16))
"""


"""
print(math.sqrt(590))
"""

"""
from math import sqrt
print(sqrt(726))
"""


"""
import math
from math import sqrt
print(sqrt(625))

"""
# Aliases
"""
import statistics as stats
"""
"""
print(stats.mean([70, 80, 90]))
"""

"""
print(stats.mean([70, 80, "N/A", 90]))
"""

"""
raw_scores = (["78", "85", "N/A", "90"])
clean_scores = []

for score in raw_scores:
    try:
        clean_scores.append(int(score))
    except ValueError:
        pass
average = stats.mean(clean_scores)
print(average)
"""

"""
raw_scores = (["78", "85", "N/A", "90"])
clean_scores = []

for score in raw_scores:
    try:
        clean_scores.append(int(score))
    except ValueError:
        pass
mode = stats.mode(clean_scores)
print(mode)
"""


"""
raw_scores = (["78", "85", "N/A", "90"])
clean_scores = []

for score in raw_scores:
    try:
        clean_scores.append(int(score))
    except ValueError:
        pass
median = stats.median(clean_scores)
print(median)
"""


# Aliases
"""
import math
print(math.ceil(4.2))
print(math.floor(4.8))

"""

# Aliases
"""
from datetime import datetime
now = datetime.now()
print(now)
"""

# Aliases
from datetime import datetime
date = datetime.strptime("2026-10-13", "%Y-%m-%d")
print(date)


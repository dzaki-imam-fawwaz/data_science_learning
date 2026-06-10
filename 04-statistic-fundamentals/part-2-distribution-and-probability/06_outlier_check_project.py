"""
TOPIC: Outlier Check Project

QUESTION:
Is a value unusually far from the rest?

GOAL:
Use mean and standard deviation to inspect possible outliers.

SIMPLE RULE:
If a value is more than 2 or 3 standard deviations away from the mean,
it may be considered unusual.

NOTE:
This is a simple beginner-friendly rule, not the only outlier detection method.
"""

import statistics

scores = [60, 65, 70, 75, 80, 85, 90, 95, 100]

mean_score = statistics.mean(scores)
std_score = statistics.stdev(scores)

value_to_check = 100

distance_from_mean = abs(value_to_check - mean_score)
std_distance = distance_from_mean / std_score

print("Scores:", scores)
print("Mean:", mean_score)
print("Standard Deviation:", std_score)

print("\nValue to Check:", value_to_check)
print("Distance from Mean:", distance_from_mean)
print("Standard Deviation Distance:", std_distance)

if std_distance > 2:
    print("Result: Possible outlier")
else:
    print("Result: Not an outlier")

"""
INTERPRETATION:
The value 100 is high, but based on this dataset it may still be normal.

CHALLENGE:
Change value_to_check to 150.
Then observe whether the result changes.
"""


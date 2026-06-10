"""
TOPIC: Mean

QUESTION:
What is the average value?

GOAL:
Learn how to calculate the mean manually and with Python.

REAL WORLD USE CASES:
- Average sales
- Average salary
- Average customer spending
- Average exam score
"""

scores = [80, 90, 70, 100]

# Manual calculation
total_score = sum(scores)
number_of_scores = len(scores)

mean_score = total_score / number_of_scores

print("Scores:", scores)
print("Total Score:", total_score)
print("Number of Scores:", number_of_scores)
print("Mean Score:", mean_score)

"""
EXPECTED OUTPUT:
Scores: [80, 90, 70, 100]
Total Score: 340
Number of Scores: 4
Mean Score: 85.0

INTERPRETATION:
The average score is 85.
"""


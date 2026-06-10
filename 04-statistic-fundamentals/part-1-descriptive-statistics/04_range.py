"""
TOPIC: Range

QUESTION:
How far apart are the maximum and minimum values?

GOAL:
Understand the simplest way to measure data spread.

REAL WORLD USE CASES:
- Price range
- Age range
- Score range
"""

scores = [80, 90, 70, 100]

minimum_score = min(scores)
maximum_score = max(scores)
score_range = maximum_score - minimum_score

print("Scores:", scores)
print("Minimum Score:", minimum_score)
print("Maximum Score:", maximum_score)
print("Range:", score_range)

"""
EXPECTED OUTPUT:
Minimum Score: 70
Maximum Score: 100
Range: 30

INTERPRETATION:
The difference between the highest and lowest score is 30.
"""


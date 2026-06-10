"""
TOPIC: Distribution

QUESTION:
What shape does the data have?

GOAL:
Understand how values are distributed around the mean.

REAL WORLD USE CASES:
- Exam scores
- Heights
- Customer spending
- Model prediction errors

WHY THIS MATTERS:
Machine Learning models often depend on the pattern or distribution of data.
A distribution helps us see whether data is balanced, skewed, normal, or contains outliers.
"""

import numpy as np

scores = np.array([80, 85, 75, 90, 95, 78, 82, 88, 92, 77])

mean_score = scores.mean()
std_score = scores.std()

print("Scores:", scores)
print("Mean:", mean_score)
print("Standard Deviation:", std_score)

"""
INTERPRETATION:
The mean shows the center of the data.
The standard deviation shows how spread out the scores are.

If most values are near the mean, the data is consistent.
If many values are far from the mean, the data is more spread out.
"""


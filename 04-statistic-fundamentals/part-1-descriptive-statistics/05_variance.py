"""
TOPIC: Variance

QUESTION:
How spread out is the data?

GOAL:
Understand that variance measures how far values spread from the mean.

REAL WORLD USE CASES:
- Risk analysis
- Salary inequality
- Sales volatility
- Model error variability

IMPORTANT:
Variance is useful conceptually, but its unit is squared.
That is why standard deviation is usually easier to interpret.
"""

import statistics

class_a_scores = [78, 80, 82, 79, 81]
class_b_scores = [10, 50, 80, 100, 160]

class_a_mean = statistics.mean(class_a_scores)
class_b_mean = statistics.mean(class_b_scores)

class_a_variance = statistics.variance(class_a_scores)
class_b_variance = statistics.variance(class_b_scores)

print("Class A Scores:", class_a_scores)
print("Class A Mean:", class_a_mean)
print("Class A Variance:", class_a_variance)

print("\nClass B Scores:", class_b_scores)
print("Class B Mean:", class_b_mean)
print("Class B Variance:", class_b_variance)

"""
EXPECTED OUTPUT:
Class A Mean: 80
Class B Mean: 80

But Class B Variance is much larger.

INTERPRETATION:
Both classes have the same average score.
However, Class B scores are much more spread out.
Variance helps us detect that difference.
"""


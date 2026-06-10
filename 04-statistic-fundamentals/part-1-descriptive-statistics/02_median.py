"""
TOPIC: Median

QUESTION:
What is the middle value?

GOAL:
Understand why median is useful when data has outliers.

REAL WORLD USE CASES:
- Salary analysis
- House price analysis
- Customer spending analysis
"""

import statistics

scores = [70, 80, 90]
salaries = [5, 5, 6, 7, 100]

score_median = statistics.median(scores)
salary_mean = statistics.mean(salaries)
salary_median = statistics.median(salaries)

print("Scores:", scores)
print("Median Score:", score_median)

print("\nSalaries:", salaries)
print("Mean Salary:", salary_mean)
print("Median Salary:", salary_median)

"""
EXPECTED OUTPUT:
Median Score: 80
Mean Salary: 24.6
Median Salary: 6

INTERPRETATION:
The salary mean is affected by the outlier 100.
The median gives a better representation of the typical salary.
"""


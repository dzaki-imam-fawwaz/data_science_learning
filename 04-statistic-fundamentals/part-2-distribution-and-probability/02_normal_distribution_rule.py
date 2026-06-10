"""
TOPIC: Normal Distribution Rule

QUESTION:
Where are most values located in a normal distribution?

GOAL:
Understand the 68-95-99.7 rule.

RULE:
In a normal distribution:

- Around 68% of data is within mean +/- 1 standard deviation
- Around 95% of data is within mean +/- 2 standard deviations
- Around 99.7% of data is within mean +/- 3 standard deviations

REAL WORLD USE CASES:
- Outlier detection
- Risk analysis
- Quality control
"""

mean_score = 80
std_score = 10

lower_1_std = mean_score - std_score
upper_1_std = mean_score + std_score

lower_2_std = mean_score - (2 * std_score)
upper_2_std = mean_score + (2 * std_score)

lower_3_std = mean_score - (3 * std_score)
upper_3_std = mean_score + (3 * std_score)

print("Mean:", mean_score)
print("Standard Deviation:", std_score)

print("\n68% range:", lower_1_std, "to", upper_1_std)
print("95% range:", lower_2_std, "to", upper_2_std)
print("99.7% range:", lower_3_std, "to", upper_3_std)

"""
EXPECTED OUTPUT:
68% range: 70 to 90
95% range: 60 to 100
99.7% range: 50 to 110

INTERPRETATION:
If exam scores are normally distributed with mean 80 and std 10,
most students will score between 70 and 90.
"""


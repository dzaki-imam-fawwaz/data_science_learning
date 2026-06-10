"""
TOPIC:
Hypothesis Testing

GOAL:
Understand how to test whether two groups are significantly different.

WHY THIS MATTERS:
Data Scientists use hypothesis testing to avoid making decisions based on random chance.

Example question:
Is the new teaching method really better, or did the result happen by chance?
"""

from scipy import stats

old_method_scores = [70, 72, 68, 71, 69, 70, 73, 68]
new_method_scores = [78, 80, 77, 79, 81, 76, 80, 82]

t_statistic, p_value = stats.ttest_ind(
    old_method_scores,
    new_method_scores
)

print("Old Method Scores:", old_method_scores)
print("New Method Scores:", new_method_scores)

print("\nT-Statistic:", t_statistic)
print("P-Value:", p_value)

alpha = 0.05

if p_value < alpha:
    print("\nConclusion: Reject the null hypothesis.")
    print("There is a statistically significant difference.")
else:
    print("\nConclusion: Fail to reject the null hypothesis.")
    print("There is not enough evidence to say the groups are different.")

"""
IMPORTANT CONCEPTS:

Null Hypothesis (H0):
There is no difference between the two groups.

Alternative Hypothesis (H1):
There is a difference between the two groups.

P-value:
The probability of seeing a result like this if the null hypothesis is true.

Common rule:
If p-value < 0.05, the result is considered statistically significant.
"""


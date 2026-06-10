"""
TOPIC:
A/B Testing

GOAL:
Understand how to compare two product versions.

WHY THIS MATTERS:
Companies use A/B testing to decide which version performs better.

Examples:
- Old landing page vs new landing page
- Blue button vs green button
- Current pricing vs new pricing
"""

from scipy import stats

# Daily signup counts from old homepage
old_homepage_signups = [
    100, 105, 98, 110, 102,
    99, 101, 106, 103, 100
]

# Daily signup counts from new homepage
new_homepage_signups = [
    120, 125, 118, 130, 122,
    119, 121, 126, 123, 120
]

old_average = sum(old_homepage_signups) / len(old_homepage_signups)
new_average = sum(new_homepage_signups) / len(new_homepage_signups)

t_statistic, p_value = stats.ttest_ind(
    old_homepage_signups,
    new_homepage_signups
)

print("Old Homepage Average Signups:", old_average)
print("New Homepage Average Signups:", new_average)

print("\nT-Statistic:", t_statistic)
print("P-Value:", p_value)

alpha = 0.05

if p_value < alpha:
    print("\nConclusion:")
    print("The new homepage performs significantly differently from the old homepage.")
else:
    print("\nConclusion:")
    print("The difference may be due to random chance.")

"""
BUSINESS INTERPRETATION:
If the p-value is below 0.05, the company has stronger evidence that the new homepage changed performance.

But remember:
Statistical significance does not always mean business significance.

Example:
A 0.1% improvement may be statistically significant but may not be worth implementing.
"""


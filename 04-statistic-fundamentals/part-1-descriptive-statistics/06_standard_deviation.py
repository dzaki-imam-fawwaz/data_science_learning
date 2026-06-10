"""
TOPIC: Standard Deviation

QUESTION:
On average, how far are values from the mean?

GOAL:
Understand standard deviation as a readable measure of spread.

REAL WORLD USE CASES:
- Measuring consistency
- Detecting unstable sales performance
- Understanding model error
- Preparing data for machine learning

KEY IDEA:
Mean tells us the center.
Standard deviation tells us how spread out the data is.
"""

import statistics

consistent_scores = [78, 80, 82, 79, 81]
spread_scores = [10, 50, 80, 100, 160]

consistent_std = statistics.stdev(consistent_scores)
spread_std = statistics.stdev(spread_scores)

print("Consistent Scores:", consistent_scores)
print("Standard Deviation:", consistent_std)

print("\nSpread Scores:", spread_scores)
print("Standard Deviation:", spread_std)

"""
EXPECTED OUTPUT:
The spread scores will have a much higher standard deviation.

INTERPRETATION:
Low standard deviation means values are close to the mean.
High standard deviation means values are far from the mean.
"""


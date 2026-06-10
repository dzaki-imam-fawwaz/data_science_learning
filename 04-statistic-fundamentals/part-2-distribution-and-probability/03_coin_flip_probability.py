"""
TOPIC: Probability - Coin Flip

QUESTION:
How likely is an event?

GOAL:
Simulate coin flips and estimate the probability of getting Heads.

REAL WORLD CONNECTION:
Machine learning classification often predicts probability.

Example:
Spam probability = 0.95
"""

import random

heads_count = 0
number_of_trials = 1000

for _ in range(number_of_trials):
    result = random.choice(["Heads", "Tails"])

    if result == "Heads":
        heads_count += 1

probability_of_heads = heads_count / number_of_trials

print("Number of Trials:", number_of_trials)
print("Heads Count:", heads_count)
print("Probability of Heads:", probability_of_heads)

"""
EXPECTED OUTPUT:
The probability should be close to 0.5.

INTERPRETATION:
With more trials, the result gets closer to the theoretical probability.
"""


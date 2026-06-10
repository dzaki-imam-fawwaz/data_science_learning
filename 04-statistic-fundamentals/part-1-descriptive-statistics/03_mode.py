"""
TOPIC: Mode

QUESTION:
Which value appears most often?

GOAL:
Learn how to find the most frequent value in a dataset.

REAL WORLD USE CASES:
- Most popular product
- Most common customer category
- Most frequent rating
"""

import statistics

product_ratings = [5, 4, 5, 3, 5, 4, 2]

most_common_rating = statistics.mode(product_ratings)

print("Product Ratings:", product_ratings)
print("Most Common Rating:", most_common_rating)

"""
EXPECTED OUTPUT:
Most Common Rating: 5

INTERPRETATION:
Rating 5 appears most often.
This means most customers gave the product a high rating.
"""


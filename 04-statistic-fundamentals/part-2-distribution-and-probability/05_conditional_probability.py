"""
TOPIC: Conditional Probability

QUESTION:
What is the probability of an event given another event?

GOAL:
Understand P(Buy | Visit).

REAL WORLD USE CASES:
- Marketing conversion
- Recommendation systems
- Fraud detection
- Customer behavior analysis
"""

website_visitors = 100
buyers_after_visit = 20

probability_buy_given_visit = buyers_after_visit / website_visitors

print("Website Visitors:", website_visitors)
print("Buyers After Visit:", buyers_after_visit)
print("P(Buy | Visit):", probability_buy_given_visit)

"""
EXPECTED OUTPUT:
P(Buy | Visit): 0.2

INTERPRETATION:
20% of website visitors made a purchase.
"""


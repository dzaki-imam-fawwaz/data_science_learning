# Exercise Solutions

## Exercise 01

```python
import statistics

sales = [100, 120, 130, 90, 110, 150, 160]

print("Mean:", statistics.mean(sales))
print("Median:", statistics.median(sales))
print("Range:", max(sales) - min(sales))
print("Variance:", statistics.variance(sales))
print("Standard Deviation:", statistics.stdev(sales))
```

Interpretation:

The mean shows the average sales value.
The standard deviation shows how spread out the sales numbers are.

## Exercise 02

```python
from scipy import stats

version_a_revenue = [200, 210, 190, 205, 198, 202, 207]
version_b_revenue = [230, 240, 225, 235, 238, 232, 236]

average_a = sum(version_a_revenue) / len(version_a_revenue)
average_b = sum(version_b_revenue) / len(version_b_revenue)

t_statistic, p_value = stats.ttest_ind(version_a_revenue, version_b_revenue)

print("Average A:", average_a)
print("Average B:", average_b)
print("P-Value:", p_value)

if p_value < 0.05:
    print("The difference is statistically significant.")
else:
    print("The difference may be due to random chance.")
```


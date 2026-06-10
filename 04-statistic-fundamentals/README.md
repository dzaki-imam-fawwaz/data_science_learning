# Statistic Fundamentals for Data Science

This module teaches the most important statistics concepts for beginner Data Scientists.

The goal is not to memorize formulas first. The goal is to understand what each concept is used for in real data analysis and machine learning.

## Why Statistics Matters

Statistics helps Data Scientists understand data before building machine learning models.

You use statistics to answer questions like:

- What is the average value?
- Is the data consistent or highly spread out?
- Are there unusual values?
- How likely is an event?
- Is a change meaningful or just random chance?
- Is version B really better than version A?

## Learning Objectives

By the end of this module, you should understand:

1. Mean
2. Median
3. Mode
4. Range
5. Variance
6. Standard Deviation
7. Distribution
8. Normal Distribution Rule
9. Probability
10. Conditional Probability
11. Outlier Detection
12. Hypothesis Testing
13. A/B Testing

## Module Structure

```text
04-statistic-fundamentals/
|
|-- README.md
|-- datasets/
|   |-- student_scores.csv
|   `-- ab_test_results.csv
|-- part-1-descriptive-statistics/
|   |-- README.md
|   |-- 01_mean.py
|   |-- 02_median.py
|   |-- 03_mode.py
|   |-- 04_range.py
|   |-- 05_variance.py
|   |-- 06_standard_deviation.py
|   `-- 07_summary_project.py
|-- part-2-distribution-and-probability/
|   |-- README.md
|   |-- 01_distribution_intro.py
|   |-- 02_normal_distribution_rule.py
|   |-- 03_coin_flip_probability.py
|   |-- 04_dice_probability.py
|   |-- 05_conditional_probability.py
|   `-- 06_outlier_check_project.py
|-- part-3-statistical-testing/
|   |-- README.md
|   |-- 01_hypothesis_testing.py
|   `-- 02_ab_testing.py
`-- exercises/
    |-- exercise_01_basic_statistics.py
    |-- exercise_02_ab_testing.py
    `-- solutions.md
```

## Recommended Learning Order

1. Run `part-1-descriptive-statistics/01_mean.py`
2. Run `part-1-descriptive-statistics/02_median.py`
3. Run `part-1-descriptive-statistics/03_mode.py`
4. Run `part-1-descriptive-statistics/04_range.py`
5. Run `part-1-descriptive-statistics/05_variance.py`
6. Run `part-1-descriptive-statistics/06_standard_deviation.py`
7. Run `part-1-descriptive-statistics/07_summary_project.py`
8. Run `part-2-distribution-and-probability/01_distribution_intro.py`
9. Run `part-2-distribution-and-probability/02_normal_distribution_rule.py`
10. Run `part-2-distribution-and-probability/03_coin_flip_probability.py`
11. Run `part-2-distribution-and-probability/04_dice_probability.py`
12. Run `part-2-distribution-and-probability/05_conditional_probability.py`
13. Run `part-2-distribution-and-probability/06_outlier_check_project.py`
14. Run `part-3-statistical-testing/01_hypothesis_testing.py`
15. Run `part-3-statistical-testing/02_ab_testing.py`
16. Complete the exercises

## Required Libraries

Install the required libraries:

```bash
pip install numpy scipy
```

## Key Ideas

Mean tells you the center of the data.

Standard deviation tells you how spread out or messy the data is.

Distribution and probability help you understand uncertainty.

P-value helps you decide whether a result is likely real or just random chance.


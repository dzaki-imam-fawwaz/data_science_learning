"""
TOPIC: Descriptive Statistics Summary Project

GOAL:
Analyze a small dataset using mean, median, mode, range, variance, and standard deviation.

SCENARIO:
You are analyzing student exam scores.
"""

import statistics

exam_scores = [80, 90, 70, 100, 95, 85, 75, 90]

mean_score = statistics.mean(exam_scores)
median_score = statistics.median(exam_scores)
mode_score = statistics.mode(exam_scores)
score_range = max(exam_scores) - min(exam_scores)
score_variance = statistics.variance(exam_scores)
score_std = statistics.stdev(exam_scores)

print("Exam Scores:", exam_scores)
print("Mean:", mean_score)
print("Median:", median_score)
print("Mode:", mode_score)
print("Range:", score_range)
print("Variance:", score_variance)
print("Standard Deviation:", score_std)

"""
INTERPRETATION GUIDE:

Mean:
The average exam score.

Median:
The middle score.

Mode:
The most frequent score.

Range:
The distance between the highest and lowest score.

Variance:
How spread out the scores are.

Standard Deviation:
The typical distance from the mean.

CHALLENGE:
Change the dataset by adding an outlier, for example 20.
Then compare how the mean and median change.
"""


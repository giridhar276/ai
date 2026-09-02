import statistics

scores = [68, 72, 75, 80, 80, 85, 90, 95]
print("Scores:", scores)

# Measures of central tendency
print("Arithmetic mean:", statistics.mean(scores))
print("Floating-point mean:", statistics.fmean(scores))
print("Median:", statistics.median(scores))
print("Low median:", statistics.median_low(scores))
print("High median:", statistics.median_high(scores))
print("Mode:", statistics.mode(scores))
print("All modes:", statistics.multimode(scores))

# Measures of spread
print("Sample variance:", statistics.variance(scores))
print("Population variance:", statistics.pvariance(scores))
print("Sample standard deviation:", statistics.stdev(scores))
print("Population standard deviation:", statistics.pstdev(scores))

# Divide values into four groups
print("Quartile boundaries:", statistics.quantiles(scores, n=4))

# Weighted average with fmean()
marks = [80, 90, 70]
weights = [0.30, 0.50, 0.20]
print("Weighted average:", statistics.fmean(marks, weights=weights))

# Relationship between two variables
study_hours = [2, 3, 4, 5, 6]
test_scores = [60, 68, 75, 83, 91]
print("Covariance:", statistics.covariance(study_hours, test_scores))
print("Correlation:", statistics.correlation(study_hours, test_scores))
regression = statistics.linear_regression(study_hours, test_scores)
print("Regression slope:", regression.slope)
print("Regression intercept:", regression.intercept)

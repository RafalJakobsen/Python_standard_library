# Statistics Module
import statistics
import math

# Mean - avarage = 7/3 = 2.33333333
# Median - midpoint = 2
# Mode - most frequent value = 2

agesData = [10, 13, 14, 12, 11, 10, 11, 10, 15]

print(statistics.mean(agesData))
print(statistics.mode(agesData))
print(statistics.median(agesData))
print(sorted(agesData))

# Variance - the average of the squared differences from the mean
# ((2-2.33)2 + (2 - 2.33)2 + (3 - 2.33)2)/(3-1) ) 1/3

# Standard deviation - the square root of the variance
# Square root of 1/3 = .57735

print(statistics.variance(agesData))
print(statistics.stdev(agesData))
print(math.sqrt(statistics.variance(agesData)))





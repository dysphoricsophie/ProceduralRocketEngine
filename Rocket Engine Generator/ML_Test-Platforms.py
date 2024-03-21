from scipy import stats

speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]
print(stats.gmean(speed))
print(stats.mode(speed))
print(stats.tmin(speed))
print(stats.tmax(speed))


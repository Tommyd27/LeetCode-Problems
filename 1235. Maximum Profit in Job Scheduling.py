from bisect import bisect
def jobScheduling(startTime, endTime, profit):
	jobs = sorted(zip(startTime, endTime, profit), key=lambda v: v[1])
	dp = [[0, 0]]
	for s, e, p in jobs:
		i = bisect(dp, [s + 1]) - 1
		if dp[i][1] + p > dp[-1][1]:
			dp.append([e, dp[i][1] + p])
	return dp[-1][1]

jobScheduling([1,2,3,4,6], [3,5,10,6,9], [20,20,100,70,60])
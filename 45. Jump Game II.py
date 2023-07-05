def jump(nums: list[int]) -> int:
    m = len(nums)
    def updateSection(beg, jumpStrength):
        for i in range(beg + 1, min(beg + jumpStrength + 1, m)):
            dp[i] = min(dp[i], dp[beg] + 1)
    
    dp = [0] + [float("inf")] * m - 1
    for i, jump in enumerate(nums):
        updateSection(i, jump)
    return dp[-1]
print(jump([2,3,1,1,4]))
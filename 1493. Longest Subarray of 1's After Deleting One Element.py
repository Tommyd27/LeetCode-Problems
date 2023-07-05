def longestSubarray(nums: list[int]) -> int:
    zeros = nums.count(0)
    if zeros <= 1:
        return len(nums) - 1
    prevSection = currentSection = 0
    ans = 0
    for n in nums:
        if n:
            currentSection += 1
            ans = max(ans, currentSection + prevSection)
        else:
            prevSection = currentSection
            currentSection = 0
    return ans

print(longestSubarray([1,1,0,1]))
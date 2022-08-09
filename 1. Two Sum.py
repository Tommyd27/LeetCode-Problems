def twoSum(nums, target):
    subtractionArray = []
    subtractionIndex = []

    for i, num in enumerate(nums):
        for i, num in enumerate(nums):
            subtractionTarget = target - num
            for j, numTwo in enumerate(nums[i + 1]):
                if numTwo == subtractionTarget:
                    return i, i + j + 1
                
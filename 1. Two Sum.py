def twoSum(nums, target):
    subtractionArray = []
    subtractionIndex = []

    for i, num in enumerate(nums):
        try:
            return subtractionIndex[subtractionArray.index(num)], i
        except ValueError:
            subtractionArray.append(num)
            subtractionIndex.append(i)
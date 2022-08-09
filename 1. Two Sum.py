def twoSum(self, nums: list[int], target: int) -> List[int]:
    subtractionDictionary = {}
    i = 0
    for num in nums:
        if num in subtractionDictionary:
            return subtractionDictionary[num], 
        subtractionDictionary[target - num] = i
        i += 1
                
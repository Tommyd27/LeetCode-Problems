def twoSum(nums, target):
    def twoSum(self, nums: list[int], target: int) -> List[int]:
        subtractionDictionary = {}
        for i, num in enumerate(nums):
            if num in subtractionDictionary:
                return subtractionDictionary[num], 
            subtractionDictionary[target - num] = i
        
                
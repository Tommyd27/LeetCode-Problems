def twoSum(nums, target):
    def twoSum(self, nums: list[int], target: int) -> List[int]:
        subtractionDictionary = {}
        for i, num in enumerate(nums):
            try:
                return subtractionDictionary[num], i
            except KeyError:
                subtractionDictionary[num] = i
        
                
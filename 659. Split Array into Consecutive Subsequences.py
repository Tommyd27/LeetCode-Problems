def isPossible(nums: list[int], toRemove = []) -> bool:
    nums = list(nums)
    for i, numRemove in enumerate(toRemove):
        del nums[numRemove - i]
    numsLen = len(nums)
    if numsLen < 3:
        return False
    if validSequence(nums):
        return True
    sequence = [nums[0]]
    indexesToRemove = [0]
    for i, num in enumerate(nums[1:], 1):
        if num == sequence[-1] + 1:
            sequence.append(num)
            indexesToRemove.append(i)
            if len(sequence) >= 3 and isPossible(nums, indexesToRemove):
                return True
    return False
def validSequence(nums):
    for i, num in enumerate(nums[1:], 1):
        if num != nums[i - 1] + 1:
            return False
    return True

print(isPossible([1,2,3,4,4,5]))


#print(validSequence([1,2,3,4,4,5]))
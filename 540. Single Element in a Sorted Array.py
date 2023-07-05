def singleNonDuplicate(nums: list[int]) -> int:
    l, h = 0, len(nums)
    while l < h:
        mid = (l + h) // 2
        if nums[mid] not in [nums[mid + 1], nums[mid - 1]]:
            return nums[mid]
        if mid % 2:
            if nums[mid - 1] != nums[mid]:
                h = mid
            else:
                l = mid + 1
        else:
            if nums[mid + 1] != nums[mid]:
                h = mid
            else:
                l = mid + 1
    return -1
print(singleNonDuplicate([3,3,7,7,10,11,11]))
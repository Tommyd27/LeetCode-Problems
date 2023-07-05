def checkSubarraySum(nums: list[int], k: int) -> bool:
	pos = []
	for num in nums:
		if not num % k:
			return True
		for p in pos:
			p += num
			if not p % k:
				return True
		pos.append(num)
	return False

checkSubarraySum([23,2,6,4,7], 13)
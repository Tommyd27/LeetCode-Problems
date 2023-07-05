def earliestFullBloom(plantTime: list[int], growTime: list[int]) -> int:
	lst = [(plantTime, growTime) for plantTime, growTime in zip(plantTime, growTime)]
	lst.sort(key = lambda x: x[0] - x[1])
	day = lst[0][0]
	done = lst[0][1]
	
	for plantTime, growTime in lst[1:]:
		day += plantTime
		done = max(growTime, done - plantTime)
	return day + done
plantTime = [1,4,3]
growTime = [2, 3, 1]

print(earliestFullBloom(plantTime, growTime))
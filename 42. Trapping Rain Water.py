def trap(height: list[int]) -> int:
	vol = 0
	print(len(height))
	
	
		trapHeight = min(height[i - 1], height[i + 1])
		if trapHeight > height[i]:
			vol += trapHeight - height[i]
	return vol
print(trap([0,1,0,2,1,0,1,3,2,1,2,1]))
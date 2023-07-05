inp = [1,1,-2,6]

def increasingTriplet(nums: list[int]) -> bool:
    sets = {}
    for num in nums:
        for (posSet, val) in sets.items():
            if posSet >= num:
                continue
            if len(val) == 1:
                if val[0] < num:
                    return True
                val[0] = num
            else:
                val.append(num)
        if num not in sets:
            sets[num] = []
    return False
print(increasingTriplet(inp))
            
            
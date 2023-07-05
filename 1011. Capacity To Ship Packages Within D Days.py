def shipWithinDays(weights: list[int], days: int) -> int:
    largest_weight = max(weights)
    m = len(weights)
    lo = largest_weight
    hi = largest_weight * m
    def canDo(weight_value):
        c_count = 0
        day_count = 1
        for weight in weights:
            c_count += weight
            if c_count > weight_value:
                c_count = weight
                day_count += 1
            if day_count > days:
                return False
        return day_count <= days
    print(canDo(11))
    while lo < hi:
        mid = (lo + hi) // 2
        if canDo(mid):
            hi = mid
        else:
            lo = mid + 1
    return lo

print(shipWithinDays([1,2,3,4,5,6,7,8,9,10], 5))
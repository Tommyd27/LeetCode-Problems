def maxSatisfaction(A):
    res = total = 0
    A.sort()
    while A and A[-1] + total > 0:
        total += A.pop()
        res += total
    return res
print(maxSatisfaction([-1,-8,0,5,-7]))
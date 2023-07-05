from collections import Counter

def solution(arrOne, arrTwo):
    cOne, cTwo = Counter(arrOne), Counter(arrTwo)
    out = 0
    for num in cOne:
        out += min(cOne[num], cTwo[num])
    return out

print(solution([1, 2, 3, 3, 4], [3, 4, 5, 6]))
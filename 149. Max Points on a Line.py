from collections import defaultdict
def maxPoints(points: list[list[int]]) -> int:
    amountLines = defaultdict(int)
    pSoFar = []
    for x1, y1 in points:
        for x2, y2 in pSoFar:
            if x2 != x1:
                gradient = abs((y2 - y1) / (x2 - x1))
                c = y1 - gradient * x1
            else:
                gradient = float("inf")
                c = x1
            amountLines[(gradient, c)] += 1
        pSoFar.append((x1, y1))
    return max(amountLines.values())
print(maxPoints([[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]))
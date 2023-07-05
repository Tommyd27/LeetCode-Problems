from collections import Counter
def minSetSize(arr: list[int]) -> int:
    arrCounter = Counter(arr)
    currentSize = len(arr)
    neededSize = currentSize // 2
    numRemoved = 0
    for val in sorted(arrCounter.values()):
        numRemoved += 1
        currentSize -= val
        if currentSize <= neededSize:
            return numRemoved

minSetSize([9,77,63,22,92,9,14,54,8,38,18,19,38,68,58,19])
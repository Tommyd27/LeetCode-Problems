from collections import defaultdict
def firstUniqChar(s: str) -> int:
        
    charDict = defaultdict(list)
    i = 0
    for char in s:
        charDict[char].append(i)
        i += 1
    print(charDict)
    for char in charDict.values():
        if len(char) == 1:
            return charDict[char][0]
    return -1

firstUniqChar("loveleetcode")
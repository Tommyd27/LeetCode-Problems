from collections import Counter
def characterReplacement(s, k):
    maxf = res = 0
    count = Counter()
    for i in range(len(s)):
        count[s[i]] += 1
        maxf = max(maxf, count[s[i]])
        if res - maxf < k:
            res += 1
        else:
            count[s[i - res]] -= 1
    return res
print(characterReplacement("ABAA", 0))
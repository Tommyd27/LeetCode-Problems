from collections import Counter
def findAnagrams(s: str, p: str) -> list[int]:
    m = len(p)
    n = len(s)
    if n < m: return []

    p_counter = Counter(p)
    counter = Counter(s[:m])
    if p_counter == counter:
        ans = [0]
    else:
        ans = []
    for i in range(1, n - m):
        counter[s[i - 1]] -= 1
        counter[s[i + m - 1]] += 1
        if counter == p_counter:
            ans.append(i)
    return ans
findAnagrams("cbaebabacd", "abc")
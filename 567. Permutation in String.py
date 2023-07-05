from collections import Counter
def checkInclusion(s1: str, s2: str) -> bool:
    m, n = len(s1), len(s2)
    if m > n:
        return False
    if m == n:
        return Counter(s1) == Counter(s2)
    matching = 0
    s1_count = Counter(s1) 


    for i in range(n):
        n_char = s2[i]

        if n_char in s1_count:
            s1_count[n_char] -= 1
            if not s1_count[n_char]:
                matching += 1
            
        if i >= m:
            o_char = s2[i - m]
            if o_char in s1_count:
                if not s1_count[o_char]:
                    matching -= 1
                s1_count[o_char] += 1
        if matching == m:
            return True
    return False
print(checkInclusion("rvwrk", "lznomzggwrvrkxecjaq"))
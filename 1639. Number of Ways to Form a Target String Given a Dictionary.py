from collections import Counter
def numWays(words, target):
    n, mod = len(target), 10**9 + 7
    res = [1] + [0] * n
    for i in range(len(words[0])):
        count = Counter(w[i] for w in words)
        for j in range(n - 1, -1, -1):
            res[j + 1] += res[j] * count[target[j]] % mod
    return res[n] % mod
print(numWays(["abba","baab"], "bab"))
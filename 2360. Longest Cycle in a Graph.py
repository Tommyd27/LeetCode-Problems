def longestCycle(edges: list[int]) -> int:
    n = len(edges)
    canLoop = [None] * n
    seen = [False] * n
    for i, n in enumerate(edges):
        if n == -1: 
            canLoop[i] = False
        elif canLoop[n] != False:
            canLoop[n] = True
    ans = -1
    def dfs(pos, parent):
        if pos == -1: return 0
        if pos == parent: return 1
        if seen[pos]: return 0
        seen[pos] = True
        if not canLoop[pos]: return 0
        child = dfs(edges[pos], parent)
        if child:
            return 1 + child
        return 0

    for i in range(n):
        if seen[i] or not canLoop[i]: continue
        seen[i] = True
        loopLen = dfs(edges[i], i)
        if loopLen:
            ans = max(ans, loopLen)
    return ans
print(longestCycle([1,0]))
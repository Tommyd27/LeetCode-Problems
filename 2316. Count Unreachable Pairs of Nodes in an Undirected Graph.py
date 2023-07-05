from collections import defaultdict
def countPairs(n: int, edges: list[list[int]]) -> int:
    grid = defaultdict(list)
    for a, b in edges:
        grid[a].append(b)
        grid[b].append(a)
    visited = [False] * n
    ans = 0
    def dfs(position):
        if visited[position]: return 0
        visited[position] = True
        cnt = 1
        for otherPos in grid[position]:
            cnt += dfs(otherPos)
        return cnt
    for i in range(n):
        if visited[i]: continue
        size = dfs(i)
        ans += size * (n - size)
    return ans

print(countPairs(7, [[0,2],[0,5],[2,4],[1,6],[5,4]]))
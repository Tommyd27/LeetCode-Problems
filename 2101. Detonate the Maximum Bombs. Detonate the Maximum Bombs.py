from collections import defaultdict
def maximumDetonation(bombs: list[list[int]]) -> int:
    grid = defaultdict(list)
    for i, (x, y, radius) in enumerate(bombs):
        for j, (p, q, r2) in enumerate(bombs[i + 1:], i + 1):
            dis = (x - p) ** 2 + (y - q) ** 2
            if dis <= radius:
                grid[i].append(j)
            if dis <= r2:
                grid[j].append(i)
    def dfs(i):
        if i in visited: return 0
        visited.add(i)
        return 1 + sum([dfs(j) for j in grid[i]])
    ans = 0
    for i in range(len(bombs)):
        visited = set()
        ans = max(ans, dfs(i))
    return ans
print(maximumDetonation([[2,1,3],[6,1,4]]))
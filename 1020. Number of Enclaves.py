def numEnclaves(grid: list[list[int]]) -> int:
    m, n = len(grid), len(grid[0])
    def dfs(i, j):
        if not (0 <= i < m and 0 <= j < n): return False
        if grid[i][j] != 1: return None
        grid[i][j] = 2
        ans = 1
        for x, y in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            res = dfs(i + x, j + y)
            if res == False: return False
            if res == None: continue
            ans += res
        return ans
    ans = 0
    for i, row in enumerate(grid):
        for j, cell in enumerate(row):
            if cell != 1: continue
            ans += dfs(i, j)
    return ans
print(numEnclaves([[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]]))
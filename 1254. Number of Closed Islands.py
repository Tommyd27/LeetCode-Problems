def closedIsland(grid: list[list[int]]) -> int:
    m, n = len(grid), len(grid[0])
    def dfs(i, j):
        if not (0 <= i < m and 0 <= j < n):
            return False
        if grid[i][j] != 0: return True
        grid[i][j] = 2
        return all([dfs(i + 1, j),
                    dfs(i - 1, j),
                    dfs(i, j + 1),
                    dfs(i, j - 1)
                    ])

    ans = 0
    for i, row in enumerate(grid):
        for j, cell in enumerate(row):
            if cell: continue
            ans += dfs(i, j)
    return ans
print(closedIsland([[0,0,1,0,0],[0,1,0,1,0],[0,1,1,1,0]]))
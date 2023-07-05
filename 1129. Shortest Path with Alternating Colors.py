def shortestAlternatingPaths(n: int, redEdges: list[list[int]], blueEdges: list[list[int]]) -> list[int]:
    grid = {}
    ans = [-1] * n
    for a, b in redEdges:
        if a in grid:
            grid[a][True].append(b)
        else:
            grid[a] = {True : [b], False : []}
    for a, b in blueEdges:
        if a in grid:
            grid[a][False].append(b)
        else:
            grid[a] = {False : [b], True : []}
    stack = [(0, 0, True), (0, 0, False)]
    while stack:
        pos, steps, color = stack.pop()
        if ans[pos] == -1:
            ans[pos] = steps
        else:
            ans[pos] = min(ans[pos], steps)
        n_color = not color
        if pos in grid and grid[pos][n_color]:
            for other_pos in grid[pos][n_color]:
                stack.append((other_pos, steps + 1, n_color))
            grid[pos][n_color] = []
    return ans
print(shortestAlternatingPaths(5, [[2,2],[0,4],[4,2],[4,3],[2,4],[0,0],[0,1],[2,3],[1,3]], [[0,4],[1,0],[1,4],[0,0],[4,0]]))
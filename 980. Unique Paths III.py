def uniquePathsIII(grid: list[list[int]]) -> int:
    height = len(grid)
    width = len(grid[0])
    area = height * width
    obstacles = 0
    startingPos = 0
    for i, row in enumerate(grid):
        for j, cell in enumerate(row):
            if cell == -1:
                obstacles += 1
            elif cell == 1:
                startingPos = (i, j)
    nonObstacles = area - obstacles
    stack = [[startingPos, 1, set([startingPos])]]
    count = 0
    moves = [(1,0), (-1, 0), (0, 1), (0, -1)]
    while stack:
        (i, j), num, cSet = stack.pop()
        if num == nonObstacles:
            if grid[i][j] == 2:
                count += 1
            continue
        for move in moves:
            newLocation = (i + move[0], j + move[1])
            if not (0 <= newLocation[0] < height and 0 <= newLocation[1] < width):
                continue
            if newLocation in cSet:
                continue
            cell = grid[newLocation[0]][newLocation[1]]
            if cell in [2, -1]:
                continue
            cSet.add(newLocation)
            stack.append([newLocation, num + 1, cSet])
    return count
print(uniquePathsIII([[1,0,0,0],[0,0,0,0],[0,0,2,-1]]))
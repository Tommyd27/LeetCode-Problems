def canVisitAllRooms(rooms: list[list[int]]) -> bool:
    visited = set()
    def dfs(node):
        for nodeToCheck in node:
            visited.add(nodeToCheck)
            dfs(rooms[nodeToCheck])
    dfs(rooms[0])
    return len(visited) + 1 == len(rooms)
print(canVisitAllRooms([[1],[2],[3],[]]))
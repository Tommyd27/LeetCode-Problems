def allPathsSourceTarget(graph: list[list[int]]) -> list[list[int]]:
    n = len(graph) - 1
    def dfs(node, path):
        path = [x for x in path] + [node]
        if node == n:
            return [path]
        out = []
        for connection in graph[node]:
            out.extend(dfs(connection, path))
        return out
    return dfs(0, [])

print(allPathsSourceTarget([[1,2],[3],[3],[]]))
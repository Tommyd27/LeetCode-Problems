from collections import defaultdict
"""class Solution:
    def __init__(self) -> None:
        pass
    def numberOfGoodPaths(self, vals: list[int], edges: list[list[int]]) -> int:
        grid = defaultdict(list)
        for a, b in edges:
            grid[a].append(b)
            grid[b].append(a)
        self.ans = 0
        vals_len = 0
        def dfs(node, val, p):
            if vals[node] > val:
                return
            if vals[node] == val and p != -1:
                self.ans += 1
            for child_node in grid[node]:
                if child_node == p: continue

                dfs(child_node, val, node)
        for i, val in enumerate(vals):
            vals_len += 1
            dfs(i, val, -1)
        return (self.ans / 2) + vals_len
sol = Solution()"""
def numberOfGoodPaths(vals: list[int], edges: list[list[int]]) -> int:
    # Most basic Union-Find template without ranking optimization.
    # Please share yours if you have a good Union-Find template with ranking optimization
    UF = {}
    def find(x):
        UF.setdefault(x,x)
        if x != UF[x]:
            UF[x] = find(UF[x])
        return UF[x]
    def union(x,y):
        UF[find(x)] = find(y)
    
    tree = defaultdict(list)
    # Using a hashmap of set to get the nodes with the same value easily.
    val2Nodes = defaultdict(set)
    for s,e in edges:
        tree[s].append(e)
        tree[e].append(s)
        val2Nodes[vals[s]].add(s)
        val2Nodes[vals[e]].add(e)
    
    # Include the one node path in the result, because it is not calculated when we do comb(n,r).
    res = len(vals)
    
    # Sort the value, and start to union the nodes with the current v that we are checking and their neighbors (have smaller values than the current v).
    for v in sorted(val2Nodes.keys()):
        # Union elements with the current v with its neighbor if its neighbor has a value smaller than v.
        # In this way, our unioned element will only have values smaller than or equal to the current v.
        for node in val2Nodes[v]:
            for nei in tree[node]:
                if vals[nei] <= v:
                    print("ello")
                    union(node,nei)
        
        # For each group, we need to count the number of elements with value==v in this group.
        groupCount = defaultdict(int)
        for node in val2Nodes[v]:
            groupCount[find(node)] += 1
            
        for root in groupCount.keys():
            # The following two lines are doing the same thing
            # If there are n number of nodes that have value==v in the a group. 
            # The number of paths is the number of combinations for selecting 2 elements from n elements (repetitions are not allowed).
            
            #res += comb(groupCount[root],2)
            
            res += groupCount[root] * (groupCount[root]-1) // 2
    
    return res
print(numberOfGoodPaths([1,3,2,1,3], [[0,1],[0,2],[2,3],[2,4]]))
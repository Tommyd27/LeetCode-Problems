import heapq
def findMaximizedCapital(k: int, w: int, profits: list[int], capital: list[int]) -> int:
    q = []
    current_capital = -w
    projects_done = 0
    projects = sorted([(-y, -x) for x, y in zip(capital, profits)], key = lambda x : x[1], reverse = True)
    while projects_done < k and projects:
        projects_done += 1
        for negative_profit, negative_cost in projects:
            if negative_profit >= 0: break
            heapq.heappush(q, negative_profit)
        if q:
            project_profit = heapq.heappop(q)
            current_capital += project_profit
        else:
            break


    return -current_capital

print(findMaximizedCapital(3, 0, [1,2,3], [0,1,2]))
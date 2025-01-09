import sys
from collections import defaultdict
import heapq

def dijkstra(N, graph, start, end):
    costs = [float('inf')] * (N+1)
    costs[start] = 0
    que = [(start, 0)]

    while que:
        cur_node, cur_cost = heapq.heappop(que)
        if cur_cost > costs[cur_node]:
            continue

        for nei_node, nei_cost in graph[cur_node]:
            new_cost = nei_cost + cur_cost
            if new_cost < costs[nei_node]:
                costs[nei_node] = new_cost
                heapq.heappush(que, (nei_node, new_cost))

    return costs[end]


data = sys.stdin.read().splitlines()
N = int(data[0])
M = int(data[1])

graph = defaultdict(list)

for buses in data[2:-1]:
    u, v, cost = map(int, buses.split())
    graph[u].append((v, cost))

start, end = map(int, data[-1].split())

end_cost = dijkstra(N, graph, start, end)

print(end_cost)
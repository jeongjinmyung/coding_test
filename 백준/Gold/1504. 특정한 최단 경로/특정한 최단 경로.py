import heapq
from collections import defaultdict
import sys


def dijkstra(start):
    visit_cost = [float('inf')] * (N + 1)
    visit_cost[start] = 0
    que = [(start, 0)]
    
    while que:
        this_node, this_cost = heapq.heappop(que)
        if this_cost > visit_cost[this_node]:
            continue

        for nei_node, nei_cost in graphs[this_node]:
            new_cost = this_cost + nei_cost
            if new_cost < visit_cost[nei_node]:
                visit_cost[nei_node] = new_cost
                heapq.heappush(que, (nei_node, new_cost))

    return visit_cost


input = sys.stdin.readline
N, E = map(int, input().split())

graphs = defaultdict(list)
for _ in range(E):
    a, b, c = map(int, input().split())
    graphs[a].append((b, c))
    graphs[b].append((a, c))
v1, v2 = map(int, input().split())

start_cost = dijkstra(1)
v1_cost = dijkstra(v1)
v2_cost = dijkstra(v2)

path1 = start_cost[v1] + v1_cost[v2] + v2_cost[N]
path2 = start_cost[v2] + v2_cost[v1] + v1_cost[N]

result = min(path1, path2)

print(result if result < float('inf') else -1)
import heapq
import sys

def dijkstra(start):
    visit_cost = [float('inf')] * (V + 1)
    visit_cost[start] = 0
    que = [(0, start)]

    while que:
        this_cost, this_node = heapq.heappop(que)
        if this_cost > visit_cost[this_node]:
            continue

        for nei_node, nei_cost in graphs[this_node]:
            new_cost = this_cost + nei_cost
            if new_cost < visit_cost[nei_node]:
                visit_cost[nei_node] = new_cost
                heapq.heappush(que, (new_cost, nei_node))

    return visit_cost

input = sys.stdin.read
data = input().split()

V, E = map(int, data[:2])
start = int(data[2])

graphs = [[] for _ in range(V + 1)]
index = 3
for _ in range(E):
    u, v, w = map(int, data[index:index+3])
    graphs[u].append((v, w))
    index += 3

costs = dijkstra(start)

sys.stdout.write("\n".join("INF" if costs[i] == float('inf') else str(costs[i]) for i in range(1, V + 1)) + "\n")
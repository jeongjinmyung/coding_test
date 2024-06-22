def solution(n, s, a, b, fares):
    import heapq
    
    def dijkstra(n, graph, start):
        distances = [float('inf')] * (n+1)
        distances[start] = 0
        que = [(0, start)]
        
        while que:
            cur_dist, cur_node = heapq.heappop(que)
            if cur_dist > distances[cur_node]:
                continue
            for adj, weight in graph[cur_node]:
                distance = cur_dist + weight
                if distance < distances[adj]:
                    distances[adj] = distance
                    heapq.heappush(que, (distance, adj))
        return distances
    
    graph = [[] for _ in range(n+1)]
    for fare in fares:
        u, v, w = fare
        graph[u].append((v, w))
        graph[v].append((u, w))
    
    dist_from_start = dijkstra(n, graph, s)
    dist_from_a = dijkstra(n, graph, a)
    dist_from_b = dijkstra(n, graph, b)
    
    total_cost = float('inf')
    for i in range(1, n+1):
        if dist_from_start[i] != float('inf') and dist_from_a[i] != float('inf') and dist_from_b[i] != float('inf'):
            cur_cost = dist_from_start[i] + dist_from_a[i] + dist_from_b[i]
            if total_cost > cur_cost:
                total_cost = cur_cost
    return total_cost
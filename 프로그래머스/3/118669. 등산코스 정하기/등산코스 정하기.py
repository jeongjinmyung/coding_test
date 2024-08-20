import collections, heapq

def solution(n, paths, gates, summits):
    graph = collections.defaultdict(list)
    for path in paths:
        graph[path[0]].append((path[1], path[2]))
        graph[path[1]].append((path[0], path[2]))
    
    intensity = [float('inf')] * (n+1)
    pq = []
    for gate in gates:
        heapq.heappush(pq, (0, gate))
        intensity[gate] = 0
    
    while pq:
        current_intensity, node = heapq.heappop(pq)
        
        if current_intensity > intensity[node]:
            continue
        if node in summits:
            continue

        for neighbor, weight in graph[node]:
            new_intensity = max(weight, current_intensity)
            if new_intensity < intensity[neighbor]:
                intensity[neighbor] = new_intensity
                heapq.heappush(pq, (new_intensity, neighbor))

    best_summit = -1
    best_intensity = float('inf')
    for summit in summits:
        if intensity[summit] < best_intensity or (intensity[summit] == best_intensity and summit < best_summit):
            best_intensity = intensity[summit]
            best_summit = summit
    return [best_summit, best_intensity]
import collections
import heapq

def solution(n, paths, gates, summits):
    # 그래프 생성
    graph = collections.defaultdict(list)
    
    for path in paths:
        graph[path[0]].append((path[1], path[2]))
        graph[path[1]].append((path[0], path[2]))
    
    intensity = [float('inf')] * (n+1)
    pq = []

    # 출입구에서 시작
    for gate in gates:
        heapq.heappush(pq, (0, gate))
        intensity[gate] = 0
    
    while pq:
        current_intensity, node = heapq.heappop(pq)
        # 인텐시티 크면 무시
        if current_intensity > intensity[node]:
            continue
        # 산봉우리 도착하면 무시
        if node in summits:
            continue

        for neighbor, weight in graph[node]:
            new_intensity = max(weight, current_intensity)
            if new_intensity < intensity[neighbor]:
                intensity[neighbor] = new_intensity
                heapq.heappush(pq, (new_intensity, neighbor))
    # 최소 산봉우리 찾기
    best_summit = -1
    best_intensity = float('inf')

    for summit in summits:
        if intensity[summit] < best_intensity or (intensity[summit] == best_intensity and summit < best_summit):
            best_summit = summit
            best_intensity = intensity[summit]

    # intensity 최소 등산코스에 있는 산봉우리, intensity 최소값
    return [best_summit, best_intensity]
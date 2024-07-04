import collections
import sys
sys.setrecursionlimit(10 ** 6) 

def bfs(p):
    start = []
    # 시작 위치 담기
    for i in range(5):
        for j in range(5):
            if p[i][j] == 'P':
                start.append([i, j])
    
    for s in start:
        que = collections.deque([s])
        visited = [[0] * 5 for _ in range(5)]
        distance = [[0] * 5 for _ in range(5)]
        visited[s[0]][s[1]] = 1

        while que:
            y, x = que.popleft()
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nx = x + dx
                ny = y + dy
                if 0<=nx<5 and 0<=ny<5 and visited[ny][nx] == 0:
                    if p[ny][nx] == 'O':
                        que.append([ny, nx])
                        visited[ny][nx] = 1
                        distance[ny][nx] = distance[y][x] + 1
                    if p[ny][nx] == 'P' and distance[y][x] <= 1:
                        return 0
    return 1

def solution(places):
    answer = []
    for p in places:
        answer.append(bfs(p))
    return answer
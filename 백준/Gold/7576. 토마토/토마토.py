from collections import deque
import sys
input = sys.stdin.readline
# n x m
m, n = map(int, input().split())

grids = [list(map(int, input().split())) for _ in range(n)]
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
def bfs():
    que = deque()
    for i in range(n):
        for j in range(m):
            if grids[i][j] == 1:
                que.append((i, j, 0))
    
    if len(que) == n * m:
        return 0

    max_days = 0
    while que:
        x, y, days = que.popleft()
        max_days = max(days, max_days)
        for dx, dy in directions:
            nx, ny = x+dx, y+dy
            if 0 <= nx < n and 0 <= ny < m and grids[nx][ny] != -1:
                if grids[nx][ny] == 0:
                    new_days = days + 1
                    grids[nx][ny] = 1
                    que.append((nx, ny, new_days))
    
    for i in range(n):
        for j in range(m):
            if grids[i][j] == 0:
                return -1
    return max_days

print(bfs())
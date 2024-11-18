from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
grids = [list(input()) for _ in range(N)]
visited = [[False] * M for _ in range(N)]

start = None
for i in range(N):
    for j in range(M):
        if grids[i][j] == "I":
           start = (i, j)

que = deque([start])
cnt = 0

while que:
    x, y = que.popleft()
    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nx, ny = x+dx, y+dy
        if 0 <= nx < N and 0 <= ny < M and grids[nx][ny] != "X":
            if not visited[nx][ny]:
                if grids[nx][ny] == "P":
                    cnt += 1
                visited[nx][ny] = True
                que.append((nx, ny))


print(cnt if cnt > 0 else "TT")
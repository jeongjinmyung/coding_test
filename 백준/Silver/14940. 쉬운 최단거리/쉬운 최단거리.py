from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
grids = [list(map(int, input().split())) for _ in range(n)]
answers = [[-1] * m for _ in range(n)]

start = None
for i in range(n):
    for j in range(m):
        if grids[i][j] == 2:
            start = (i, j)
            answers[i][j] = 0
        elif grids[i][j] == 0:
            answers[i][j] = 0

que = deque([start])

while que:
    x, y = que.popleft()
    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nx, ny = x+dx, y+dy
        if 0 <= nx < n and 0 <= ny < m and grids[nx][ny] == 1 and answers[nx][ny] == -1:
            answers[nx][ny] = answers[x][y] + 1
            que.append((nx, ny))
            
for row in answers:
    print(" ".join(map(str, row)))
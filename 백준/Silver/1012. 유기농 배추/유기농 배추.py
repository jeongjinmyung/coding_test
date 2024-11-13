from collections import deque
import sys

input = sys.stdin.readline
T = int(input())
test = dict()

for i in range(T):
    M, N, K = map(int, input().split())
    grids = [[0] * N for _ in range(M)]
    for _ in range(K):
        x, y = map(int, input().split())
        grids[x][y] = 1

    def bfs(x, y):
        que = deque([(x, y)])
        grids[x][y] = 0
        while que:
            cx, cy = que.popleft()
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nx, ny = cx + dx, cy + dy
                if 0 <= nx < M and 0 <= ny < N and grids[nx][ny] == 1:
                    grids[nx][ny] = 0
                    que.append((nx, ny))


    cnt = 0
    for i in range(M):
        for j in range(N):
            if grids[i][j] == 1:
                bfs(i, j)
                cnt += 1

    print(cnt)
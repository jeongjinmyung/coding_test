import sys
from collections import defaultdict
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N, M = map(int, input().split())
grids = defaultdict(list)
for _ in range(M):
    u, v = map(int, input().split())
    grids[u].append(v)
    grids[v].append(u)

visited = [False] * (N+1)

def dfs(node):
    visited[node] = True
    for nei in grids[node]:
        if not visited[nei]:
            dfs(nei)

cnt = 0
for i in range(1, N+1):
    if not visited[i]:
        cnt += 1
        dfs(i)

print(cnt)
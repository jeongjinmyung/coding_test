import sys
from collections import defaultdict, deque

input = sys.stdin.readline

N = int(input())
grids = defaultdict(list)

for _ in range(N-1):
    u, v = map(int, input().split())
    grids[u].append(v)
    grids[v].append(u)

parent = [0] * (N + 1)
parent[1] = 1

def dfs_stack(node):
    stack = [node]
    parent[node] = node
    while stack:
        start = stack.pop()
        for nei in grids[start]:
            if parent[nei] == 0:
                parent[nei] = start
                stack.append(nei)

dfs_stack(1)

for i in range(2, N+1):
    print(parent[i])
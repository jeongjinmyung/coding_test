from collections import defaultdict, deque

N = int(input())
M = int(input())
edges = defaultdict(list)

for i in range(M):
    f, t = map(int, input().split())
    edges[f].append(t)
    edges[t].append(f)

visited = [False] * (N+1)
visited[1] = True
que = deque([1])  # deque for bfs
cnt = 0

while que:
    cur = que.popleft()
    for nei in edges[cur]:
        if not visited[nei]:
            visited[nei] = True
            cnt += 1
            que.append(nei)

print(cnt)
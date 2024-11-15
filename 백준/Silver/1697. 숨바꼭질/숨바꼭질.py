import sys
input = sys.stdin.readline
from collections import deque

me, bro = map(int, input().split())

visited = [False] * (100000 + 1)
que = deque([(me, 0)])
visited[me] = True

while que:
    cur, time = que.popleft()
    if cur == bro:
        print(time)
        break

    for next in (cur-1, cur+1, cur * 2):
        if 0 <= next <= 100000 and not visited[next]:
            visited[next] = True
            que.append((next, time +1))
            
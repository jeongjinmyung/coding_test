from collections import deque
import sys
input = sys.stdin.readline

me, bro = map(int, input().split())

visited = [False] * (100001)
visited[me] = True
que = deque([(me, 0)])

while que:
    x, time = que.popleft()
    if x == bro:
        print(time)
        break
    for dx in [x-1, x+1, x * 2]:
        if 0<= dx <= 100000 and not visited[dx]:
            visited[dx] = True
            que.append((dx, time+1))

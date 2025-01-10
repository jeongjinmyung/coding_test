from collections import deque

def soultion(n, k):
    if n == k:
        return 0
    visited = [False] * 100001
    visited[n] = True
    que = deque([(n, 0)])
    
    while que:
        node, time = que.popleft()
        if node == k:
            return time
        
        for next_node in (node-1, node+1, node*2):
            if 0 <= next_node <= 100000 and not visited[next_node]:
                visited[next_node] = True
                if next_node == node * 2:
                    que.appendleft((next_node, time))
                else:
                    que.append((next_node, time+1))


N, K = map(int, input().split())

print(soultion(N, K))
from collections import deque

def solution(x, y, n):
    que = deque([(x, 0)])
    visited = set()
    visited.add(x)
    
    while que:
        cur, cnt = que.popleft()
        if cur == y:
            return cnt
        
        for nx in (cur + n, 2 * cur, 3 * cur):
            if nx <= y and nx not in visited:
                visited.add(nx)
                que.append((nx, cnt+1))
    return -1
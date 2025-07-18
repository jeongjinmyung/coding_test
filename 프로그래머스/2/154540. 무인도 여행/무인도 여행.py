from collections import deque

def bfs(maps:list, visited:list, x:int, y:int) -> (int, list):
    start = (x, y)
    visited[x][y] = True
    que = deque([start])
    cnt = int(maps[x][y])
    
    while que:
        x, y = que.popleft()
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x+dx, y+dy
            if 0 <= nx < len(maps) and 0 <= ny < len(maps[0]):
                if maps[nx][ny] != "X" and not visited[nx][ny]:
                    visited[nx][ny] = True
                    cnt += int(maps[nx][ny])
                    que.append((nx, ny))
    return cnt, visited


def solution(maps):
    answer = []
    visited = [[False for _ in range(len(maps[0]))] for _ in range(len(maps))]
    
    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if maps[i][j] != "X" and not visited[i][j]:
                cnt, visited = bfs(maps, visited, i, j)
                answer.append(cnt)
                
    answer = sorted(answer)
    return [-1] if answer == [] else answer
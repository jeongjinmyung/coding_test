import collections

def solution(board):
    n = len(board)
    m = len(board[0])
    
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    # 시작지점, 끝지점 확인
    start = goal = None
    for i in range(n):
        for j in range(m):
            if board[i][j] =='R':
                start = (i, j)
            elif board[i][j] == 'G':
                goal = (i, j)

    def bfs(start, goal):
        queue = collections.deque([(start[0], start[1], 0)])  # (x, y, 이동횟수)
        visited = [[False] * m for _ in range(n)]  # 방문 체크
        visited[start[0]][start[1]] = True
        
        while queue:
            x, y, cnt = queue.popleft()

            if (x, y) == goal:
                return cnt

            for i in range(4):
                nx, ny = x, y
                
                while True:
                    tx, ty = nx + dx[i], ny + dy[i]
                    if 0 <= tx < n and 0 <= ty < m and board[tx][ty] != 'D':
                        nx, ny = tx, ty
                    else:
                        break
                
                if not visited[nx][ny]:
                    visited[nx][ny] = True
                    queue.append((nx, ny, cnt + 1))

        return -1

    return bfs(start, goal)
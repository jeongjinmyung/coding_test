from collections import deque

def get_next_pos(pos, board):
    next_pos = []
    pos = list(pos)
    (x1, y1), (x2, y2) = pos
    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for dx, dy in moves:
        nx1, ny1, nx2, ny2 = x1 + dx, y1 + dy, x2 + dx, y2 + dy
        if board[nx1][ny1] == 0 and board[nx2][ny2] == 0:
            next_pos.append({(nx1, ny1), (nx2, ny2)})
    # 로봇이 가로
    if x1 == x2:
        for d in [-1, 1]:
            if board[x1 + d][y1] == 0 and board[x2 + d][y2] == 0:
                next_pos.append({(x1, y1), (x1 + d, y1)})
                next_pos.append({(x2, y2), (x2 + d, y2)})
    # 로봇이 세로
    elif y1 == y2:
        for d in [-1, 1]:
            if board[x1][y1 + d] == 0 and board[x2][y2 + d] == 0:
                next_pos.append({(x1, y1), (x1, y1 + d)})
                next_pos.append({(x2, y2), (x2, y2 + d)})
    return next_pos


def solution(board):
    n = len(board)
    new_board = [[1] * (n+2) for _ in range(n+2)]
    for i in range(n):
        for j in range(n):
            new_board[i+1][j+1] = board[i][j]
    start = {(1,1), (1,2)}
    que = deque([(start, 0)])
    visited = []
    visited.append(start)

    while que:
        pos, cost = que.popleft()
        if (n, n) in pos:
            return cost
        for next_pos in get_next_pos(pos, new_board):
            if next_pos not in visited:
                que.append((next_pos, cost + 1))
                visited.append(next_pos)
    return 0
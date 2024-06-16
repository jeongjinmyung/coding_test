import collections

def solution(board):
    move = [(0,1), (0,-1), (1,0), (-1,0)]    # 동서남북
    N = len(board)
    # 방향까지 고려
    costs = [[[float('inf')] * 4 for _ in range(N)] for _ in range(N)]
    que = collections.deque([(0, 0, 4, 0)])
    for i in range(4):
        costs[0][0][i] = 0
    
    while que:
        x, y, direction, cost = que.popleft()
        for new_direction, (dx, dy) in enumerate(move):
            new_x, new_y = x + dx, y + dy
            if 0 <= new_x < N and 0 <= new_y < N and board[new_x][new_y] == 0:
                new_cost = cost + 100
                # 방향이 바뀌면
                if direction != 4 and direction != new_direction:
                    new_cost += 500
                # 새로운 방향에서 비용이 적으면
                if new_cost < costs[new_x][new_y][new_direction]:
                    costs[new_x][new_y][new_direction] = new_cost
                    que.append((new_x, new_y, new_direction, new_cost))

    return min(costs[N-1][N-1])
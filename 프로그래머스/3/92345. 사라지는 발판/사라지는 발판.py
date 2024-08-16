visited = [[0] * 5 for _ in range(5)]
block = [[0] * 5 for _ in range(5)]
n, m = 0, 0

def solve(curx, cury, opx, opy):
    global visited, block, n, m
    if visited[curx][cury]:
        return 0
    ret = 0

    for d in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nx = curx + d[0]
        ny = cury + d[1]
        if nx < 0 or nx >= n or ny < 0 or ny >= m or visited[nx][ny] or block[nx][ny] == 0:
            continue
        visited[curx][cury] = 1    # 방문 표시

        val = solve(opx, opy, nx, ny)+1    # 다음 차례
        visited[curx][cury] = 0    # 방문 표시 해제

        if ret % 2 == 0 and val % 2 == 1:
            ret = val   # 현재 패배인데 새로 계산 시 승리인 경우 업데이트
        elif ret % 2 == 0 and val % 2 == 0:
            ret = max(ret, val)    # 현재 패배이고 새로 계산해도 패배인 경우 최대한 늦게 짐
        elif ret % 2 == 1 and val % 2 == 1:
            ret = min(ret, val)    # 현재 승리이고 새로 계산해도 승리인 경우 최대한 빨리 이김

    return ret

def solution(board, aloc, bloc):
    global n, m
    n, m = len(board), len(board[0])
    for i in range(n):
        for j in range(m):
            block[i][j] = board[i][j]
    return solve(aloc[0], aloc[1], bloc[0], bloc[1])
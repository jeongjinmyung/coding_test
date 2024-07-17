def solution(grid):
    answer = []
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]    # 상, 하, 좌, 우
    global turn_left, turn_right, row, col
    turn_left = [2, 3, 1, 0]    # 상>좌, 하>우, 좌>하, 우>상
    turn_right = [3, 2, 0, 1]   # 상>우, 하>좌, 좌>상, 우>하
    row, col = len(grid), len(grid[0])
    # 4 방향 방문 기록 리스트
    visited = [[[False] * 4 for _ in range(col)] for _ in range(row)]
    
    # 각 row를 리스트로 변형
    for i in range(row):
        grid[i] = list(grid[i])

    for c in range(row):
        for r in range(col):
            for k in range(4):    # 4방향으로
                if visited[c][r][k] != 0:    # 방문했으면 넘어감
                    continue
                cnt = cycle(visited, grid, c, r, k) - 1
                answer.append(cnt)
    answer.sort()
    return answer

def cycle(visited, grid, i, j, out):
    cnt = 1
    while visited[i][j][out] != 1:
        visited[i][j][out] = cnt
        cnt += 1
        if grid[i][j] == 'S':
            pass
        elif grid[i][j] == 'L':
            out = turn_left[out]
        else:
            out = turn_right[out]
        i, j = route(out, i, j)
    return cnt

def route(out, i, j):
    if out == 0:
        i -= 1
        if i <0:
            i = row -1
    elif out == 1:
        i += 1
        if i > row -1:
            i = 0
    elif out == 2:
        j -= 1
        if j <0:
            j = col -1
    elif out == 3:
        j += 1
        if j > col- 1:
            j = 0
    return i, j
import collections

def find_place(board, f):
    empty_board_list = []
    visited = [[False] * len(board[0]) for _ in range(len(board))]

    for i in range(len(board)):
        for j in range(len(board[0])):
            if not visited[i][j] and board[i][j] == f:  # 0은 빈칸, 1은 채워짐
                que = collections.deque([(i, j)])
                board[i][j] = f^1     # 보드 채우기
                visited[i][j] = True    # 방문 표시
                lst = [(i, j)]

                while que:
                    x, y = que.popleft()
                    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                        nx, ny = x + dx, y + dy
                        # 보드 벗어나는지 확인
                        if nx < 0 or nx >= len(board) or ny < 0 or ny >= len(board[0]):
                            continue
                        elif board[nx][ny] == f:
                            que.append((nx, ny))
                            board[nx][ny] = f^1
                            visited[nx][ny] = True
                            lst.append((nx, ny))
                empty_board_list.append(lst)
    return empty_board_list

def make_table(blocks):
    x, y = zip(*blocks)
    c, r = max(x) - min(x) + 1, max(y) - min(y) + 1
    table = [[0] * r for _ in range(c)]

    for i, j in blocks:
        i, j = i - min(x), j - min(y)
        table[i][j] = 1
    return table

def rotate(puzzle):
    rotate = [[0] * len(puzzle) for _ in range(len(puzzle[0]))]
    count = 0
    for i in range(len(puzzle)):
        for j in range(len(puzzle[0])):
            if puzzle[i][j]:
                count += 1
                # (i, j) -> (j, -i)
                rotate[j][len(puzzle) -1 -i] = puzzle[i][j]
    return rotate, count


def solution(game_board, table):
    answer = 0
    empty_blocks = find_place(game_board, 0)
    puzzles = find_place(table, 1)

    for empty in empty_blocks:
        filled = False
        table = make_table(empty)

        for puzzle_tuple in puzzles:
            if filled:
                break
            puzzle = make_table(puzzle_tuple)
            for _ in range(4):
                puzzle, count = rotate(puzzle)
                if table == puzzle:
                    answer += count
                    puzzles.remove(puzzle_tuple)
                    filled = True
                    break
    return answer
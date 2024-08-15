def solution(board, skill):
    row, col, cnt = len(board), len(board[0]), 0
    zero_board = [[0 for _ in range(col+1)] for _ in range(row+1)]
    
    for sk in skill:
        type, r1, c1, r2, c2, degree = sk[0], sk[1], sk[2], sk[3], sk[4], sk[5]
        val = -degree if type ==1 else degree
        zero_board[r1][c1] += val
        zero_board[r2+1][c2+1] += val
        zero_board[r1][c2+1] -= val
        zero_board[r2+1][c1] -= val
    for i in range(row+1):
        for j in range(col):
            zero_board[i][j+1] += zero_board[i][j]
    for j in range(col+1):
        for i in range(row):
            zero_board[i+1][j] += zero_board[i][j]
    return sum([1 for i in range(row) for j in range(col) if board[i][j] + zero_board[i][j] > 0])
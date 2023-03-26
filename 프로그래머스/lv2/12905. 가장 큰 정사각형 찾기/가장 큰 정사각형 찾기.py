def solution(board):
    m = len(board)
    n = len(board[0])
    
    for i in range(m -1):
        for j in range(n -1):
            # 정사각형 방향
            if board[i +1][j +1]:
                board[i +1][j +1] += min(board[i][j], board[i +1][j], board[i][j +1])
    k = 0
    for b in board:
        k = max(max(b),k)
        
    return k **2
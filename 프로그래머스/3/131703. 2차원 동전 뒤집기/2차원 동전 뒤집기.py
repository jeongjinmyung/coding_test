def solution(beginning, target):
    n = len(beginning)
    m = len(beginning[0])
    min_flip_count = float('inf')

    for row_flip_mask in range(1 << n):
        flipped = [[beginning[i][j] for j in range(m)] for i in range(n)]
        flip_count = 0

        # 행 뒤집기
        for i in range(n):
            if row_flip_mask & (1 << i):
                flip_count += 1
                for j in range(m):
                    flipped[i][j] = 1- flipped[i][j]

        # 열 뒤집기
        for j in range(m):
            need_flip = False
            for i in range(n):
                if flipped[i][j] != target[i][j]:
                    need_flip = True
                    break
            if need_flip:
                flip_count += 1
                for i in range(n):
                    flipped[i][j] = 1-flipped[i][j]

        if flipped == target:
            min_flip_count = min(min_flip_count, flip_count)
    return min_flip_count if min_flip_count != float('inf') else -1
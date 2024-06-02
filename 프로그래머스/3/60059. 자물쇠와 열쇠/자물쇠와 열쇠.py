def rotate_key(key):
    M = len(key)
    rotated = [[0] * M for _ in range(M)]
    for i in range(M):
        for j in range(M):
            rotated[j][M -1 - i] = key[i][j]
    return rotated

def check(new_lock, start_x, start_y, key, lock_size):
    M = len(key)
    N = lock_size

    for i in range(M):
        for j in range(M):
            new_lock[start_x + i][start_y + j] += key[i][j]

    for i in range(N):
        for j in range(N):
            if new_lock[M -1 + i][M -1 + j] != 1:
                return False
            
    return True

def solution(key, lock):
    M = len(key)
    N = len(lock)

    new_size = N + 2 * (M -1)
    new_lock = [[0] * new_size for _ in range(new_size)]

    for i in range(N):
        for j in range(N):
            new_lock[M -1 + i][M -1 + j] = lock[i][j]

    for _ in range(4):
        key = rotate_key(key)
        for x in range(new_size - M + 1):
            for y in range(new_size - M + 1):
                if check([row[:] for row in new_lock], x, y, key, N):
                    return True
    return False
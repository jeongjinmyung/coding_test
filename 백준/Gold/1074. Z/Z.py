import sys
input = sys.stdin.readline

N, r, c = map(int, input().split())

def devider(N, r, c):
    if N == 0:
        return 0
    
    size = 2 ** (N-1)
    if r < size and c < size:
        return devider(N-1, r, c)
    elif r < size and c >= size:
        return size * size + devider(N-1, r, c - size)
    elif r >= size and c < size:
        return 2 * size * size + devider(N-1, r - size, c)
    else:
        return 3 * size * size + devider(N-1, r- size, c - size)
    
print(devider(N, r, c))
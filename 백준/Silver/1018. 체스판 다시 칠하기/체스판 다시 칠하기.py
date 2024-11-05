N, M = map(int, input().split())
grid = []
for _ in range(N):
    grid.append(input())

min_paint = float('inf')

for i in range(N - 7):
    for j in range(M - 7):
        cnt1 = 0
        cnt2 = 0

        for x in range(8):
            for y in range(8):
                if (x + y) % 2 == 0:
                    if grid[i + x][j + y] != 'W':
                        cnt1 += 1
                    if grid[i + x][j + y] != 'B':
                        cnt2 += 1
                else:
                    if grid[i + x][j + y] != 'B':
                        cnt1 += 1
                    if grid[i + x][j + y] != 'W':
                        cnt2 += 1
        
        min_paint = min(cnt1, cnt2, min_paint)
print(min_paint)
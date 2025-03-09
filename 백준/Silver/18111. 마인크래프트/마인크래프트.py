import sys
from collections import Counter

N, M, B = map(int, sys.stdin.readline().split())
grounds = []
for _ in range(N):
    ground = map(int, sys.stdin.readline().split())
    grounds.extend(ground)

block_count = Counter(grounds)

min_h, max_h = min(block_count), max(block_count)
min_time = float('inf')
best_height = 0
total_block = sum(grounds) + B

for h in range(min_h, max_h+1):
    upper = sum((height - h) * count for height, count in block_count.items() if height > h)
    under = sum((h - height) * count for height, count in block_count.items() if height < h)

    if total_block >= h * N * M:
        time = upper * 2 + under
        if time < min_time or (time == min_time and h > best_height):
            min_time = time
            best_height = h


print(min_time, best_height)


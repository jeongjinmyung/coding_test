import sys
import heapq
data = sys.stdin.read().splitlines()
max_heap = []

for num in map(int, data[1:]):
    if num == 0:
        if max_heap:
            print(-heapq.heappop(max_heap))
        else:
            print(0)
    else:
        heapq.heappush(max_heap, -num)
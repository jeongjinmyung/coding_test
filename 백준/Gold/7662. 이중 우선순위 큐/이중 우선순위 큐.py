import heapq
import sys
from collections import defaultdict
input = sys.stdin.read
data = input().splitlines()

T = int(data[0])
results = []

for i in range(1, len(data)):
    if data[i].isdigit():
        k = int(data[i])
        min_heap = []
        max_heap = []
        visited = defaultdict(bool)
        idx = 0
        for j in range(i+1, i+k+1):
            command, num = data[j].split()
            num = int(num)
            if command == "I":
                heapq.heappush(min_heap, (num, idx))
                heapq.heappush(max_heap, (-num, idx))
                visited[idx] = True
                idx += 1
            elif command == "D":
                if num == 1:
                    while max_heap and not visited[max_heap[0][1]]:
                        heapq.heappop(max_heap)
                    if max_heap:
                        visited[max_heap[0][1]] = False
                        heapq.heappop(max_heap)
                elif num == -1:
                    while min_heap and not visited[min_heap[0][1]]:
                        heapq.heappop(min_heap)
                    if min_heap:
                        visited[min_heap[0][1]] = False
                        heapq.heappop(min_heap)

        while min_heap and not visited[min_heap[0][1]]:
            heapq.heappop(min_heap)
        while max_heap and not visited[max_heap[0][1]]:
            heapq.heappop(max_heap)

        if not min_heap or not max_heap:
            results.append("EMPTY")
        else:
            results.append(f"{-max_heap[0][0]} {min_heap[0][0]}")
        i += k

sys.stdout.write("\n".join(results) + "\n")
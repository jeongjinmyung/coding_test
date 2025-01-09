import sys
input = sys.stdin.readline

N = int(input())

prev_max = [0, 0, 0]
prev_min = [0, 0, 0]

first_row = list(map(int, input().split()))
prev_max[:] = first_row
prev_min[:] = first_row

for _ in range(1, N):
    current_row = list(map(int, input().split()))
    
    current_max = [0, 0, 0]
    current_min = [0, 0, 0]

    current_max[0] = max(prev_max[0], prev_max[1]) + current_row[0]
    current_max[1] = max(prev_max[0], prev_max[1], prev_max[2]) + current_row[1]
    current_max[2] = max(prev_max[1], prev_max[2]) + current_row[2]

    prev_max[:] = current_max

    current_min[0] = min(prev_min[0], prev_min[1]) + current_row[0]
    current_min[1] = min(prev_min[0], prev_min[1], prev_min[2]) + current_row[1]
    current_min[2] = min(prev_min[1], prev_min[2]) + current_row[2]

    prev_min[:] = current_min

print(max(prev_max), min(prev_min))
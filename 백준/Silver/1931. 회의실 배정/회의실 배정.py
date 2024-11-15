import sys
input = sys.stdin.readline

N = int(input())
meetings = []

for i in range(1, N+1):
    s, e = map(int, input().split())
    meetings.append((s, e))

meetings.sort(key=lambda x: (x[1], x[0]))
cnt = 0
last_end_time = 0

for start, end in meetings:
    if start >= last_end_time:
        cnt += 1
        last_end_time = end
    
print(cnt)
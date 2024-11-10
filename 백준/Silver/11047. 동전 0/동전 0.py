N, K = map(int, input().split())
values = [int(input()) for _ in range(N)]
values = values[::-1]
cnt = 0

for value in values:
    if value > K:
        continue
    cnt += K // value
    K %= value
    
print(cnt)
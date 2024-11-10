N, M = map(int, input().split())
sites = []
target = []
for i in range(N+M):
    if i < N:
        sites.append((input().split()))
    else:
        target.append(str(input()))

table = {s:pw for s, pw in sites}

for t in target:
    print(table[t])
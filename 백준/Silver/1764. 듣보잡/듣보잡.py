import sys
N, M = map(int, input().split())

a = set()
b = set()
for i in range(N+M):
    name = sys.stdin.readline().strip()
    if i >= M:
        b.add(name)
    else:
        a.add(name)

last = a & b
last = sorted(last)
print(len(last))
print(*last, sep='\n')
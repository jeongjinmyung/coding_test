import sys
input = sys.stdin.readline

N, M = map(int, input().split())
n_list = list(map(int, input().split()))
_sum = 0
p_sum = [0]

for i in n_list:
    _sum += i
    p_sum.append(_sum)

for _ in range(M):
    s, e = map(int, input().split())
    print(p_sum[e] - p_sum[s-1])
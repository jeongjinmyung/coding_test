import sys
from itertools import combinations

input = sys.stdin.readline

N, M = map(int, input().split())

results = combinations(range(1, N+1), M)
for seq in results:
    print(" ".join(map(str, seq)))
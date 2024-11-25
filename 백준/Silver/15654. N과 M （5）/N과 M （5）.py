import sys

input = sys.stdin.readline
N, M = map(int, input().split())
n_list = list(map(int, input().split()))  # N개
n_list.sort()
results = []

def backtrack(depth):
    if depth == M:
        print(' '.join(map(str, results)))
        return

    for i in range(len(n_list)):
        if n_list[i] not in results:
            results.append(n_list[i])
            backtrack(depth+1)
            results.pop()

backtrack(0)
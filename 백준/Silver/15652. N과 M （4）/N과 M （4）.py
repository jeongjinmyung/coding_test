import sys


def backtrack(start:int, depth:int, temp:list):
    if depth == M:
        print(" ".join(map(str, temp)))
        return

    for i in range(start, N+1):
        temp.append(str(i))
        backtrack(i, depth+1, temp)
        temp.pop()

N, M = map(int, input().split())
backtrack(1, 0, [])
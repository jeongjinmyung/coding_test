import sys


def backtrack(num_list:list, depth:int, temp:list, start:int):
    """
    N개의 자연수 중에서 M개를 고른 수열
    같은 수를 여러 번 골라도 된다.
    고른 수열은 비내림차순이어야 한다
    """
    if depth == M:
        print(" ".join(map(str, temp)))
        return

    for i in range(start, len(num_list)):
        temp.append(num_list[i])
        backtrack(num_list, depth+1, temp, i)
        temp.pop()

N, M = map(int, input().split())
num_list = list(set(map(int, input().split())))
num_list.sort()
backtrack(num_list, 0, [], 0)
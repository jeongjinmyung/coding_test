import sys
input = sys.stdin.readline

N = int(input())
num_list = [int(input()) for _ in range(N)]

num_list.sort()

print(*num_list, sep='\n')
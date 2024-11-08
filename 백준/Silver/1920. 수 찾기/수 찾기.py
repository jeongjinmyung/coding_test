import sys
input = sys.stdin.readline

N = int(input())
a_list = list(map(int, input().split()))
M = int(input())
b_list = list(map(int, input().split()))

a_list.sort()

def is_in(n: int, target: list) -> bool:
    left, right = 0, len(target)-1
    
    while left <= right:
        mid = (left + right) // 2
        if n == target[mid]:
            return True
        elif n > target[mid]:
            left = mid + 1
        elif n < target[mid]:
            right = mid -1
    
    return False

for i in range(M):
    if is_in(b_list[i], a_list):
        print(1)
    else:
        print(0)
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
trees = list(map(int, input().split()))

def get_trees(height):
    total = 0
    for tree in trees:
        if tree >= height:
            total += tree - height
    return total

left = 1
right = max(trees)

while left <= right:
    mid = (right + left) // 2
    total = get_trees(mid)
    if total >= M:
        left = mid +1
    else:
        right = mid -1

print(right)
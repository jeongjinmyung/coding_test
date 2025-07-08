import sys
import math

def isInside(x: int, y: int, cx: int, cy: int, r: int) -> bool:
    return math.hypot(x - cx, y - cy) < r

def solution(x1:int, y1:int, x2:int, y2 :int, areas: list) -> int:
    cnt = 0
    for cx, cy, r in areas:
        start_inside = isInside(x1, y1, cx, cy, r)
        end_inside = isInside(x2, y2, cx, cy, r)
        if start_inside != end_inside:
            cnt += 1
    return cnt

T = int(sys.stdin.readline())

for _ in range(T):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    n = int(sys.stdin.readline())
    areas = [tuple(map(int, sys.stdin.readline().split())) for _ in range(n)]
    print(solution(x1, y1, x2, y2, areas))
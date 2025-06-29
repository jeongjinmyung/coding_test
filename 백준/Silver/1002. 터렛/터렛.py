import sys, math

def getPositions(x1:int, y1:int, r1:int,
                 x2:int, y2:int, r2:int) -> int:
    dx = x2 - x1
    dy = y2 - y1
    distance = math.hypot(dx, dy)

    if distance == 0:
        if r1 == r2:
            return -1
        else:
            return 0
    elif distance > r1 + r2:
        return 0
    elif distance == r1 + r2:
        return 1
    elif abs(r1 - r2) < distance < (r1 + r2):
        return 2
    elif distance == abs(r1 - r2):
        return 1
    else:
        return 0


def main():

    T = int(sys.stdin.readline())
    
    for i in range(T):
        x1, y1, r1, x2, y2, r2 = map(int, sys.stdin.readline().split())
        result = getPositions(x1, y1, r1, x2, y2, r2)
        print(result)

if __name__ == "__main__":
    main()

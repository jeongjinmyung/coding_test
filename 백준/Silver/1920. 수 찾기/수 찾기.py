n = int(input())
smpl = list(map(int,input().split()))

m = int(input())
comp = list(map(int,input().split()))

smpl.sort()

def bisearch(num, target):
    start = 0
    end = n -1
    
    while start <= end:
        mid = (start + end) // 2
        if num[mid] == target:
            return 1
        elif num[mid] > target:
            end = mid -1
        elif num[mid] < target:
            start = mid + 1
    return 0

for t in comp:
    print(bisearch(smpl, t))
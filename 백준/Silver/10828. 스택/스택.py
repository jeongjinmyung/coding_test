import sys

n = int(sys.stdin.readline())
arr = []

for _ in range(n):
    word = sys.stdin.readline().split()
    order = word[0]

    if order == 'push':
        arr.append(word[1])
    elif order == 'pop':
        if arr == []:
            print(-1)
        else:
            print(arr.pop())
    elif order == 'size':
        print(len(arr))
    elif order == 'empty':
        if arr == []:
            print(1)
        else:
            print(0)
    elif order == 'top':
        if arr == []:
            print(-1)
        else:
            print(arr[-1])
        
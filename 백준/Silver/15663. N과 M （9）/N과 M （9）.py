import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = sorted(list(map(int, input().split())))
visited = [False] * N
path = []

def backtrack():
    if len(path) == M:
        print(" ".join(map(str, path)))
        return
    
    temp = 0
    for i in range(N):
        if not visited[i] and temp != arr[i]:
            visited[i] = True
            path.append(arr[i])
            temp = arr[i]
            backtrack()
            visited[i] = False
            path.pop()

backtrack()
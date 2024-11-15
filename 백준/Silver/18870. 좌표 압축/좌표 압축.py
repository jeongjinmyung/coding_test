import sys
input = sys.stdin.readline

N = int(input())
x_list = list(map(int, input().split()))

x = sorted(list(set(x_list)))

mapping = {}
for i, v in enumerate(x):
    mapping[v] = i

ans = []
for xl in x_list:
    ans.append(mapping[xl])

print(" ".join(map(str, ans)))
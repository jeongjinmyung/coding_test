N = int(input())
data = []
for _ in range(N):
    x, y = map(int, input().split())
    data.append((x, y))

sorted_data = sorted(data, key=lambda x: (x[0], x[1]))
for x, y in sorted_data:
    print(x, y)
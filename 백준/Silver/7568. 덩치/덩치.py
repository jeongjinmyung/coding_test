import sys

input = sys.stdin.read
data = input().split()
N = int(data[0])

sizes = []
for i in range(1, len(data), 2):
    W, H = map(int, data[i:i+2])
    sizes.append((W, H))

rating = []
for i in range(len(sizes)):
    cnt = 0
    my_weight, my_height = sizes[i]
    for j in range(len(sizes)):
        if i != j:
            other_weight, other_height = sizes[j]
            if my_weight < other_weight and my_height < other_height:
                cnt += 1
    rating.append(cnt + 1)

sys.stdout.write(" ".join(map(str, rating)) + "\n")
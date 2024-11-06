lines = []

while True:
    tri = list(map(int, input().split()))
    if tri[0] == 0 and tri[1] == 0 and tri[2] == 0:
        break
    lines.append(tri)

for line in lines:
    line.sort()
    if line[0] **2 + line[1] ** 2 == line[2] ** 2:
        print("right")
    else:
        print("wrong")
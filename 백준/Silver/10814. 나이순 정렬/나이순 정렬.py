N = int(input())
mem = []
for _ in range(N):
    age, name = map(str, input().split())
    mem.append((int(age), name))

sorted_member = sorted(mem, key=lambda x: x[0])
for age, name in sorted_member:
    print(age, name)
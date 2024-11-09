N = map(int, input())
lines = list(map(int, input().split()))

spend = 0
total = 0
lines.sort()

for i in lines:
    spend += i
    total += spend
print(total)
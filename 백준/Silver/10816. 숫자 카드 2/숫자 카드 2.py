from collections import Counter

N = int(input())
cards = list(map(int, input().split()))
M = int(input())
sang = list(map(int, input().split()))

counter = Counter(cards)
strings = []
for num in sang:
    strings.append(str(counter[num]))

print(*strings)
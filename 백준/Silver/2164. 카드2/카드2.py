from collections import deque

N = int(input())
deck = deque(range(1, N+1))

while len(deck) != 1:
    deck.popleft()
    deck.rotate(-1)

print(deck[0])
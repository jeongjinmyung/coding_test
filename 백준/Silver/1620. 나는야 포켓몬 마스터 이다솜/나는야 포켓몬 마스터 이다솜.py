import sys

read = sys.stdin.readline
N, M = map(int, read().split())

pokemon_dict = {}
for i in range(1, N+1):
    name = read().strip()
    pokemon_dict[i] = name
    pokemon_dict[name.lower()] = i

for _ in range(M):
    query = read().strip()
    if query.isdigit():
        print(pokemon_dict[int(query)])
    else:
        print(pokemon_dict[query.lower()])
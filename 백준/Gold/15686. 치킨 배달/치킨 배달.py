from itertools import combinations
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
grids = [list(map(int, input().split())) for _ in range(N)]

houses = []
stores = []

for i in range(N):
    for j in range(N):
        if grids[i][j] == 1:
            houses.append((i, j))
        elif grids[i][j] == 2:
            stores.append((i, j))

def calc_city_distance(valid_store):
    total = 0
    for h_x, h_y in houses:
        min_distance = float('inf')
        for s_x, s_y in valid_store:
            min_distance = min(min_distance, (abs(h_x - s_x) + abs(h_y - s_y)))
        total += min_distance
    return total

min_city_distance = float('inf')
for valid_store in combinations(stores, M):
    city_distance = calc_city_distance(valid_store)
    min_city_distance = min(min_city_distance, city_distance)

print(min_city_distance)
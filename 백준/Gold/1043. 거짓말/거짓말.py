from collections import deque
import sys
input = sys.stdin.readline

def find(parents, x):
    if parents[x] != x:
        parent[x] = find(parents, parents[x])
    return parent[x]

def union(parent, rank, x, y):
    root_x = find(parent, x)  # x의 루트 찾기
    root_y = find(parent, y)  # y의 루트 찾기

    if root_x != root_y:  # 둘의 루트가 다를 경우 병합
        if rank[root_x] > rank[root_y]:  # x의 트리가 더 크다면
            parent[root_y] = root_x  # y의 루트를 x의 루트 아래에 붙임
        elif rank[root_x] < rank[root_y]:  # y의 트리가 더 크다면
            parent[root_x] = root_y  # x의 루트를 y의 루트 아래에 붙임
        else:
            parent[root_y] = root_x
            rank[root_x] += 1  

N, M = map(int, input().split())
list_of_truth_teller = list(map(int, input().split()))
nums_of = list_of_truth_teller[0]
truth_teller = list_of_truth_teller[1:]
parties = []

for _ in range(M):
    people = list(map(int, input().split()))
    parties.append(people[1:]) 

parent = [i for i in range(N+1)]
rank = [0] * (N+1)

for i in range(1, len(truth_teller)):
    union(parent, rank, truth_teller[0], truth_teller[i])

for party in parties:
    for i in range(1, len(party)):
        union(parent, rank, party[0], party[i])

truth_root = set(find(parent, person) for person in truth_teller)

max_lie = 0
for party in parties:
    if all(find(parent, person) not in truth_root for person in party):
        max_lie += 1

print(max_lie)
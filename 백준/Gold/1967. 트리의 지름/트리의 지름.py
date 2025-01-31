import sys
sys.setrecursionlimit(10 ** 6)
from collections import defaultdict


def dfs(node, accumulated_weight):
    visited[node] = True
    
    global max_distance, farthest_node
    if accumulated_weight > max_distance:
        max_distance = accumulated_weight
        farthest_node = node
    
    for nei, weight in trees[node]:
        if not visited[nei]:
            dfs(nei, accumulated_weight + weight)

input = sys.stdin.read()
data = input.split()
n_nodes = int(data[0])
trees = defaultdict(list)

for i in range(1, len(data), 3):
    parent, child, weight = map(int, data[i:i+3]) 
    trees[parent].append((child, weight))
    trees[child].append((parent, weight))

visited = [False] * (n_nodes + 1)
max_distance, farthest_node = 0, 0
dfs(1, 0)
visited = [False] * (n_nodes + 1)
max_distance = 0
dfs(farthest_node, 0)

sys.stdout.write(str(max_distance) + "\n")
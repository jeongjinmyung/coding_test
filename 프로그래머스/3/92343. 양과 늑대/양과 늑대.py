import collections

def solution(info, edges):
    def dfs(current_node, sheep_count, wolf_count, next_nodes):
        nonlocal max_sheep, animal_tree
        if info[current_node] == 0:
            sheep_count += 1
        else:
            wolf_count += 1
        if wolf_count >= sheep_count:
            return
        
        max_sheep = max(max_sheep, sheep_count)
        
        for child in animal_tree[current_node]:
            next_nodes.append(child)
        for i, next_node in enumerate(next_nodes):
            dfs(next_node, sheep_count, wolf_count, next_nodes[:i]+next_nodes[i+1:])
    
    
    animal_tree = collections.defaultdict(list)
    for parent, child in edges:
        animal_tree[parent].append(child)
    
    max_sheep = 0
    dfs(0, 0, 0, [])
    return max_sheep
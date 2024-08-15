import collections

def solution(info, edges):
    def dfs(current_node, sheep_cnt, wolf_cnt, next_nodes):
        nonlocal max_sheep, edges_dict

        if info[current_node] == 0:    # 양이면
            sheep_cnt += 1
        else:
            wolf_cnt += 1
        
        if wolf_cnt >= sheep_cnt:    # 잡아먹히면 끝
            return
        
        max_sheep = max(sheep_cnt, max_sheep)

        for child in edges_dict[current_node]:
            next_nodes.append(child)
        
        for i, next_node in enumerate(next_nodes):
            dfs(next_node, sheep_cnt, wolf_cnt, next_nodes[:i]+next_nodes[i+1:])

    edges_dict = collections.defaultdict(list)
    for parent, child in edges:
        edges_dict[parent].append(child)
    
    max_sheep = 0
    dfs(0, 0, 0, [])

    return max_sheep
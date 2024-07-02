def solution(a, edges):
    from collections import defaultdict
    import sys
    sys.setrecursionlimit(300000)
    if sum(a) != 0:
        return -1
    
    tree = defaultdict(list)
    for u, v in edges:
        tree[u].append(v)
        tree[v].append(u)
        
    visited = [False] * len(a)
    
    def dfs(node):
        visited[node] = True
        total_move =0
        for nei in tree[node]:
            if not visited[nei]:
                total_move += dfs(nei)
                a[node] += a[nei]
                total_move += abs(a[nei])
                a[nei] = 0
        return total_move
    
    return dfs(0)
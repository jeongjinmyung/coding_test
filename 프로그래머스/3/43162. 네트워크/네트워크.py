def solution(n, computers):
    answer = 0
    visited = [False] * n
    
    def dfs(node):
        if visited[node] == False:
            visited[node] = True
        
        for c in range(n):
            if visited[c] == False and computers[node][c] == 1:
                dfs(c)
    
    for i in range(n):
        if visited[i] == False:
            dfs(i)
            answer += 1
    return answer
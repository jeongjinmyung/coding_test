from collections import defaultdict
import sys
sys.setrecursionlimit(1000001)

def solution(n, lighthouse):
    # 그래프 생성
    graph = defaultdict(list)
    for a, b in lighthouse:
        graph[a].append(b)
        graph[b].append(a)

    # DP 테이블
    dp = [[0, 0] for _ in range(n+1)]
    visited = [False] * (n+1)

    def dfs(node):
        visited[node] = True
        dp[node][0] = 0  # 현재 노드를 끄는 경우
        dp[node][1] = 1  # 현재 노드를 켜는 경우

        for neighbor in graph[node]:
            if not visited[neighbor]:
                dfs(neighbor)
                # 현재 노드를 끄는 경우, 자식 노드 중 하나는 켜져 있어야 함
                dp[node][0] += dp[neighbor][1]
                # 현재 노드를 켜는 경우, 자식 노드는 꺼져도 상관 없음
                dp[node][1] += min(dp[neighbor][0], dp[neighbor][1])
    dfs(1)  # 루트 노드에서 dfs 실행
    return min(dp[1][0], dp[1][1])
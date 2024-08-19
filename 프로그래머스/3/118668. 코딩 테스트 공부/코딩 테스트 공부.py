def solution(alp, cop, problems):
    # 목표 알고력, 코딩력 채우기
    max_alp = max(max([p[0] for p in problems]), 0)
    max_cop = max(max([p[1] for p in problems]), 0)

    # alp와 cop가 목표보다 크거나 같으면 목표치로 맞춤
    alp = min(alp, max_alp)
    cop = min(cop, max_cop)

    # dp 테이블. i 알고력 j 코딩력을 도달하는 최단시간
    dp = [[float('inf')] * (max_cop + 1) for _ in range(max_alp + 1)]
    dp[alp][cop] = 0

    for i in range(alp, max_alp +1):
        for j in range(cop, max_cop+1):
            # 알고력 1 증가
            if i < max_alp:
                dp[i+1][j] = min(dp[i+1][j], dp[i][j]+1)
            # 코딩력 1 증가
            if j < max_cop:
                dp[i][j+1] = min(dp[i][j+1], dp[i][j]+1)
            # 각 문제 풀기
            for alp_req, cop_req, alp_rwd, cop_rwd, cost in problems:
                if i>= alp_req and j>= cop_req:
                    new_alp = min(max_alp, i+alp_rwd)
                    new_cop = min(max_cop, j+cop_rwd)
                    dp[new_alp][new_cop] = min(dp[new_alp][new_cop], dp[i][j]+cost)

    return dp[max_alp][max_cop]
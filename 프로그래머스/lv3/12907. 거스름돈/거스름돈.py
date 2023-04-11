def solution(n, money):
    dp = [0] * (n+1)
    for m in money:
        dp[m] += 1
        for n in range(m+1, n+1):
            dp[n] += dp[n-m]
    return dp[n]
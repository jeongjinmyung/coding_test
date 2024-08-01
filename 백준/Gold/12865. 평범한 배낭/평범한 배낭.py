import sys
input = sys.stdin.readline

n, k = map(int, input().split())
items = [list(map(int, input().split())) for _ in range(n)]

dp = [[0] * (k + 1) for _ in range(n+1)]

for i in range(1, n+1):
    weight, value = items[i-1]
    for w in range(k + 1):
        if w >= weight:
# 포함하지 않는 경우, 포함하는 경우
            dp[i][w] = max(dp[i-1][w], dp[i-1][w-weight]+value)
        else:
            dp[i][w] = dp[i-1][w]
print(dp[n][k])
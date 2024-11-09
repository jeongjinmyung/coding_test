N = int(input())

dp = [0] * (N + 1)

for i in range(2 , N+1):
    dp[i] = dp[i-1] + 1  # 이전 값에서 1을 뺀 기본 연산

    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i // 2]+1)  # 2로 나눈 이전 값에서 1회 추가(X2)
    
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i // 3]+1)  # 3으로 나눈 이전 값에서 1회 추가(X3)
    
print(dp[N])
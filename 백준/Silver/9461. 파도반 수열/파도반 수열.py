T = int(input())
for i in range(T):
    N = int(input())
    dp = [0, 1, 1, 1, 2, 2]

    if N <= 5:
        print(dp[N])
        continue
    
    for j in range(6, N+1):
        dp.append(dp[j-5] + dp[j-1])

    print(dp[N])
import sys

input = sys.stdin.readline

N = int(input())
stairs = [0] * 301
for i in range(1, N+1):
    stairs[i] = int(input())
    
dp = [0] * 301
dp[1] = stairs[1]
dp[2] = stairs[1] + stairs[2]
dp[3] = max(stairs[1]+stairs[3], stairs[2]+stairs[3])

for i in range(4, N+1):
    dp[i] = max(stairs[i] + stairs[i-1] + dp[i-3], stairs[i]+dp[i-2])
    
print(dp[N])
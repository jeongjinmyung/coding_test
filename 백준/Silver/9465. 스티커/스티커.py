import sys

data = sys.stdin.read().splitlines()

T = int(data[0])
results = []

line = 1
for _ in range(T):
    n = int(data[line])
    stickers = [
        list(map(int, data[line+1].split())),
        list(map(int, data[line+2].split())),
    ]
    line += 3

    if n == 1:
        results.append(max(stickers[0][0], stickers[1][0]))
        continue

    dp = [[0] * n for _ in range(2)]
    dp[0][0] = stickers[0][0]
    dp[1][0] = stickers[1][0]
    dp[0][1] = stickers[1][0] + stickers[0][1]
    dp[1][1] = stickers[0][0] + stickers[1][1]

    for i in range(2, n):
        dp[0][i] = max(dp[1][i-1], dp[1][i-2]) + stickers[0][i]
        dp[1][i] = max(dp[0][i-1], dp[0][i-2]) + stickers[1][i]
    
    results.append(max(dp[0][-1], dp[1][-1]))

for result in results:
    print(result)
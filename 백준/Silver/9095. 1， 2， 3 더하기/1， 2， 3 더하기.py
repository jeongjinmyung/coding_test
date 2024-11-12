T = int(input())
n_list = list(int(input()) for _ in range(T))

def finder(num):
    if num == 1:
        return 1
    elif num == 2:
        return 2
    elif num == 3:
        return 4
    else:
        dp = [0] * num
        dp[0] = 1
        dp[1] = 2
        dp[2] = 4

        for i in range(3, num):
            dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
    
    return dp[-1]

for n in n_list:
    cnt = finder(n)
    print(cnt)
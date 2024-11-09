T = int(input())
nums = [int(input()) for _ in range(T)]

def fibo_counter():
    n = 40
    count_0 = [0] * (n+1)
    count_1 = [0] * (n+1)

    count_0[0] = 1
    count_1[0] = 0
    count_0[1] = 0
    count_1[1] = 1

    for i in range(2, n+1):
        count_0[i] = count_0[i-1] + count_0[i-2]
        count_1[i] = count_1[i-1] + count_1[i-2]

    return count_0, count_1

for num in nums:
    count_0, count_1 = fibo_counter()
    print(count_0[num], count_1[num])
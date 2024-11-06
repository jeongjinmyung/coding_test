import math

n = int(input())
num_list = list(map(int, input().split()))

prime_cnt = 0

def is_prime(num):
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False

    for i in range(5, int(math.sqrt(num))+1, 6):
        if num % i == 0 or num % (i+2) == 0:  # 5, 7
            return False
    return True

for num in num_list:
    if is_prime(num):
        prime_cnt += 1
print(prime_cnt)
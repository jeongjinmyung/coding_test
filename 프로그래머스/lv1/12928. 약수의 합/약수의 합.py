import math
def solution(n):
    answer = 0
    div = math.ceil(n ** (1/2))
    for i in range(1, div):
        if n % i == 0:
            v = n // i
            answer += i
            answer += v
    if (div ** 2) == n:
        answer += div
    return answer
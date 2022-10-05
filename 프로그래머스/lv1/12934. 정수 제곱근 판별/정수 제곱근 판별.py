def solution(n):
    answer = 0
    div = round(n ** (1/2))
    if (div ** 2) == n:
        answer = (div + 1) ** 2
    else:
        answer = -1
    
    return answer
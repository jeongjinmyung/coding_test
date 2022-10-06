def solution(num):
    answer = 0
    count = 0
    while not num == 1:
        if count >= 500:
            answer = -1
            return answer
            break
        if num % 2 == 0:
            num = num // 2
            count += 1
        elif num % 2 == 1:
            num = num * 3 + 1
            count += 1
    answer = count    
    return answer
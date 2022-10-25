def solution(n):
    num = [1,1]
    i = 0
    while len(num) < n:
        new = num[i] +num[i+1]
        num.append(new)
        i += 1
    answer = num.pop() % 1234567
    return answer
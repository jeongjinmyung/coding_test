def solution(n):
    answer = 0
    a = list(str(n))
    for i in a:
        i = int(i)
        answer += i
    return answer
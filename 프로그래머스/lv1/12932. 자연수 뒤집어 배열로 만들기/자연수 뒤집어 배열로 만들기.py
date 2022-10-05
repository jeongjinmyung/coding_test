def solution(n):
    answer = []
    n = list(str(n))
    for i in n[::-1]:
        i = int(i)
        answer.append(i)
    return answer
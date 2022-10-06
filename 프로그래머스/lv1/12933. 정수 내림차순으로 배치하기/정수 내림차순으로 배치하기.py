def solution(n):
    answer = 0
    n = list(str(n))
    b = n.sort(reverse=True)
    answer = "".join(n)
    answer = int(answer)
    return answer
def solution(a, b):
    answer = 0
    if b == a:
        answer = b
    elif b < a:
        b, a = a, b
        c = [a for a in range(a,b+1)]
        answer = sum(c)
    else:
        c = [a for a in range(a,b+1)]
        answer = sum(c)
    
    return answer
def solution(n):
    cnt = 0
    while True:
        cnt += 1
        if bin(n + cnt)[2:].count('1') == bin(n)[2:].count('1'):
            break            
    return n + cnt
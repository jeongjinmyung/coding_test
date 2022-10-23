def solution(a,b,n):
    
    ans = 0
    remained = 0
    cola = 0
    
    while n >= a:
        cola = n //a * b
        remained = n % a
        n = cola + remained
        ans += cola
        
    return ans 
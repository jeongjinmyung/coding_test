import sys

N = int(input())

def solution(number):
    count = 0
    num = 666
    
    while True:
        if '666' in str(num):
            count += 1
        if count == number:
            return num
        num += 1


print(solution(N))
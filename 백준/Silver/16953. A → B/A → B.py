import sys

A, B = map(int, input().split())


def a_to_b(a, b):
    operations = 0
    while b > a:
        if b % 2 == 0:
            b //= 2
        elif b % 10 == 1:
            b //= 10
        else:
            return -1
        
        operations += 1
    
    return operations + 1 if b == a else -1

print(a_to_b(A, B))
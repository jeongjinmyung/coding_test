def comprod(arr):
    temp = 1
    for i in arr:
        temp *= i
    return temp

def solution(n, m):
    smaller = n if n <= m-n else m-n
    m_acc = comprod(range(m, m-n, -1))
    n_acc = comprod(range(n, 1, -1))
    return int(m_acc / n_acc)


T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    result = solution(N, M)
    print(result)
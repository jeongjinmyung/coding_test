def solution(sizes):
    a = []
    b = []
    for i, j in sizes:
        if i >= j:
            a.append(i)
            b.append(j)
        elif j <= j:
            a.append(j)
            b.append(i)
    return max(a) * max(b)
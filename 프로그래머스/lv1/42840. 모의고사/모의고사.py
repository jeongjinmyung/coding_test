def solution(answers):
    user = [[1, 2, 3, 4, 5], [2, 1, 2, 3, 2, 4, 2, 5], [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]
    s = [0] * len(user)
    for i, j in enumerate(answers):
        for k, l in enumerate(user):
            if j == l[i % len(l)]:
                s[k] += 1
    return [i +1 for i, v in enumerate(s) if v == max(s)]
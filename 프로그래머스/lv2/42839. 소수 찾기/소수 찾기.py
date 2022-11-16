from itertools import permutations

def solution(numbers):
    answer = []
    numbers = [n for n in numbers]
    temp = []

    for i in range(1, len(numbers) +1):
        temp += list(permutations(numbers, i))
    new = [int("".join(t)) for t in temp]

    for n in new:
        if n < 2:
            continue
        chk = True
        for i in range(2, int(n ** 0.5) +1):
            if n % i == 0:
                chk = False
                break
        if chk:
            answer.append(n)

    return len(set(answer))
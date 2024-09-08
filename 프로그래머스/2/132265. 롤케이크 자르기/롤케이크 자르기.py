import collections

def solution(topping):
    answer = 0
    topping_count = collections.Counter(topping)
    td = set()

    for t in topping:
        topping_count[t] -= 1
        td.add(t)
        if topping_count[t] == 0:
            topping_count.pop(t)
        if len(topping_count) == len(td):
            answer += 1

    return answer
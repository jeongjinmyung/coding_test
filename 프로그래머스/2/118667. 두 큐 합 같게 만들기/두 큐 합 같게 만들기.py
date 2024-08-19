from collections import deque

"""
pop과 insert를 합쳐서 1회
"""
def solution(queue1, queue2):
    queue1 = deque(queue1)
    queue2 = deque(queue2)
    sum1, sum2 = sum(queue1), sum(queue2)
    cnt = 0

    for _ in range(300000):
        if sum1 == sum2:
            return cnt
        elif sum1 >= sum2:
            common = queue1.popleft()
            queue2.append(common)
            sum1 -= common
            sum2 += common
            cnt += 1
        else:
            common = queue2.popleft()
            queue1.append(common)
            sum1 += common
            sum2 -= common
            cnt += 1
    return -1
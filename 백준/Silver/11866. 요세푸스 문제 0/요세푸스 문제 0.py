from collections import deque

N, K = map(int, input().split())

num_list = deque(range(1, N+1))
K = K-1
answer = []
while len(num_list) != 0:
    num_list.rotate(-K)
    out = num_list.popleft()
    answer.append(out)

print("<" + ', '.join(map(str, answer)) + ">")
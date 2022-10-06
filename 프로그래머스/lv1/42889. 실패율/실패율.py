def solution(N, stages):
    answer = []
    len_stages = len(stages)
    failure = {}
    for i in range(1, N + 1):
        if len_stages == 0:
            failure[i] = 0
        else:
            failure[i] = stages.count(i) / len_stages
            len_stages -= stages.count(i)
    answer = sorted(failure, key = lambda i : failure[i], reverse=True)
    return answer
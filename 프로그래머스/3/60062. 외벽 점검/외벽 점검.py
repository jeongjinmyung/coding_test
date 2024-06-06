from itertools import permutations

def solution(n, weak, dist):
    weak_size = len(weak)
    min_cnt = float('inf')
    weak = weak + [n + w for w in weak]


    for start in range(weak_size):
        for d in permutations(dist, len(dist)):    
            cnt = 1
            pos = start
            for i in range(1, weak_size):
                next_pos = start + i
                diff = weak[next_pos] - weak[pos]
                if diff > d[cnt -1]:
                    pos = next_pos
                    cnt += 1
                    if cnt > len(dist):
                        break
            if cnt <= len(dist):
                min_cnt = min(min_cnt, cnt)
    if min_cnt == float('inf'):
        return -1
    return min_cnt
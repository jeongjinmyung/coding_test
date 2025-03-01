import itertools
import collections

def solution(orders, course):
    answer = []
    for k in course:
        candidates =[]
        for menu_li in orders:
            for li in itertools.combinations(menu_li, k):
                res = ''.join(sorted(li))
                candidates.append(res)
        sorted_candidates = collections.Counter(candidates).most_common()
        answer += [menu for menu, cnt in sorted_candidates if cnt > 1 and cnt == sorted_candidates[0][1]]
    return sorted(answer)
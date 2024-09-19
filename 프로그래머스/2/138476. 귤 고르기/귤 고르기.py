from collections import Counter
def solution(k, tangerine):
    tan_count = Counter(tangerine)
    result = []
    tan_count = tan_count.most_common()
    for size, val in tan_count:
        if k > 0:
            result.append(size)
            k -= val

    return len(result)
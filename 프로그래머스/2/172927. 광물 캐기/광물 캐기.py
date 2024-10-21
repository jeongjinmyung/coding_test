import collections 

def solution(picks, minerals):
    available = 5 * sum(picks)
    if len(minerals) > available:
        minerals = minerals[:available]

    loader = []
    for i in range(0, len(minerals), 5):
        cnt = collections.Counter(minerals[i:i+5])
        loader.append((cnt['diamond'], cnt['iron'], cnt['stone']))

    loader.sort(reverse=True)
    
    total_fatigue = 0
    for n_dia, n_iron, n_stone in loader:
        if picks[0] > 0:
            total_fatigue += (1 * n_dia) + (1 * n_iron) + (1 * n_stone)
            picks[0] -= 1
        elif picks[1] > 0:
            total_fatigue += (5 * n_dia) + (1 * n_iron) + (1 * n_stone)
            picks[1] -= 1
        elif picks[2] > 0:
            total_fatigue += (25 * n_dia) + (5 * n_iron) + (1 * n_stone)
            picks[2] -= 1
        else:
            break
    return total_fatigue
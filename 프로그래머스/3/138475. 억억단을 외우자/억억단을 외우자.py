import sys
sys.setrecursionlimit(10 ** 6)

def solution(e, starts):
    # 각 수가 몇 번 등장할지 계산
    counts = [0] * (e + 1)
    # 각 수의 약수 개수를 카운트
    for i in range(2, e+1):
        for j in range(i, e+1, i):
            counts[j] += 1
    # i 부터 e까지 범위에서 가장 많이 등장하는 수 저장
    max_counts = [0] * (e + 1)
    # e 등장 초기화
    max_counts[e] = e
    # e 등장 수를 역순으로 계산
    for i in range(e-1, min(starts)-1, -1):
        if counts[max_counts[i+1]] <= counts[i]:
            max_counts[i] = i
        else:
            max_counts[i] = max_counts[i+1]
    
    result = []
    for s in starts:
        result.append(max_counts[s])
    return result
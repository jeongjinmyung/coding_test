def solution(n, k, enemy):
    import heapq
    N = len(enemy)

    heap = []
    for i in range(N):
        # 최대 힙으로 적 수 추가
        heapq.heappush(heap, -enemy[i])
        n -= enemy[i]
        
        if n < 0:
            if k > 0:
                n += -heapq.heappop(heap)
                k -= 1
            else:
                return i
    return N
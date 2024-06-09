def solution(stones, k):
    def can_cross(mid):
        skips = 0
        for s in stones:
            if s - mid <0:
                skips += 1
                if skips >= k:
                    return False
            else:
                skips = 0
        return True
    
    left, right = 1, max(stones)
    ans = left 
    while left <= right:
        mid = (left + right) // 2
        if can_cross(mid):
            ans = mid
            left = mid + 1
        else:
            right = mid -1
    return ans
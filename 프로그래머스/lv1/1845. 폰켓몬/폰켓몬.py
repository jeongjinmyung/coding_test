from collections import Counter
def solution(nums):
    answer = 0
    max_limit = len(nums) // 2
    mons = set(nums)
    
    if len(mons) <= max_limit:
        answer = len(mons)
    else:
        answer = max_limit
    
    return answer
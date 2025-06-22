def solution(nums):
    answer = 0

    maxLimit = len(nums) // 2
    numsOfMonsters = len(set(nums))

    if maxLimit <= numsOfMonsters:
        answer = maxLimit
    else:
        answer = numsOfMonsters
    
    return answer
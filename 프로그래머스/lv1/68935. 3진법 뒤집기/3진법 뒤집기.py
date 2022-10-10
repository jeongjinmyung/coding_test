def solution(n):
    answer = 0
    nums = []
    while n > 0:
        q = n % 3
        nums.append(q)
        n = n // 3
    nums.reverse()
    for i in range(len(nums)):
        answer += (3 ** i) * nums[i]
    return answer
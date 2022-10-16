import math
from itertools import combinations

def solution(nums):
    
    def isprime(num):
        if num == 0 or num == 1:
            return False
        for i in range(2,int(math.sqrt(num)) +1):
            if num % i == 0:
                return False
        return True
    
    answer = 0
    nums_list = list(combinations(nums,3))
    for i in nums_list:
        if isprime(sum(i)):
            answer += 1
    return answer
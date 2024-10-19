def solution(numbers):
    n = len(numbers)
    answer = [-1] * n
    stack = []
    
    for i in range(n):
        while stack and numbers[i] > numbers[stack[-1]]:
            idx = stack.pop()
            answer[idx] = numbers[i]
        stack.append(i)
    return answer
def solution(numbers):
    ans = set()
    for i in range(len(numbers) -1):
        j = i +1
        while j < len(numbers):
            ans.add(numbers[i] + numbers[j])
            j +=1
    return list(sorted(ans))
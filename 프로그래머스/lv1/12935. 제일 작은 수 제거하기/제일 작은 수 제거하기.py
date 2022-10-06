def solution(arr):
    answer = []
    arr.remove(min(arr))
    answer = arr
    if arr == []:
        answer = [-1]
    
    return answer
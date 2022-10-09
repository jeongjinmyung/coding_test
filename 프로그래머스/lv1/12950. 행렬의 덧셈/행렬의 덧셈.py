def solution(arr1, arr2):
    answer = []
    for j in range(len(arr1)):
        s = [i + v for i, v in (zip(arr1[j], arr2[j]))]
        answer.append(s)
    return answer
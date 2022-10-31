def solution(arr1, arr2):  
    return [[sum(a*b for a, b in zip(a_row, b_row)) for b_row in zip(*arr2)] for a_row in arr1]
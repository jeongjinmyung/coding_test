from math import gcd
from functools import reduce

def oneside_divide(num, array):
    return all(n % num != 0 for n in array)

def solution(arrayA, arrayB):
    gcdA = reduce(gcd, arrayA)
    gcdB = reduce(gcd, arrayB)
    
    result = 0
    
    if oneside_divide(gcdA, arrayB):
        result = max(result, gcdA)
        
    if oneside_divide(gcdB, arrayA):
        result = max(result, gcdB)
        
    return result
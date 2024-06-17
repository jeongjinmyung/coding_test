import collections

def solution(a):
    if not a:
        return 0
    
    count = collections.Counter(a)
    max_length = 0

    for num in count:
        if count[num] * 2 <= max_length:
            continue

        curr = 0
        i = 0

        while i < len(a) -1:
            if (a[i] == num and a[i+1] != num) or (a[i] != num and a[i+1] == num):
                curr += 2
                i += 2
            else:
                i += 1
            
            max_length = max(max_length, curr)

    return max_length
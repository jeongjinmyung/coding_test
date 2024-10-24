import sys
input=sys.stdin.readline

N = int(input())
nums = []
for _ in range(N):
    nums.append(int(input()))

def merge_sort(list_a):
    if len(list_a) < 2:
        return list_a
    
    mid = len(list_a) // 2
    low_arr = merge_sort(list_a[:mid])
    high_arr = merge_sort(list_a[mid:])
    
    merged = []
    l = r = 0
    while len(low_arr) > l and len(high_arr) > r:
        if low_arr[l] < high_arr[r]:
            merged.append(low_arr[l])
            l += 1
        else:
            merged.append(high_arr[r])
            r += 1
    # 님은 데이터 삽입
    merged += low_arr[l:]
    merged += high_arr[r:]
    
    return merged

print(*merge_sort(nums), sep="\n")
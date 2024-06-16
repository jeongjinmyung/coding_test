def solution(gems):
    gem_dict = dict()
    set_gems = set(gems)
    num_gems = len(set_gems)
    for g in set_gems:
        gem_dict[g] = 0

    l = 0
    min_len = len(gems) + 1
    answer = [0, 0]
    contained = 0
    
    for r in range(len(gems)):
        if gem_dict[gems[r]] == 0:
            contained += 1
        gem_dict[gems[r]] += 1
        
        # 다모았으면 왼쪽에서부터 제거
        while contained == num_gems:
            if r - l + 1 < min_len:
                min_len = r - l + 1
                answer = [l+1, r+1]
            gem_dict[gems[l]] -= 1
            if gem_dict[gems[l]] == 0:
                contained -= 1
            l += 1
    return answer
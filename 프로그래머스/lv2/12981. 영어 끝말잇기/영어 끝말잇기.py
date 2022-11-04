def solution(n, words):
    answer = [0, 0]
    idx = -1
    
    while idx + 1 < len(words):
        idx += 1
        if idx > 0 and words[idx-1][-1] != words[idx][0] or words[idx] in words[:idx]:
            answer = [(idx % n) + 1, idx // n + 1]
            break
    return answer
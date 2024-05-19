def solution(begin, target, words):
    from collections import deque
    
    queue = deque([(begin, 1)])
    visited = set([begin])
    
    while queue:
        word, level = queue.popleft()

        for w in words:
            if w in visited:
                continue

            diff = 0
            for i in range(len(word)):
                if word[i] != w[i]:
                    diff += 1

            if diff == 1:
                queue.append((w, level+1))
                visited.add(w)

                if w == target:
                    return level
                
    return 0
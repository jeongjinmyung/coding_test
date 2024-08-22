def solution(cards):
    answer = []
    n = len(cards)
    visited = [False] * (n+1)
    
    for v in cards:
        if not visited[v]:
            temp = []
            while v not in temp:
                temp.append(v)
                v = cards[v-1]
                visited[v] = True
            answer.append(len(temp))
    
    if answer[0] == n:
        return 0
    else:
        answer.sort(reverse=True)
        return answer[0] * answer[1]
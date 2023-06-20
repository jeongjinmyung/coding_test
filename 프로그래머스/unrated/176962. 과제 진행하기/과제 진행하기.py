def convert_to_num(time):
    if ":" not in time:
        return int(time)
    h, m = time.split(":")
    return (int(h) * 60) + int(m)

def solution(plans):
    to_do = []
    
    for title, start, time in plans:
        to_do.append((title, convert_to_num(start), convert_to_num(time)))
    
    to_do.sort(key = lambda x: x[1])
    answer = []
    stack = []
    
    # 시간 안에 과제를 끝낼 경우와 못끝낼 경우
    for i in range(len(to_do)):
        # 마지막 과제에 도달했을 경우
        if i == len(to_do) -1:
            answer.append(to_do[i][0])
            # stack에 있는것들을 뒤에서부터 answer에 넣는다
            for i in range(-1, -len(stack)-1, -1):
                answer.append(stack[i][0])
            break
        #다음 과제시간 - (현재과제시간 + 과제 진행시간)
        extra = to_do[i+1][1] - (to_do[i][1] + to_do[i][2])
        # 시간 안에 끝낼수 있는 과제가 있으면, 끝낸다
        if extra >= 0:
            answer.append(to_do[i][0])
            while stack:
                # 스택에 남은 시간보다 여분의 시간이 많은경우
                if stack[-1][1] <= extra:
                    k = stack.pop()
                    answer.append(k[0])
                    extra -= k[1]
                else:
                    stack[-1][1] -= extra
                    break
        else:
            # 다음 과제시간까지 못끝낸경우
            stack.append([to_do[i][0], -extra])
    return answer
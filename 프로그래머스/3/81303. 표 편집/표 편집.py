def solution(n, k, cmd):
    table = {i:[i-1, i+1] for i in range(n)}
    table[0] = [None, 1]
    table[n-1] = [n-2, None]
    curser = k
    stack = []
    answer = ['O'] * n

    for c in cmd:
        parts = c.split()
        if parts[0] == 'U':
            for _ in range(int(parts[1])):
                curser = table[curser][0]
        elif parts[0] == 'D':
            for _ in range(int(parts[1])):
                curser = table[curser][1]
        elif parts[0] == 'C':
            answer[curser] = 'X'
            prev, next = table[curser]
            stack.append([prev, curser, next])
            if next == None:
                curser = table[curser][0]    # prev
            else:
                curser = table[curser][1]    # next
            
            if prev == None:
                table[next][0] = None
            elif next == None:
                table[prev][1] = None
            else:
                table[next][0] = prev
                table[prev][1] = next
        elif parts[0] == 'Z':
            prev, now, next = stack.pop()
            answer[now] = 'O'
            if prev == None:
                table[next][0] = now
            elif next == None:
                table[prev][1] = now
            else:
                table[next][0] = now
                table[prev][1] = now
    return ''.join(answer)
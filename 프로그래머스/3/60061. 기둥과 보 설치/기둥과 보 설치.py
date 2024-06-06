def check_build(ans):
    for x, y, a in ans:
        # 보인 경우
        if a:
            if ([x, y-1, 0] not in ans and\
            [x+1, y-1, 0] not in ans and\
            ([x-1, y, 1] not in ans or\
            [x+1, y, 1] not in ans)):
                return False
        else:
            if y != 0 and\
            [x, y -1, 0] not in ans and\
            [x-1, y, 1] not in ans and\
            [x,y,1] not in ans:
                return False
    return True


def solution(n, build_frame):
    ans = []
    for x, y, a, b in build_frame:
        if b:
            ans.append([x, y, a])
            if not check_build(ans):
                ans.remove([x, y, a])
        else:
            ans.remove([x, y, a])
            if not check_build(ans):
                ans.append([x, y, a])
    ans.sort(key=lambda x: (x[0], x[1], x[2]))
    return ans
def solution(m, n, startX, startY, balls):
    answer = []

    def get_sym(m, n, x, y):
        # 우, 하, 좌, 상
        return [[m+(m-x), y],[x, -y],[-x, y],[x, n+(n-y)]]

    r, d, l, u = get_sym(m,n,startX,startY)


    for bx, by in balls:
        right = (r[0] - bx) ** 2 + (r[1] - by) ** 2
        down = (d[0] - bx) ** 2 + (d[1] - by) ** 2
        left = (l[0] - bx) ** 2 + (l[1] - by) ** 2
        up = (u[0] - bx) ** 2 + (u[1] - by) ** 2

        # y가 같을때
        if by == startY:
            if startX > bx:
                answer.append(min(up, down, right))
            else:
                answer.append(min(up, down, left))
            
        # x 가 같을때
        if bx == startX:
            if startY > by:
                answer.append(min(left, right, up))
            else:
                answer.append(min(left, right, down))
        if bx != startX and by != startY:
            answer.append(min(up, down, left, right))
    return answer
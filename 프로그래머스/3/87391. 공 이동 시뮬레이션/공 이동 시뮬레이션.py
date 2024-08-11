def solution(n, m, x, y, queries):
    min_x, max_x = x, x
    min_y, max_y = y, y
    
    for cmd, d in reversed(queries):
        if cmd == 0:
            max_y = max_y+d if max_y+d < m else m-1
            if min_y > 0:
                min_y += d
        elif cmd == 1:
            min_y = min_y-d if min_y-d >= 0 else 0
            if max_y < m-1:
                max_y -= d
        elif cmd == 2:
            max_x = d+max_x if max_x+d < n else n-1
            if min_x > 0:
                min_x += d
        elif cmd == 3:
            min_x = min_x-d if min_x-d >= 0 else 0
            if max_x < n-1:
                max_x -= d
                
        if min_x >= n or max_x < 0 or min_y >= m or max_y < 0:
            return 0
        
    return (max_x - min_x + 1) * (max_y - min_y + 1)
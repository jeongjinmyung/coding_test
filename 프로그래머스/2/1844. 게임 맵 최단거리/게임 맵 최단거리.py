def solution(maps):
    from collections import deque
    
    end = (len(maps)-1, len(maps[0])-1)
    dir = [(1,0), (-1,0), (0,1), (0,-1)]
    que = deque()
    que.append((0,0))
    visited = set()
    visited.add((0,0))
    answer = []
    move = 0

    while que:
        que_len = len(que)
        for _ in range(que_len):
            node = que.popleft()
            if node == end:
                return move+1
            for d in dir:
                new_dir = (node[0]+d[0], node[1]+d[1])
                if new_dir not in visited and 0<=new_dir[0]<len(maps) and 0<=new_dir[1]<len(maps[0]) and maps[new_dir[0]][new_dir[1]]:
                    que.append(new_dir)
                    visited.add(new_dir)
        move += 1
    return -1
def solution(numbers):
    keyboard = {
        '1':(0,0),
        '2':(0,1),
        '3':(0,2),
        '4':(1,0),
        '5':(1,1),
        '6':(1,2),
        '7':(2,0),
        '8':(2,1),
        '9':(2,2),
        '*':(3,0),
        '0':(3,1),
        '#':(3,2)
    }
    
    def cal_length(head, to):
        dx = abs(head[0] - to[0])
        dy = abs(head[1] - to[1])
        if dx == 0 and dy == 0:
            return 1
        elif dx + dy == 1:
            return 2
        elif dx == 1 and dy == 1:
            return 3
        else:
            return 2 * (dx + dy) - min(dx, dy)
    
    n = len(numbers)
    dp = {}
    dp[('4', '6')] = 0

    for n in numbers:
        next_dp = {}
        for (left, right), cost in dp.items():
            next_num = n
            
            if next_num != right:
                left_cost = cost + cal_length(keyboard[left], keyboard[next_num])
                next_dp[(next_num, right)] = min(next_dp.get((next_num, right), float('inf')), left_cost)
            if next_num != left:
                right_cost = cost + cal_length(keyboard[right], keyboard[next_num])
                next_dp[(left, next_num)] = min(next_dp.get((left, next_num), float('inf')), right_cost)
        dp = next_dp
    return min(dp.values())
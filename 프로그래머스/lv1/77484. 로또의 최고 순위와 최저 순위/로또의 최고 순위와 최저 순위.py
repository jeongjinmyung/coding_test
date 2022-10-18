def solution(lottos, win_nums):
    count = 0
    num_zero = 0
    dict = {6:1,5:2,4:3,3:4,2:5,1:6,0:6}
    
    for i in range(len(lottos)):
        if lottos[i] in win_nums:
            count += 1
        elif lottos[i] == 0:
            num_zero += 1
    
    max_num = count + num_zero

    return [dict[max_num], dict[count]]
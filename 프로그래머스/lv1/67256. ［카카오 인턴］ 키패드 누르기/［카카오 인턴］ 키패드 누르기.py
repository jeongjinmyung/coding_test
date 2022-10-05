def solution(numbers, hand):
    answer = ""
    num_dict = {"1":[1,1],"2":[1,2],"3":[1,3],
               "4":[2,1],"5":[2,2],"6":[2,3],
               "7":[3,1],"8":[3,2],"9":[3,3],
               "*":[4,1],"0":[4,2],"#":[4,3]}
    left_stat = num_dict["*"]
    right_stat = num_dict["#"]
    
    
    def distance(next):
        ans = ""
        left_dist = abs(num_dict[str(next)][0] - left_stat[0]) + abs(num_dict[str(next)][1] - left_stat[1])
        right_dist = abs(num_dict[str(next)][0] - right_stat[0]) + abs(num_dict[str(next)][1] - right_stat[1])
        if left_dist == right_dist:
            if hand == "right":
                ans = "R"
            elif hand == "left":
                ans = "L"
        elif left_dist > right_dist:
            ans = "R"
        elif left_dist < right_dist:
            ans = "L"
        return ans
    
    for n in numbers:
        if n in [1,4,7]:
            answer += "L"
            left_stat = num_dict[str(n)]
        elif n in [3,6,9]:
            answer += "R"
            right_stat = num_dict[str(n)]
        elif n in [2,5,8,0]:
            if distance(n) == "R":
                answer += "R"
                right_stat = num_dict[str(n)]
            elif distance(n) == "L":
                answer += "L"
                left_stat = num_dict[str(n)]
    
    
    return answer
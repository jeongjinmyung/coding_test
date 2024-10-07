def solution(storey):
    answer = 0
    
    while storey > 0:
        current_digit = storey % 10
        next_digit = (storey // 10) % 10
        
        if current_digit > 5 or (current_digit==5 and next_digit >=5):
            answer += 10 - current_digit
            storey = (storey // 10) + 1
        else:
            answer += current_digit
            storey //= 10
    
    return answer
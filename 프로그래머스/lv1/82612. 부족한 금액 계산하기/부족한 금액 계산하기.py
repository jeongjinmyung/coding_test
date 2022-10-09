def solution(price, money, count):
    answer = 0
    price_sum = 0
    for i in range(1, count +1):
        price_sum += price * i
    if price_sum <= money:
        return 0
    else:
        answer = price_sum - money
        return answer
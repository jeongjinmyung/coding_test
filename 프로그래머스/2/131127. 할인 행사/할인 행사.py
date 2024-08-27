def solution(want, number, discount):
    want_dict = dict(zip(want, number))
    n = len(discount)
    total_days = 0

    for i in range(n - 10 + 1):
        current_discount = discount[i:i + 10]
        discount_dict = {}
        
        for item in current_discount:
            if item in discount_dict:
                discount_dict[item] += 1
            else:
                discount_dict[item] = 1
        
        if all(discount_dict.get(product, 0) >= want_dict[product] for product in want_dict):
            total_days += 1
    
    return total_days
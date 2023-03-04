def solution(today, terms, privacies):
    answer = []
    today_y, today_m, today_d = map(int,today.split('.'))
    
    exp = {}
    for n in terms:
        typ, num = n.split(" ")
        exp[typ] = int(num)

    for i in range(len(privacies)):
        days, kind = privacies[i].split(" ")
        year, mon, day = map(int,days.split("."))

        mon += exp[kind]
        while mon > 12:
            mon -= 12
            year += 1

        if year > today_y:
            continue
        elif year == today_y:
            if mon > today_m:
                continue
            elif mon == today_m:
                if day > today_d:
                    continue
        answer.append(i+1)
    
    return answer
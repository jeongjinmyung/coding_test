import collections
import math

def solution(fees, records):
    answer = []
    base_time, base_fee, extra_sec, extra_fee = fees

    car_records = collections.defaultdict(list)
    for record in records:
        time, car, move = record.split()
        hour, min = map(int, time.split(':'))
        minutes = hour * 60 + min
        
        if move == "IN":
            car_records[car].append([minutes, 1439])
        else:
            car_records[car][-1][1] = minutes
    car_records = sorted(car_records.items(), key=lambda x: x[0], reverse=False)
    
    for rcd in car_records:
        cumulated_time = 0
        for start, end in rcd[1]:
            cumulated_time += end - start
        if cumulated_time <= base_time:
            answer.append(base_fee)
        else:
            total_fee = base_fee + (math.ceil((cumulated_time - base_time) / extra_sec) * extra_fee)
            answer.append(total_fee)

    return answer
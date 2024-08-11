def solution(a, b, g, s, w, t):
    left, right = 0, 10**18
    while left < right:
        mid = (left + right) // 2
        total_gold, total_silver, total_weight = 0, 0, 0
        for i in range(len(g)):
            max_trip_time = mid // (2 * t[i])
            if mid % (2 * t[i]) >= t[i]:
                max_trip_time += 1
            possible_gold = min(g[i], max_trip_time * w[i])
            possible_silver = min(s[i], max_trip_time * w[i])
            possible_weight = min(g[i] + s[i], max_trip_time * w[i])

            total_gold += possible_gold
            total_silver += possible_silver
            total_weight += possible_weight
        if total_gold >= a and total_silver >= b and total_weight >= a+b:
            right = mid
        else:
            left = mid + 1
    return left
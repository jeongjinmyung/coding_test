def solution(absolutes, signs):
    answer = sum([absolutes if signs else -absolutes for absolutes, signs in zip(absolutes, signs)])
    return answer
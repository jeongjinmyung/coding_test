def solution(x):
    answer = True
    xlst = list(str(x))
    xsum = 0
    for i in range(len(xlst)):
        xsum += int(xlst[i])
    if x % xsum == 0:
        return answer
    else:
        return not answer
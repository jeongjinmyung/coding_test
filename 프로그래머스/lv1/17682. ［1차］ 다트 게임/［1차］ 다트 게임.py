import re

def solution(dartResult):

    point = {"S":1, "D":2, "T":3}
    bonus = {"":1, "*":2, "#":-1}


    regx = re.compile("(\d?\d)([SDT])([#*]?)")
    reg = regx.findall(dartResult)
    
    for i in range(len(reg)):
        if reg[i][2] == "*" and i >0:
            reg[i -1] *= 2
        reg[i] = int(reg[i][0]) ** point[reg[i][1]] * bonus[reg[i][2]]
    return sum(reg)
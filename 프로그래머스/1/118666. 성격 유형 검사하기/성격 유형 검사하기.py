from collections import defaultdict

def solution(survey, choices):
    answer = ''
    combi = defaultdict(int)

    for sur, cho in zip(survey, choices):
        score = cho - 4  # 양수면 동의, 음수면 비동의, 0이면 모르겠음
        if score > 0:
            combi[sur[1]] += score
        elif score < 0:
            combi[sur[0]] += -score
    
    if combi['R'] >= combi['T']:
        answer += 'R'
    else:
        answer += 'T'
    
    if combi['C'] >= combi['F']:
        answer += 'C'
    else:
        answer += 'F'
    
    if combi['J'] >= combi['M']:
        answer += 'J'
    else:
        answer += 'M'

    if combi['A'] >= combi['N']:
        answer += 'A'
    else:
        answer += 'N'

    return answer
def solution(s):
    zero = 0   # 0의 개수
    conver = 0 # 이진 변환 횟수
    
    # s가 '1'이 될 때까지
    while s != '1':
        if '0' in s: # '0' 이 있으면
            zero += s.count('0')  # '0'의 개수를 더하고
            s = s.replace('0','') # 공백으로 바꾸기
            
        length = len(s) # 문자열의 길이
        s = str(format(length,'b')) # 2진수로 변환
        conver += 1 # 이진 변환 횟수 +1

    return [conver,zero]
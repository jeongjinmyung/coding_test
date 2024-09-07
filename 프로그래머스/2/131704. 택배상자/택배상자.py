def solution(order):
    stack = []  # 보조 컨테이너
    l = len(order)
    idx = 0  # 현재 실을 상자
    answer = 0

    for box in range(1, l+1):
        stack.append(box)  # 보조 컨테이너에 담음
        while stack and stack[-1] == order[idx]:  # 보조 컨테이너에 상자가 있고 그게 현재 실어야 되는 순서라면
            answer += 1  # 실음
            idx += 1  # 다음 순서로 이동
            stack.pop()  # 보조 컨테이너에서 제거
    return answer
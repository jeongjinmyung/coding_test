def solution(name, yearning, photo):
    answer = [0] * len(photo) 
    n_dict = {}
    for n, y in zip(name, yearning):
        n_dict[n] = y

    for i in range(len(photo)):
        for p in photo[i]:
            if p in name:
                answer[i] += n_dict[p]
            else:
                pass
    answer
    return answer
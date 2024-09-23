def solution(n, l, r):
    def count_ones_recursive(n, l, r):
        # n번째 비트열의 길이는 5^n
        if n == 0:
            return 1 if l <= 1 <= r else 0

        # 현재 비트열의 길이
        length = 5 ** n
        # 이전 단계에서의 비트열 길이
        prev_length = length // 5

        count = 0
        for i in range(5):
            start = i * prev_length + 1
            end = (i + 1) * prev_length

            # 현재 구간이 완전히 중간 구간(3번째 구간, 00000에 해당)인 경우
            if i == 2:
                continue

            # 구간이 현재 조사해야 하는 구간과 겹치는 경우
            if r >= start and l <= end:
                count += count_ones_recursive(n - 1, max(l, start) - start + 1, min(r, end) - start + 1)

        return count

    return count_ones_recursive(n, l, r)
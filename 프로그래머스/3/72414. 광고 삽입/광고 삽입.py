def str_to_seconds(time_str):
    hours, minutes, seconds = map(int, time_str.split(':'))
    return hours * 3600 + minutes * 60 + seconds

def seconds_to_str(seconds):
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    seconds = seconds % 60
    return f"{hours:02}:{minutes:02}:{seconds:02}"

def solution(play_time, adv_time, logs):
    play_seconds = str_to_seconds(play_time)
    adv_seconds = str_to_seconds(adv_time)
    
    total_time = [0] * (play_seconds + 1)

    # 시청자들의 재생 구간을 누적 재생시간 배열에 반영
    for log in logs:
        start, end = log.split('-')
        start_sec = str_to_seconds(start)
        end_sec = str_to_seconds(end)
        total_time[start_sec] += 1
        total_time[end_sec] -= 1

    # 각 시각의 누적 재생시간 계산
    for i in range(1, play_seconds + 1):
        total_time[i] += total_time[i - 1]

    # 누적 재생시간 계산
    for i in range(1, play_seconds + 1):
        total_time[i] += total_time[i - 1]

    max_view_time = total_time[adv_seconds - 1]
    max_start_time = 0

    # 공익광고를 삽입했을 때의 누적 재생시간 계산
    for start_time in range(1, play_seconds - adv_seconds + 1):
        view_time = total_time[start_time + adv_seconds - 1] - total_time[start_time - 1]
        if view_time > max_view_time:
            max_view_time = view_time
            max_start_time = start_time

    return seconds_to_str(max_start_time)
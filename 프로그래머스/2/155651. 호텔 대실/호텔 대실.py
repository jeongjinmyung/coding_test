import heapq
from typing import List, Tuple

def conver_to_minutes(time:List[str]) -> Tuple[int, int]:
    start_hour, start_minutes = map(int, time[0].split(":"))
    end_hour, end_minutes = map(int, time[1].split(":"))
    start = start_hour * 60 + start_minutes
    end = end_hour * 60 + end_minutes + 10
    return (start, end)

def solution(book_time: List[List[str]]) -> int:
    times = [conver_to_minutes(time) for time in book_time]
    times.sort(key=lambda x: x[0])

    rooms = []

    for start, end in times:
        if rooms and rooms[0] <= start:
            heapq.heappop(rooms)
        heapq.heappush(rooms, end)

    return len(rooms)
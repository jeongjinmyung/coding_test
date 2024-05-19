def solution(tickets):
    from collections import defaultdict
    graph = defaultdict(list)

    for f,t in tickets:
        graph[f].append(t)
        
    for c in graph:
        graph[c].sort(reverse=True)

    path = []
    stack = ['ICN']
    while stack:
        city = stack[-1]

        if graph[city]:
            next_city = graph[city].pop()
            stack.append(next_city)
        else:
            path.append(stack.pop())
    return path[::-1]
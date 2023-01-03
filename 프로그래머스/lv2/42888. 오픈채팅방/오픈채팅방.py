def solution(record):
    answer = []
    userDB = dict()
    actions = []


    for v in record:
        info = v.split()
        action, userid = info[0], info[1]
        if action in ["Enter", "Change"]:
            nickname = info[2]
            userDB[userid] = nickname
        actions.append((userid, action))

    for actioninfo in actions:
        userid, action = actioninfo[0], actioninfo[1]
        if action == "Enter":
            answer.append(f"{userDB[userid]}님이 들어왔습니다.")
        elif action == "Leave":
            answer.append(f"{userDB[userid]}님이 나갔습니다.")
    return answer
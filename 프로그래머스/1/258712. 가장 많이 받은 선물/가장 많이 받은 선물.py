def solution(friends, gifts):
    giver = {}
    taker = {}
    score_dict = {}

    for i in range(len(friends)):
        giver[friends[i]] = {}
        taker[friends[i]] = {}
        score_dict[friends[i]] = 0
        for j in range(len(friends)):
            if i == j:
                continue
            else:
                giver[friends[i]][friends[j]] = 0
                taker[friends[i]][friends[j]] = 0

    for names in gifts:
        names = names.split()
        giver[names[0]][names[1]] += 1
        taker[names[1]][names[0]] += 1

    for i in range(len(friends)):
        me = friends[i]
        friend = [name for name in friends if name != friends[i]]

        for f in friend:
            my_gift_idx = sum(giver[me].values()) - sum(taker[me].values())
            friend_gift_idx = sum(giver[f].values()) - sum(taker[f].values())

            if giver[me][f] == taker[me][f]:
                if my_gift_idx == friend_gift_idx:
                    continue
                elif my_gift_idx > friend_gift_idx:
                    score_dict[me] += 1
                elif my_gift_idx < friend_gift_idx:
                    score_dict[f] += 1

            elif giver[me][f] > taker[me][f]:
                score_dict[me] += 1
            elif giver[me][f] < taker[me][f]:
                score_dict[f] += 1
    return max([n // 2 for n in score_dict.values()])
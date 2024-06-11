import re
import itertools

def solution(user_id, banned_id):
    ban_list = []
    for ban in banned_id:
        ban = ban.replace("*", ".")
        pattern = re.compile(ban)
        pat = [element for element in user_id if pattern.fullmatch(element)]
        pat.sort()
        ban_list.append(pat)
        
    ban_len = len(ban_list)
    combination = set(tuple(sorted(combi)) for combi in itertools.product(*ban_list) if len(set(combi)) == ban_len)

    return len(combination)
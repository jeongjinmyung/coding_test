import itertools
import collections
import bisect


def solution(info, query):
    
    candidates = []
    for infos in info:
        lang, position, career, food, score = infos.split()
        score = int(score)
        candidates.append((lang, position, career, food, score))
        
    queries = []
    for qr in query:
        qr = qr.replace('and', '')
        lang, position, career, food, score = qr.split()
        score = int(score)
        queries.append((lang, position, career, food, score))
        
    def get_key(lang, position, career, food):
        keys = []
        for l, p, c, f in itertools.product([lang, '-'], [position, '-'], [career, '-'], [food, '-']):
            keys.append((l, p, c, f))
        return keys
    
    conditions = collections.defaultdict(list)
    
    for lang, position, career, food, score in candidates:
        keys = get_key(lang, position, career, food)
        for key in keys:
            conditions[key].append(score)
            
    for score in conditions.values():
        score.sort()
    
    answer = []
    for lang, position, career, food, score in queries:
        key = (lang, position, career, food)
        if key in conditions:
            score_k = conditions[key]
            idx = bisect.bisect_left(score_k, score)
            answer.append(len(score_k) - idx)
        else:
            answer.append(0)
        
    return answer
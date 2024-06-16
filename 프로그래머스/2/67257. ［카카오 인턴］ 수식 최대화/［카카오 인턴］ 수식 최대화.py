import re
import itertools

def solution(expression):
    operator = set(re.findall(r'\D', expression))
    operator_npr = list(itertools.permutations(operator, len(operator)))
    
    ans = 0
    for npr in operator_npr:
        evaluated_val = int(eval_recursive(expression, npr))
        ans = max(ans, abs(evaluated_val))
    
    return ans


def eval_recursive(exp:str, npr:list, depth:int=0) -> str:
    if depth == (len(npr) -1):
        return str(eval(exp))
    
    op = npr[depth]
    evaluated = eval(
        op.join(
            [eval_recursive(e, npr, depth+1) for e in exp.split(op)]
        )
    )

    return str(evaluated)
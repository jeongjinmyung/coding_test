N = int(input())
vps = []
for _ in range(N):
    data = list(input())
    vps.append(data)

def check_vps(bracket: list) -> bool:
    if bracket[0] == ")":  # 만들지 못함
        return False
    stack = []
    for b in bracket:
        if stack == [] or b == "(":
            stack.append(b)
            continue
        
        if b == ")":
            if stack[-1] == "(":
                stack.pop()
    
    if len(stack) > 0:
        return False
    else:
        return True
    
for v in vps:
    if check_vps(v):
        print("YES")
    else:
        print("NO")

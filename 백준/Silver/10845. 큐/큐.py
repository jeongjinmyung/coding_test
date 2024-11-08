from collections import  deque

N = int(input())
commands = []
for _ in range(N):
    com = input()
    commands.append(com)

class Myprogram:
    def __init__(self):
        self.que = deque([])

    def push(self, num:int):
        self.que.append(num)

    def pop(self):
        if len(self.que) == 0:
            return -1
        
        output = self.que.popleft()
        return output
    
    def size(self):
        return len(self.que)
    
    def empty(self):
        if len(self.que) == 0:
            return 1
        else:
            return 0
        
    def front(self):
        if len(self.que) == 0:
            return -1
        return self.que[0]
    
    def back(self):
        if len(self.que) == 0:
            return -1
        return self.que[-1]

computer = Myprogram()
answer = []
for command in commands:
    method_name = command
    if command.startswith('push'):
        method_name, num = command.split()
        num = int(num)
    
    if hasattr(computer, method_name):
        method = getattr(computer, method_name)
        if method_name == 'push':
            method(num)
        else:
            output = method()
            answer.append(output)

for ans in answer:
    print(ans)
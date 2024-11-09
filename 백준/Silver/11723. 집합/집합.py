import sys

M = int(input())

class Myprogram:
    def __init__(self):
        self.set = set()

    def add(self, x):
        self.set.add(x)

    def remove(self, x):
        self.set.discard(x)

    def check(self, x):
        if x in self.set:
            print(1)
        else:
            print(0)

    def toggle(self, x):
        if x in self.set:
            self.remove(x)
        else:
            self.add(x)

    def all(self):
        self.set = set(range(1, 21))

    def empty(self):
        self.set = set()


computer = Myprogram()


for _ in range(M):
    command = sys.stdin.readline().rstrip()
    if command == "all" or command == "empty":
        method = getattr(computer, command)
        method()
    else:
        method_name, num = command.split()
        num = int(num)
        method = getattr(computer, method_name)
        method(num)

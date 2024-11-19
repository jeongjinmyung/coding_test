from collections import deque


class AC:
    def __init__(self, orders: str, arr: deque):
        self.orders = orders
        self.arr = arr
        self.reversed = False
    
    def D(self):
        if not self.arr:
            return "error"
        if self.reversed:
            self.arr.pop()
        else:
            self.arr.popleft()
        return None
    
    def forward(self):
        for order in self.orders:
            if order == "R":
                self.reversed = not self.reversed
            elif order == "D":
                result = self.D()
                if result == "error":
                    return "error"
                
        if self.reversed:
            self.arr.reverse()
        return "[" + ",".join(map(str, self.arr)) + "]"


T = int(input())
for _ in range(T):
    p = list(input().strip())
    n = int(input())
    xs = input().strip()
    arr = deque() if xs == "[]" else deque(map(int, xs[1:-1].split(",")))

    computer = AC(p, arr)
    result = computer.forward()
    print(result)

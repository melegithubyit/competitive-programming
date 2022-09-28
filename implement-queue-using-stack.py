class MyQueue:
    def __init__(self):
        self.stk1 = []    #creating two empty stacks
        self.stk2 = []
    def push(self, x):
        self.stk1.append(x)
    def pop(self):
        if self.stk2:
            return self.stk2.pop()
        else:
            while self.stk1:
                self.stk2.append(self.stk1.pop())
            if self.stk2:
                return self.stk2.pop()
            else:
                raise Exception()
    def peek(self):
        if self.stk2:
            x = self.stk2.pop()
            self.stk2.append(x)
            return x
        else:
            while self.stk1:
                self.stk2.append(self.stk1.pop())
            if self.stk2:
                x = self.stk2.pop()
                self.stk2.append(x)
                return x
            else:
                raise Exception()
    def empty(self):
        return not self.stk1 and not self.stk2

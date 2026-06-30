class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []
        
    def push(self, val: int) -> None:
        self.stack.append(val)
        self.minStack.append(min(self.stack))
            

    def pop(self) -> None:
        self.stack = self.stack[0:-1]
        self.minStack = self.minStack[0:-1]
            

    def top(self) -> int:
        return self.stack[-1]
            

    def getMin(self) -> int:
        return self.minStack[-1]

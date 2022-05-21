

# Idea: As the stack grows, we just save the minimum for each height in
# another stack. This works because of how a stack grows, the lower elements
# cannot be changed until all elements above it are popped.
class MinStack:

    def __init__(self):
        self.min = []
        self.stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.min.append(val)
        if len(self.min) < 2: return
        if self.min[-1] > self.min[-2]:
            self.min[-1] = self.min[-2]

    def pop(self) -> None:
        self.stack.pop()
        self.min.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min[-1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
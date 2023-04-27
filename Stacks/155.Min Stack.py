class MinStack:

    def __init__(self):
        self.stack = []
        self.minstack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.minstack:
            self.minstack.append(val)
        else:
            self.minstack.append(min(val, self.minstack[-1]))

    def pop(self) -> None:
        self.stack.pop()
        self.minstack.pop()

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.minstack[-1]
        


# Your MinStack object will be instantiated and called as such:
obj = MinStack()
for val in "876785254156":
    obj.push(val)   



param_3 = obj.top()
print("Top ", param_3)

param_4 = obj.getMin()
print("Min ", param_4)

obj.pop()
obj.pop()
obj.pop()
obj.pop()

param_3 = obj.top()
print("Top ", param_3)

param_4 = obj.getMin()
print("Min ", param_4)
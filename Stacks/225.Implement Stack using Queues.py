from collections import deque

class MyStack:

    def __init__(self):
        self.stack = deque()

    def push(self, x: int) -> None:
        # self.stack.reverse()
        # self.stack.append(x)
        # self.stack.reverse()

        length = len(self.stack)
        self.stack.append(x)

        while length:
            length -= 1
            self.stack.append(self.stack.popleft())

    def pop(self) -> int:
        # self.stack.reverse()
        # val = self.stack.pop()
        # self.stack.reverse()
        # return val

        return self.stack.popleft()


    def top(self) -> int:
        return self.stack[0]
        

    def empty(self) -> bool:
        return not self.stack


# Your MyStack object will be instantiated and called as such:
obj = MyStack()
obj.push(15)
param_2 = obj.pop()
print(param_2)
obj.push(15)
obj.push(25)
obj.push(35)
param_3 = obj.top()
print(param_3)

obj.pop()
obj.pop()
obj.pop()
param_4 = obj.empty()
print(param_4)
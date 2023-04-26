class Stack:
    def __init__(self):
        self.vals = []

    def isEmpty(self):
        return not self.vals

    def push(self, val):
        self.vals.append(val)

    def pop(self):
        return self.vals.pop()
    
    def peek(self):
        return self.vals[-1]
    
    def __str__(self):
        return str(self.vals)
res = Stack()
print(res.isEmpty())
res.push(1)
res.push(2)
print(res.isEmpty())
print(res)
print(res.peek())
res.push(3)
print(res.peek())
res.pop()
print(res)



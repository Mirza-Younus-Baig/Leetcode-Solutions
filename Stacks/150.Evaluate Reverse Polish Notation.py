from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        stack = []

        for val in tokens:

            if val == "+":
                stack.append(stack.pop() + stack.pop())
            elif val == "-":
                a = stack.pop()
                b = stack.pop()
                stack.append(b - a)
            elif val == "*":
                stack.append(stack.pop() * stack.pop())
            elif val == "/":
                a = stack.pop()
                b = stack.pop()
                stack.append(int(b / a))
            else:
                stack.append(int(val))

        return stack[-1]

res = Solution()
# inp = ["2","1","+","3","*"]
# inp = ["4","13","5","/","+"]
inp = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
# inp = ["18"]
print(res.evalRPN(inp))

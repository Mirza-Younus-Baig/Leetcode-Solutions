


class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 == 1:
            return False
            
        stack = []
        mapping = {")" : "(", "}" : "{", "]" : "["} 
        for val in s:
            if val in ("(", "{", "["):
                stack.append(val)
            
            else:
                if not stack or mapping[val] != stack.pop():
                    return False


        return not stack


res = Solution()

inp = "()[]{}"
# inp = ")(){{]}]}"
# inp = "({[([])]})"

print(res.isValid(inp))
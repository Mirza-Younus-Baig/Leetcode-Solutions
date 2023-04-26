from typing import List

class Solution:
    def reverseString1(self, s: List[str]) -> None:
        s.reverse()
        print(s)

    def reverseString2(self, s: List[str]) -> None:
        i, j = 0, len(s) - 1
        while i < j:
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1
        print(s)

    def reverseString3(self, s: List[str]) -> None:
        s[:] = s[::-1]
        print(s)


res = Solution()
s = ["h","e","l","l","o"]

# Uncomment the below function call to execute the required code
# As per the requirement the functions does not return any value
res.reverseString1(s)
# res.reverseString2(s)
# res.reverseString3(s)
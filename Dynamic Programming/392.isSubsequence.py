class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        j = 0
        i = 0 
        while i < len(t) and j < len(s):
            if t[i] == s[j]:
                j += 1
            i += 1
        return j == len(s)
            





res = Solution()
s = ""
t = ""
print(res.isSubsequence(s, t))

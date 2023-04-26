# Question link: https://leetcode.com/problems/roman-to-integer/

class Solution:    
    def romanToInt(self, s:str) -> int:
        valDict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        res = 0
        for i in range(len(s)):
            if i+1<len(s) and valDict[s[i]] < valDict[s[i+1]]:
                res -= valDict[s[i]]
            else:
                res += valDict[s[i]]
                
        return res
                


    

inp = input('Enter the roman number to convert').upper()
res = Solution()


print(res.romanToInt(inp))
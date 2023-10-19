from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        common = min(strs, key=len)
        for i in strs[1:]:
            j = 0
            while j < len(common) and j < len(i):
                if common[j] != i[j]:
                    common = common[:j]                
                    break
                j += 1
        return common

print(Solution().longestCommonPrefix(["flower","flow","flight"]))



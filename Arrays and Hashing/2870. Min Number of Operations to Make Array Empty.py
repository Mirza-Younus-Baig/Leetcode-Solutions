from typing import List
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        occ = dict()
        for i in range(len(nums)):
            if nums[i] in occ:
                occ[nums[i]] += 1
            else:
                occ[nums[i]] = 1
        res = 0
        for elem, val in occ.items():
            if val == 1:
                return -1
            if val % 3 == 0:
                res += val // 3
            else:
                res += val // 3 + 1
        
        return res

            

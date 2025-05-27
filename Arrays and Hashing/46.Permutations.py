from typing import List

class Solution:

    def perm(self, start,res, nums):
        if start == len(nums):
            res.append(nums[:])
            return 
        
        for i in range(start, len(nums)):
            nums[i], nums[start] = nums[start], nums[i]
            self.perm(start + 1, res, nums)
            nums[i], nums[start] = nums[start], nums[i]
        
        return res

    def permute(self, nums: List[int]) -> List[List[int]]:
        return self.perm(0, [], nums)

        
        
obj = Solution()
nums = list(map(int, input().split()))
res = obj.permute(nums)

print(res)
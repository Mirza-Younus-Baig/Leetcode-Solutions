from typing import List
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        l = 0
        total = sum(nums)
        for i in range(len(nums)):
            r = total - nums[i] - l
            if l ==r:
                return i
            l += nums[i]
        return -1


res = Solution()
inp = [1,7,3,6,5,6]
print(res.pivotIndex(inp))
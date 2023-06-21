from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        count = 0
        for i in range(len(nums)):
            if nums[i] == val:
                nums[i] = 51
                count += 1
    
        nums[:] = sorted(nums)

        return len(nums) - count
    
res = Solution()
print(res.removeElement([0,1,2,2,3,0,4,2], 2))
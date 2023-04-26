from typing import List

class Solution:
    # Solution 1
    def moveZeroes(self, nums: List[int]) -> None:
        if len(nums) >= 2:
            i, j = 0, 0
            while j < len(nums):
                if nums[j] != 0:
                    nums[i] = nums[j]
                    j+= 1
                    i+=1
                else:
                    j += 1
            for z in range(i, len(nums)):
                nums[z] = 0
            print(nums)

    # Solution 2
    def moveZeroes2(self, nums: List[int]) -> None:
        i = 0
        for j in range(len(nums)):
            if nums[j] != 0:
                nums[i], nums[j] = nums[j] , nums[i]
                i += 1
        print(nums)


res = Solution()
inp = [0,1,0,3,12]
# res.moveZeroes(inp)
# res.moveZeroes2(inp)
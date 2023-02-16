from typing import List

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        l, h = 0, len(nums) - 1
        res = [0 for _ in range(len(nums))]
        nums = [abs(n) for n in nums]
        for i in range(len(nums)-1, -1, -1):
            if nums[l] < nums[h]:
                res[i] = nums[h]**2
                h -= 1
            else:
                res[i] = nums[l]**2
                l += 1


        return res


res = Solution()
inp = [-4,-1,0,3,10]
# inp = [-7,-3,2,3,11]
print(res.sortedSquares(inp))
from typing import List
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        currOnes, maxOnes = 0, 0
        for currElement in nums:
            if currElement == 0:
                maxOnes = max(maxOnes, currOnes)
                currOnes = 0
            else:
                currOnes += 1
        return max(maxOnes, currOnes)

nums = [1,1,0,1,1,1]
print(Solution().findMaxConsecutiveOnes(nums))
from typing import List

class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        
        nums1 = set(nums1)
        nums2 = set(nums2)

        return [list(nums1 - nums2), list(nums2 - nums1)]


nums1 = [-80,-15,-81,-28,-61,63,14,-45,-35,-10]
nums2 = [-1,-40,-44,41,10,-43,69,10,2]

res = Solution()
print(res.findDifference(nums1, nums2))
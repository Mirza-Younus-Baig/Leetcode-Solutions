from typing import List
from math import ceil

class Solution:
    def minEatingSpeed(self, nums: List[int], h: int) -> int:
        # Binary search to find the minimum eating speed such that
        # Koko can eat all bananas within h hours
        left = 1
        right = max(nums)
        result = right

        while left <= right:
            mid = (left + right) // 2
            hours = 0

            for pile in nums:
                hours += ceil(pile / mid)

            if hours > h:
                left = mid + 1
            else:
                result = mid
                right = mid - 1

        return result
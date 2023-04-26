from typing import List


class Solution:
    # First method that uses a new array and two loops to add elements
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def rotate1(self, nums: List[int], k: int) -> None:
        k = k % len(nums)
        res = []
        for i in nums[len(nums)-k:]:
            res.append(i)
        for i in nums[:len(nums)-k-1]:
            res.append(i)
        print("First method: ", res)

    # Second method that uses a new array and one loop to add elements
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def rotate2(self, nums: List[int], k: int) -> None:
        lenNums = len(nums)
        k = k % lenNums
        res = [0 for _ in range(lenNums)]
        for i in range(lenNums):
            res[(i+k) % lenNums] = nums[i]
        print("Second method: ", res)

    # Third method that used same array and one for loop
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def rotate3(self, nums: List[int], k: int) -> None:
        k = k % len(nums)
        l, r = 0, len(nums) - k - 1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l, r = l+1, r-1
        l, r = len(nums) - k, len(nums) - 1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l, r = l+1, r-1
        l, r = 0, len(nums)-1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l, r = l+1, r-1
        print("Third Method:", nums)

res = Solution()
inp = [1, 2, 3, 4, 5, 6, 7]
k = 3
# res.rotate1(inp, k)
# res.rotate2(inp, k)
res.rotate3(inp, k)

from typing import List

class Solution:
    def perm(self, nums):
        ind = 0
        for i in range(len(nums) - 1, 0, -1):
            if nums[i-1] < nums[i]:
                ind = i
                break
        else:
            nums.reverse()
            return nums

        next_great = float('inf')
        maxInd = ind

        for i in range(ind, len(nums)):
            if nums[i] > nums[ind - 1] and next_great > nums[i]:
                next_great = nums[i]
                maxInd = i

        nums[ind - 1], nums[maxInd] = nums[maxInd], nums[ind - 1]
        nums[ind:] = sorted(nums[ind:])
        return nums


    def nextPermutation(self, nums: List[int]) -> None:
       print(self.perm(nums))

obj = Solution()
nums = list(map(int, input().split()))
obj.nextPermutation(nums)
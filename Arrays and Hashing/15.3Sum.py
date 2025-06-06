

class Solution(object):
    def threeSum(self, nums):
        nums.sort()
        N, result = len(nums), []
        target = 0
        res = []
        for i in range(N-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
           
            left,right = i+1, N-1
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total == target:
                    res.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1

                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1

                elif total < target:
                    left += 1
                else:
                    right -= 1

        return res
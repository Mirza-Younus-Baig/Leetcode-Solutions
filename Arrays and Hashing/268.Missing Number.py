class Solution:
    # def missingNumber(self, nums):
    #     res = len(nums)
    #     for i in range(len(nums)):
    #         res ^= i
    #         res ^= nums[i]
    #     return res
    
    def missingNumber(self, nums):
        total = 0
        for i in range(len(nums) + 1):
            total += i
        return total - sum(nums)

print(Solution().missingNumber([3,0,1]))
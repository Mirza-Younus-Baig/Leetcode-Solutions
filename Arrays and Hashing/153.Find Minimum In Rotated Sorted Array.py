from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        low, high = 0, len(nums) - 1

        while low <= high:
        
            if nums[low] <= nums[high]:
                return nums[low]
        
            mid = (low + high)//2

            if nums[low] > nums[mid]:
                high = mid
            else:
                low = mid + 1

    

if __name__ == '__main__':
    # inpArray = list(map(int, input().split()))

    # inpArray = [0,1,2,4,5,6,7]
    inpArray = [5,6,7,-88, 0,1,2,4]
    # inpArray = [7,0,1,2,4,5,6]

    sol = Solution()
    print(sol.findMin(inpArray))
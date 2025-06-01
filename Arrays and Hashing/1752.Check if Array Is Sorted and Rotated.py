from typing import List

class Solution:
    def check(self, nums: List[int]) -> bool:
        return sum(nums[i] < nums[i-1] for i in range(len(nums))) <= 1

        # Expanded solution for the above one-liner
        # cnt = 0
        # for i in range(len(nums)):
        #     if nums[i] > nums[(i+1) % len(nums)]:
        #         cnt += 1
        # if cnt <= 1:
        #     return True
        # else:
        #     return False


if __name__ == "__main__":
    # nums = list(map(int, input().split()))
    nums = [3,4,5,1,2]
    # nums = [2,1,3,4]
    print(Solution().check(nums))
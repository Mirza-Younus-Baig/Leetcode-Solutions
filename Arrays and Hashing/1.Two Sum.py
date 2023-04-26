from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i, j = 0, len(numbers) - 1
        while i < j:
            k = numbers[i] + numbers[j]
            if k == target:
                return [i+1,j+1]
            elif k < target:
                i += 1
            else:
                j -= 1



res = Solution()
inp = [2,7,11,15]
k = 13
print(res.twoSum(inp, k))
from typing import List

class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        i = 0
        j = 0
        count = 0

        while i < len(nums1) and j < len(nums2):
            print("vef",i, j)
            if nums2[j:].count(nums1[i]) != 0:
                count += 1
                j = nums2.index(nums1[i]) + 1
                nums2[:j] = [0] * j
                print(i, j)
            
            i += 1
        
        return count


if __name__ == "__main__":
    res = Solution()
    inp1 = [2,5,1,2,5]
    inp2 = [10,5,2,1,5,2]

    print(res.maxUncrossedLines(inp1, inp2))
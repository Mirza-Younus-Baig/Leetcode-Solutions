from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i, j = m-1, n-1
        end = m + n - 1
        while i > -1 and j > -1:
            if nums1[i] >= nums2[j]:
                nums1[end] = nums1[i]

                i -= 1
            else:
                nums1[end] = nums2[j]
                j -= 1
            
            end -= 1
        
        while j > -1:
            nums1[end] = nums2[j]
            j -= 1
            end -= 1
        
    


res =Solution()
nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n =3
res.merge(nums1, m, nums2, n)
print(nums1)

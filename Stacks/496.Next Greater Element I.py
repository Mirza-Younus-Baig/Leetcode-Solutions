from typing import List

class Solution:
    def nextGreaterElement(self, nums1: List[int], arr: List[int]) -> List[int]:
        stack = []
        nge = []

        for i in range(len(arr) - 1, -1, -1):
            
            while stack and arr[i] >= stack[-1] :
                stack.pop()
            
            if stack:
                nge.append(stack[-1])
            else:
                nge.append(-1)

            stack.append(arr[i])
        
        nge = nge[::-1] 
        res = []

        for i in range(len(nums1)):
            res.append(nge[arr.index(nums1[i])])
        
        return res

if __name__ == "__main__":
    sol = Solution()
    nums1 = [4, 1, 2]
    arr = [1, 3, 4, 2]
    result = sol.nextGreaterElement(nums1, arr)
    print("Next Greater Elements for nums1 in arr:", result)
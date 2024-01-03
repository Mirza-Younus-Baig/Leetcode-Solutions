from typing import List

class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        h = dict()
        arr = list()
        for i in nums:
            if i in h:
                h[i] += 1
            else:
                h[i] = 0
            
            if h[i] >= len(arr):
                arr.append([i])
            else:
                arr[h[i]].append(i)
        return arr


from typing import List

class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        x = sorted(set([i[0] for i in points]))
        
        maxWidth = 0
        for i in range(len(x) - 1):
            if x[i+1] - x[i] > maxWidth:
                maxWidth = x[i+1] - x[i]
        

        return maxWidth


        
obj = Solution()
# points = [[8,7],[9,9],[7,4],[9,7]]
points = [[3,1],[9,0],[1,0],[1,4],[5,3],[8,8]]
print(obj.maxWidthOfVerticalArea(points))

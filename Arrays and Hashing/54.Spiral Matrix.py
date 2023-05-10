from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                print(matrix[i][j])



res = Solution()
inp = [[1,2,3],[4,5,6],[7,8,9]]

print(res.spiralOrder(inp))
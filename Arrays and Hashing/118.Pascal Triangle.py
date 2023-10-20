''' Three possible questions

1. Given row and column, find the element at that position.
2. Given row, print the entire row elements.
3. Given number of rows, print the entire pascal triangle.
'''

from typing import List
from math import ceil 

class Solution:
    def elementAtPos(self, row: int, col: int) -> int:
        # rowCcol (nCr)
        res = 1
        for i in range(col - 1):
            res = res * (row - i - 1)
            res = res / (i+1)
        return res
        
    def printRow(self, row: int) -> List[int]:
        # TC: O(n2)
        # res = [1]
        # if row < 2:
        #     return res
        # for i in range(2, row):
        #     res.append(self.elementAtPos(row - 1, i - 1))
        # res.append(1)
        # return res

        # Optimal Solution
        # TC: O(n)
        res = [1]
        ans = 1
        for i in range(1, row):
            ans *= (row - i) 
            ans //= i
            res.append(ans)
        
        return res

    
    def generate(self, numRows: int) -> List[List[int]]:
        ans = []
        for i in range(1, numRows + 1):
            ans.append(self.printRow(i))
        
        return ans



if __name__ == "__main__":
    obj = Solution()

    # Problem 1
    row = 5
    col = 3
    print(obj.elementAtPos(row, col))


    # Problem 2
    row = 12
    print(obj.printRow(row))

    # # Problem 3
    n = 6
    print(obj.generate(n))
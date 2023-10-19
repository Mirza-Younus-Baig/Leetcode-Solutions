''' Three possible questions

1. Given row and column, find the element at that position.
2. Given row, print the entire row elements.
3. Given number of rows, print the entire pascal triangle.
'''

from typing import List

class Solution:
    def elementAtPos(self, row: int, col: int) -> int:
        # rowCcol (nCr)
        res = 1
        for i in range(col):
            res = res * (row - i)
            res = res / (i+1)
            # row -= 1e
        return res
        pass
        
 
    def printRow(self, row: int) -> List[int]:
        res = [1]
        if row < 2:
            return res
        for i in range(2, row):
            res.append(self.elementAtPos(row - 1, i - 1))
        res.append(1)
        return res
    
    def generate(self, numRows: int) -> List[List[int]]:
        pass



if __name__ == "__main__":
    obj = Solution()

    # Problem 1
    row = 5
    col = 3
    print(obj.elementAtPos(row - 1, col - 1))


    # Problem 2
    row = 6
    print(obj.printRow(row))

    # # Problem 3
    # n = 6
    # print(obj.generate(n))
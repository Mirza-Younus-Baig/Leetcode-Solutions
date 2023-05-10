from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # Intialize the 4 directions of the matrix
        top = 0
        bottom = len(matrix) - 1
        right = len(matrix[0]) - 1
        left = 0
        
        # Create an array to store the resultant array
        res = []

        # Iterate until you have no rows and columns
        while top <= bottom and left <= right:

            # Since Python ranges are not inclusive, we have to consider adding or substracting 1 to allow complete matrix ranges. 

            # Iterate from left to right
            # We have the top as constant as the row number
            for i in range(left, right + 1):
                res.append(matrix[top][i])
            # Now, we can move to the next row
            # Increment top by 1 to move to the next row
            top += 1
            
            # Iterate from top to bottom
            # We have right as the constant column number
            for i in range(top, bottom + 1):
                res.append(matrix[i][right])
            # Now, we can elimiate the right column
            # Decrement right by 1 to move to the previous column
            right -= 1

            # In case where we have no more rows to print, 
            # We need to check if the top is still less than or equal to bottom
            if top <= bottom: 
                # Iterate from right to left
                # We have the bottom as constant as the row number
                for i in range(right, left - 1, -1):
                    res.append(matrix[bottom][i])
                # Now, we can elimiate the bottom row
                # Decrement right by 1 to move to the previous row  
                bottom -= 1

            # In case where we have no more columns to print, 
            # We need to check if the left is still less than or equal to right
            if left <= right:
                # Iterate from bottom to top
                # We have the left as constant as the column number
                for i in range(bottom, top - 1, -1):
                    res.append(matrix[i][left])
                # Now, we can elimiate the left column
                # Increment left by 1 to move to the next column  
                left += 1

        return res
    


if __name__ == "__main__":
    res = Solution()
    inp = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
    print(res.spiralOrder(inp))
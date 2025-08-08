from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        low = 0
        high = len(matrix) - 1
        
        while low < high:
            row = (low + high) // 2
            if target > matrix[row][-1]:
                low = row + 1
            elif target < matrix[row][0]:
                high = row - 1
            else:
                break
        
        row = (low + high) // 2    

        low = 0
        high = len(matrix[row]) - 1
        

        if target < matrix[row][0] or target > matrix[row][-1]:
            return False

        while low <= high:
            mid = (low + high) // 2
            if target == matrix[row][mid]:
                return True
            elif target < matrix[row][mid]:
                high = mid - 1
            else:
                low = mid + 1
        
        return False



if __name__ == "__main__":
    mat = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
    print(Solution().searchMatrix(mat, 1))
    print(Solution().searchMatrix(mat, 25))
    print(Solution().searchMatrix(mat, 16))
    print(Solution().searchMatrix(mat, 19))
    print(Solution().searchMatrix(mat, 21))
    print(Solution().searchMatrix(mat, 25))
from typing import List

# Partial implementation
# Fails at test case: [[13,13], [13, 13]]

class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        gridLen = len(grid)
        res = 0

        rowDict = dict()
        for i in range(gridLen):
            temp = '@'.join(map(str, grid[i]))
            rowDict[temp] = rowDict.get(temp, 0) + 1
        print(rowDict)

        colDict = dict()
        colList = [[] for _ in grid]
        for i in range(gridLen):
            for j in range(gridLen):
                colList[j].append(grid[i][j])
        
        for i in range(gridLen):
            temp = '@'.join(map(str, colList[i]))
            colDict[temp] = colDict.get(temp, 0) + 1

        # print(colList)
        print(colDict)

        dictl = max(len(rowDict), len(colDict))

        for i in rowDict.keys():
            if i in colDict:
                res += max(rowDict[i], colDict[i])
    

        
        return res

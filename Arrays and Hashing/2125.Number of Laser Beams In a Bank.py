from typing import List

class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        res = 0
        prevCount = 0
        currCount = 0
        for i in range(len(bank)):
            currCount = bank[i].count('1')
            print(prevCount, currCount)
            if currCount: 
                if prevCount:
                    res += prevCount * currCount
                
                prevCount = currCount
        return res
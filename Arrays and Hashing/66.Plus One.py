# import List
from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        ind = len(digits) - 2
        carry = (digits[-1] + 1) // 10
        digits[-1] = (digits[-1] + 1) % 10
        

        while carry and ind > -1:
            carry = (digits[ind] + 1) // 10
            digits[ind] = (digits[ind] + 1) % 10
            ind -= 1
        if carry:
            digits.insert(0, 1)
        

        return digits


res = Solution()
print(res.plusOne([9,9,9,9]))


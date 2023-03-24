from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        for i in range(len(prices)):
            maxn = max(prices[i:]) - prices[i]
            if maxProfit < maxn:
                maxProfit = maxn
            


        return maxProfit


res = Solution()

inp = [7,1,3,5,6,4]

print(res.maxProfit(inp))

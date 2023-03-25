from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Brute force solution
        # maxProfit = 0
        # for i in range(len(prices)):
        #     maxn = max(prices[i:]) - prices[i]
        #     if maxProfit < maxn:
        #         maxProfit = maxn

        # return maxProfit
        l, r = 0, 1
        maxp = 0
        while r < len(prices):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxp = max(maxp, profit)
            else:
                l = r
            
            r += 1
        return maxp

res = Solution()

inp = [7,1,3,5,6,4]

print(res.maxProfit(inp))

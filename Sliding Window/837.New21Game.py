

class Solution:
    def new21Game (self, n: int, k: int, maxPts: int) -> float:
        if k == 0:
            return 1.0
      
        windowSum = 0
        for i in range(k, k + maxPts) :
            windowSum += 1 if i <= n else 0
        
        dp = dict() 
        for i in range(k - 1, -1, -1):
            dp[i] = windowSum / maxPts
            remove = 0
            if i + maxPts <= n:
                remove = dp.get(i + maxPts, 1)
            windowSum += dp[i] - remove
        
        return dp[0]
    
if __name__ == "__main__":
    res = Solution()

    n = 6
    k = 1
    maxPts = 10

    print(res.new21Game(n, k, maxPts))


class Solution:
    def climbingStairs(self, n : int) -> int:
        var1, var2 = 1, 1

        for i in range(n - 1):
            var1, var2 = var1 + var2, var1
        
        return var1


if __name__ == "__main__":
    res = Solution()
    inp = 5

    print(res.climbingStairs(inp))
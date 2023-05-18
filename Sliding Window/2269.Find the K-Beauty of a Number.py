
class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        nums = str(num)
        
        beauty = 0

        for i in range(len(nums) - k + 1):
            
            val = int(nums[i:i+k])

            if val and num % val == 0:
                beauty += 1

        del nums

        return beauty



if __name__ == "__main__":
    res = Solution()

    inp = 430043
    k=2

    print(res.divisorSubstrings(inp, k))

from typing import List

class Solution: 
    def sortedArray(self, a: List[int], b: List[int]) -> List[int]:
        # Write your code here

        # Approach 1 
        # return sorted(set(a).union(set(b)))


        # Approach 2

        res = []
        i, j = 0, 0
        m ,n = len(a), len(b)

        while i < m and j < n:
            if a[i] <= b[j]:
                if len(res) == 0 or res[-1] != a[i]:
                    res.append(a[i])
                i += 1
            elif b[j] < a[i]:
                if len(res) == 0 or res[-1] != b[j]:
                    res.append(b[j])
                j += 1

        while i < m:
            if res[-1] < a[i]:
                res.append(a[i])
            
            i += 1

        while j < n:
            if res[-1] < b[j]:
                res.append(b[j])
            
            j += 1

        return res
    
if __name__ == "__main__":

    # a = [1,3,4,5,6,7]
    # b = [2,3,5,7,9]
    
    # 2 3 5 5 6 8 8 9
    # 1 5 7 7 9 10
    
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    print(Solution().sortedArray(a, b))
from collections import Counter

class Solution:
    def minDeletions(self, s: str) -> int:
        cnt, res, used = Counter(s), 0, set()
        for _, freq in cnt.items():
            while freq > 0 and freq in used:
                freq -= 1
                res += 1
            used.add(freq)
        return res
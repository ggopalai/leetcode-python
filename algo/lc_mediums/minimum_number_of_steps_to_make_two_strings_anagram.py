class Solution:
    def minSteps(self, s: str, t: str) -> int:
        from collections import Counter
        c1 = dict(Counter(s))
        c2 = dict(Counter(t))
        n = len(s)

        # anagrams already
        if c1 == c2:
            return 0
        
        matchCount = 0
        for k in t:
            if k in c1:
                matchCount += 1
                c1[k] -= 1
                if c1[k] == 0:
                    del c1[k]

        return n - matchCount
        
        
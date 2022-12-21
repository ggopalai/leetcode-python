# 163/164 cases - didn't cleat some exceptioally bug number depsite modulo
class Solution:
    def numWays(self, s: str) -> int:
        n = len(s)
        count = [0] * len(s)
        c = 0
        for i in range(len(s)):
            if s[i] == '1':
                c += 1
            count[i] = c
        
        # special case. all 0s. research a bit more on why this is the case. 
        if c == 0:
            return ((n - 1) * (n - 2) // 2) % (10 ** 9 + 7)
        
        if count[-1] % 3:
            return 0

        pg = c // 3
        
        p, q = c - pg, c - 2 * pg
        cp, cq = 0, 0

        for i in count:
            if i == p:
                cp += 1
            if i == q:
                cq += 1


        return cp * cq
# My sol - passed 32/37 cases. Failing for cases with k = 0 and all same chars. eg AAAA k = 0
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 1
        d = collections.defaultdict(int)
        l, r = 0, 1
        d[s[l]] = 1
        while r < len(s):
            lw = r - l + 1
            if (lw - max(d.values())) <= k:
                res = max(res, lw)
                r += 1
                if r == len(s):
                    return res
                d[s[r]] += 1
            else:
                if l == len(s):
                    return res
                d[s[l]] -= 1
                l += 1
        
        return res
        
# neetcode sol - 
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        d = collections.defaultdict(int)
        l = 0
        # right pointer is gonna increment either ways.
        for r in range(len(s)):
            d[s[r]] += 1
            
            # increment left if no swaps are possible
            if (r - l + 1 - max(d.values())) > k:
                d[s[l]] -= 1
                l += 1
            
            # reset length
            res = max(res, r - l + 1)
        
        return res
        
        
        
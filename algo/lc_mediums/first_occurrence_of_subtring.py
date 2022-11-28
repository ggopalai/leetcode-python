class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        hl = len(haystack)
        nl = len(needle)
        
        #empty needle is always in the haystack
        if not nl:
            return 0
        
        if hl < nl:
            return -1
        
        for i in range(hl - nl + 1):
            if haystack[i: i+nl] == needle:
                return i
        
        return -1
        
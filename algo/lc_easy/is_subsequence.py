# 1. My solution
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) > len(t):
            return False
        if len(s) == 0:
            return True
        
        i, j = 0, 0
        
        while j < len(t):
            if s[i] == t[j]:
                i += 1
                if i == len(s):
                    return True
            j += 1
        
        return False
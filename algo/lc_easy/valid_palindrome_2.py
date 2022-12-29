class Solution:
    def validPalindrome(self, s: str) -> bool:
        def checkPal(s, i ,j):
            while i < j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1    
            return True
        
        l, r = 0, len(s) - 1
        while l < r:
            # when there is a mismatch, check with both options. 
            if s[l] != s[r]:
                return checkPal(s, l + 1, r) or checkPal(s, l, r - 1)
            l += 1
            r -= 1
        
        return True
        
        
        
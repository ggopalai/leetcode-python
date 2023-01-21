class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        
        # odd length palindromes 
        for i in range(len(s)):
            l, r = i, i
            while (l > -1 and r < len(s) and s[l] == s[r]):
                res += 1
                l -= 1
                r += 1
        
        # even length palindromes
        for i in range(len(s) - 1):
            l, r = i, i + 1
            while (l > -1 and r < len(s) and s[l] == s[r]):
                res += 1
                l -= 1
                r += 1
        
        return res
            
        
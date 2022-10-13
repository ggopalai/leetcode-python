class Solution:
    def longestPalindrome(self, s: str) -> str:
        le = len(s)
        ls = ""
        
        for i in range(0, le):
            
            #odd length palindromic subtring
            l, r = i, i  
            while l > -1 and r < len(s) and s[l] == s[r]:
                cur = s[l:r+1]
                if len(ls) < len(cur):
                    ls = cur
                l -= 1
                r += 1
            
            #even length palindromic subtring
            l, r = i, i + 1
            while l > -1 and r < len(s) and s[l] == s[r]:
                cur = s[l:r+1]
                if len(ls) < len(cur):
                    ls = cur
                l -= 1
                r += 1

        
        return ls
            
        
        
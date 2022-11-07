class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        if len(palindrome) < 2:
            return ""
        
        t = list(palindrome)
        # change the first non-a to a. 
        for i in range(len(t)):
            if t[i] != 'a':
                t[i] = 'a'
                break
        
        # for edge cases with non-a in the middle (or all a's), change last letter to b. 
        if t == t[::-1]:
            t = list(palindrome)
            t[-1] = 'b'
            
        return "".join(t)
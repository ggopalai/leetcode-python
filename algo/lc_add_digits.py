"""
https://leetcode.com/problems/add-digits/
"""

class Solution:
    def adds(self, num: int) -> int:
        res = 0
        a = list(str(num))
        for i in a:
            res += int(i)        
        return res
    
    def addDigits(self, num: int) -> int:
        x = num 
        while x > 9: 
            x = self.adds(x)
            if x < 10:
                return x
        
        return x
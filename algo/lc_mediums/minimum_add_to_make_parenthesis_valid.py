# greedy
class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        if not s:
            return 0
        res = 0
        c = 0
        for i in s:
            if i == '(':
                c += 1
            else:
                if c > 0:
                    c -= 1
                else:
                    res += 1
        
        res += c

        return res            

        
        
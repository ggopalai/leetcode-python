class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1: return s
        
        res = ""
        #the next char in the same row in the zigzag formation
        inc = 2 * (numRows - 1)

        for r in range(numRows):
            for i in range(r, len(s), inc):
                res += s[i]
                #zigzag elements for middle rows
                if r > 0 and r < numRows - 1 and i + inc - 2 * r < len(s):
                    res += s[i + inc - 2 * r]
        
        return res
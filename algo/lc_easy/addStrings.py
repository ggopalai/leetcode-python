class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        a = list(num1[::-1])
        b = list(num2[::-1])
        res = ""
        i = j = 0
        carry = 0
        
        while i < len(a) or i < len(b) or carry:
            
            z = int(a[i]) if i < len(a) else 0
            x = int(b[j]) if j < len(b) else 0
            
            val = z + x + carry
            dig = val % 10
            carry = val // 10
            
            res = str(dig) + res
            
            i += 1
            j += 1
            
        return res
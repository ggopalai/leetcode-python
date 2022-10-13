#works for most cases, but TLE for corner cases with big numbers. 
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        count = 0
        
        num = abs(divisor)
        numCount = num
        dend = abs(dividend)
        
        while num <= dend:
            count += 1
            num += numCount   
        
        return count if (dividend * divisor > 0) else (count * -1)


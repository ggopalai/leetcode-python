"""
https://leetcode.com/problems/power-of-two/
"""
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 1:
            return True
        x = n
        
        while x:
            a = x % 2
            x = x / 2
            if a > 0:
                return False
            if x == 1:
                return True
               

# Follow up with a non-iterative solution -> can be done by checking bits? every power of 2 will have only one '1' bit in its binary representation. 
            
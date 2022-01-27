class Solution:
    def square(self, x, i, j):
        mid = (i+j)/2
        m = mid * mid

        if m == x or abs(m - x) < 0.00001:   #binary search once we identify least n for which n * n > num, 0.00001 = precision upto 5 decimal points
            return mid
        elif m < x:
            return self.square(x, mid, j)
        else:
            return self.square(x, i, mid)
        
    def mySqrt(self, x: int) -> int:
        i = 1
        found = False
        
        while not found:
            if i * i == x:
                found = True
                return i
            elif i * i > x:
                return self.square(x, i-1, i)  #identify least n for which n * n > num 
            else:
                i += 1



# Faster solution from LC. Check this out. Does this work only becase the lc question expects truncated values? 
class Solution:
    def mySqrt(self, x: int) -> int:
        
        left, right = 0, 2**16
        
        while left < right:
            mid = left + (right - left + 1) // 2
            if mid ** 2 <= x:
                left = mid
            else:
                right = mid - 1
                
        return left
            
        
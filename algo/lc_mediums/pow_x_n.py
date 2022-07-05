#linear times out. this gives log n complexity. 
class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        
        def fastPow(x: float, n: int) -> float:
            if n == 0:
                return 1
            half = fastPow(x, n // 2)
            if n % 2 == 0:
                return half * half
            else:
                return x * half * half 
        
        if n < 0:
            x = 1 / x
            n = -n
        return fastPow(x, n)


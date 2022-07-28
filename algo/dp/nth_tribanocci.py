from turtle import up


# 1. Bottom up
class Solution:
    def tribonacci(self, n: int) -> int:
        
        #base cases
        if n == 0 or n == 1:
            return n
        if n == 2:
            return n-1
        
        #array to store values
        dp = [0] * (n+1)
        dp[0] = 0
        dp[1] = 1
        dp[2] = 1
        
        #recurrence relation
        for i in range(3, n+1):
            dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
        
        return dp[n]

# 2. Top down 
class Solution:
    def tribonacci(self, n: int) -> int:
        h = {}
        
        def dp(n):
            
            if n == 0 or n == 1:
                return n
            if n == 2:
                return n-1
            if n not in h:
                h[n] = dp(n-1) + dp(n-2) + dp(n-3)
            
            return h[n]
        
        return dp(n)
        
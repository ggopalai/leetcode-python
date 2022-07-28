# 1. Bottom-up solution
class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        
        #base cases
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums[0], nums[1])
        
        #array to store max uptil that house
        dp = [0] * n
        
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        
        #recurrence relation
        for i in range(2, len(nums)):
            dp[i] = max(dp[i-1], dp[i-2] + nums[i])
                
        return dp[n-1]

# 2. Top-down solution
class Solution:
    def rob(self, nums: List[int]) -> int:
        h = {}
        
        def dp(n):
            
            #base cases
            if n == 1:
                return nums[0]
            if n == 2:
                return max(nums[0], nums[1])
            
            #memoization + recurrence relation
            if n not in h:
                h[n] = max(dp(n-1), dp(n-2) + nums[n-1])
            
            
            return h[n]
        
        return dp(len(nums))
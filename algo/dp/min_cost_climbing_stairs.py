# 1. Bottom up
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        dp = [0] * (n+1)
        if n == 2:
            return min(cost[0], cost[1])
        
        #base cases
        dp[0] = 0
        dp[1] = 0
        
        #recurrence
        for i in range(2, n+1):
            dp[i] = min(dp[i-1] + cost[i-1], (dp[i-2] + cost[i-2]))
        
        
        return dp[n]

# 2. Top down?
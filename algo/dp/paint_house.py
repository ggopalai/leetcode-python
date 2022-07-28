class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        #base case
        if len(costs) == 1:
            return min(costs[0])
        
        c = [[0 for j in range(3)] for i in range(len(costs))]
        
        #first house
        for i in range(3):
            c[0][i] = costs[0][i]
            
        for i in range(1, len(costs)):
            for j in range(3):
                if j == 0:
                    a, b = 1, 2
                elif j == 1:
                    a, b = 0, 2
                else:
                    a, b = 0, 1
                c[i][j] = costs[i][j] + min(c[i-1][a], c[i-1][b])
        
        return min(c[len(costs)-1])

# Memory optimized - we only need the values of previous row to compute costs of current row. so keep just 1 row and update for each house. 
class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        
        dp = [0] * 3
        
        for i in range(len(costs)):
            dp0 = costs[i][0] + min(dp[1], dp[2])
            dp1 = costs[i][1] + min(dp[0], dp[2])
            dp2 = costs[i][2] + min(dp[0], dp[1])
            dp = [dp0, dp1, dp2] #update dp with current house for next house to use. 
                    
        return min(dp)
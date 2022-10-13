class Solution:
    def numSquares(self, n: int) -> int:
        dp = [n] * (n+1) #n because the max number of ways would be n 1s.
        dp[0] = 0
        
        # bottom-up dp, start building the sub-problems first
        # for each number, check till the least perfect square below the target number. 
        for target in range(1, n + 1):
            for s in range(1, target + 1):
                square = s * s
                if square > target:
                    break
                dp[target] = min(dp[target], 1 + dp[target - square])
        
        return dp[-1]
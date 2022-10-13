class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount + 1] *  (amount + 1) #any val above the amount itself should be fine, as we cant use more coins than the amount itself. 
        dp[0] = 0 #base case
        
        for i in range(1, amount + 1):
            for a in coins:
                if i - a >= 0:
                    dp[i] = min(dp[i], 1 + dp[i - a])
        
        return dp[amount] if dp[amount] != amount + 1 else -1
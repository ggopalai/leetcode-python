class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        #2d array of length text1+1 and text2+1 (+1 is to store 0s that we compute the matrix values from.)
        dp = [[0 for j in range(len(text2) + 1)] for i in range(len(text1) + 1)]
        
        #start filling up matrix in reverse.
        for i in range(len(text1) - 1, -1, -1):
            for j in range(len(text2) - 1, -1, -1):
                #if characters match, add 1 + value from diagonal tile. 
                #(if we did not do in reverse, we mark and move diagonally down, this basically moves pointers from both chars)
                if text1[i] == text2[j]: 
                    dp[i][j] = 1 + dp[i+1][j+1]
                #if not done in reverse, we would check both cases (keep one char and move in other and vice-versa)
                else: #if not, max between 
                    dp[i][j] = max(dp[i+1][j], dp[i][j+1])
                
        return dp[0][0]
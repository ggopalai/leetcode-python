# 1. Leetcode solution
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        l = len(s)
        dp = [False] * l
        
        for i in range(l):
            for w in wordDict:
                # i >= len(w) - 1 : length check
                # i == len(w) - 1 : for the first word match
                # dp[i - len(w)] : building on top on the previous matches
                if i >= len(w) - 1 and (i == len(w) - 1 or dp[i - len(w)]):
                    if s[i - len(w) + 1: i+1] == w: #match the word
                        dp[i] = True
        
        return dp[-1]

# 2. Neetcode - bottom-up but in reverse.
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        l = len(s)
        dp = [False] * (l + 1)
        dp[l] = True
        
        for i in range(l - 1, -1, -1):
            for w in wordDict:
                if (i + len(w)) <= l and s[i : i + len(w)] == w:
                    dp[i] = dp[i + len(w)]
                if dp[i]:
                    break
        
        return dp[0]
        
        
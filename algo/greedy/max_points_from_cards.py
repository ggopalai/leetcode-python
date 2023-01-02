# 37/40, TLE for 3.
class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        cards = []
        l, r = 0, len(cardPoints) - 1
        
        while len(cards) < k:
            remCards = k - len(cards)
            lSum = sum(cardPoints[l: l + remCards])
            rSum = sum(cardPoints[r - remCards + 1:  r + 1])
            if lSum > rSum:
                cards.append(cardPoints[l])
                l += 1
            else:
                cards.append(cardPoints[r])
                r -= 1
        
        return sum(cards)

# 38/40
class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        # basecase 
        if n == k:
            return sum(cardPoints)
        
        l, r = 0, n - k - 1
        minSum = sum(cardPoints[l:r + 1])
        
        while r < n:
            curSum = sum(cardPoints[l : r + 1])
            minSum = min(minSum, curSum)
            r += 1
            curSum -= cardPoints[l]
            l += 1
        
        return sum(cardPoints) - minSum

# accepted 
class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        # basecase 
        if n == k:
            return sum(cardPoints)
        
        l, r = 0, n - k - 1
        
        curSum = sum(cardPoints[l: r + 1])
        minSum = curSum
        
        while r < n:
            r += 1
            curSum += cardPoints[r]
            curSum -= cardPoints[l]
            l += 1
            minSum = min(minSum, curSum)
            if r == n - 1:
                break
        
        return sum(cardPoints) - minSum
            
        
            
       
            
            
        
            
       
            
            
#1. Bottom-up. 
class Solution:
    def numWays(self, n: int, k: int) -> int:
        if n == 1:
            return k
        if n == 2:
            return k * k 
        
        total = [k] + [k * k] + [0] * (n-2)
        
        for i in range(2, n):
            total[i] = (k-1) * (total[i-1] + total[i-2])
        
        return total[-1]

#Recurrence explanation - 

"""
For the first 1st fence, we have k options. 
For the second fence, total ways = k * k, by permutations.
For n = 3 onwards, we have 2 decisions for each fence. 
    1. Paint the fence a different color than previous fence.
        For this, we have k - 1 options. so total becomes (k-1) * total[i-1]
    2. Paint same color as previous fence.
        Number of ways = 1 * total[i-1]. But, because we have a restriction saying we can't
        paint 3 or more houses same color, we need to find in how many ways we can paint i-1th fence
        differently than i-2th fence. 
        this can be done in (k - 1) * total[i-2]. Substituting that in above equation - 
        1 * total[i - 1] = 1 * (k-1) * total[i-2] = (k-1) * total[i-2].
    
    so total = (k-1) * total[i-1] + (k-1) * total[i-2]
             = (k-1) * (total[i-1] + total[i-2])
"""
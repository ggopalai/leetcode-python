"""
The idea is to find the min of max heights to the left and right of the current position. this is because, the min height is the bottleneck. 
"""
# 1.  DP, Linear space and time. 
class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        leftMax = [None] * n
        rightMax = [None] * n
        leftMax[0] = height[0]
        rightMax[n-1] = height[n-1]
        res = 0
        
        for i in range(1, n-1):
            leftMax[i] = max(leftMax[i-1], height[i])
            rightMax[n-i-1] = max(rightMax[n-i], height[n-i-1])
        
        for i in range(1, n-1):
            res += min(leftMax[i], rightMax[i]) - height[i]
        
        return res

# 2. Two-pointer linear time, constant space.
# Intuition - Because we know that the bottleneck is caused by the min height, at any given time if we know that the max upto now is less on the left side, we dont need
# know the right max because already have the minimum (and vice-versa).
class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        maxLeft, maxRight = height[l], height[r]
        res = 0
        
        while l < r:
            if maxLeft <= maxRight:
                l += 1
                maxLeft = max(maxLeft, height[l])
                res += maxLeft - height[l]
            else:
                r -= 1
                maxRight = max(maxRight, height[r])
                res += maxRight - height[r]
        
        return res
        
        
        
        
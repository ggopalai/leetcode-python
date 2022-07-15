class Solution:
    def maxArea(self, height: List[int]) -> int:
        res = 0 
        l, r = 0, len(height) - 1
        
        while l < r:
            area = (r - l) * min(height[l], height[r]) #area with least height the limiting factor
            res = max(res, area)
            if height[l] < height[r] or height[l] == height[r]: #as height is limiting, move the lesser. 
                l += 1
            else:
                r -= 1
        
        return res
        
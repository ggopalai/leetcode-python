class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        curMin, curMax = 1, 1 #maintain the min and max until the previous index. 
        res = max(nums) #single element in array
        for i in nums:
            if not i:
                curMin, curMax = 1, 1
            
            tmp = i * curMin 
            curMin = min(i * curMin, i * curMax, i) 
            curMax = max(tmp, i * curMax, i)
            if curMax > res:
                res = curMax
        
        return res
            
        
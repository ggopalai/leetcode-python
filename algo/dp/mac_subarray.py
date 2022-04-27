class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cmax = nums[0] # current or local maximum
        gmax = nums[0] # global maximum
        
        for i in range(1, len(nums)):
            cmax = max(nums[i], cmax + nums[i])
            if cmax > gmax:
                gmax = cmax
        
        return gmax
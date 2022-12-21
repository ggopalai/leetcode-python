class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        # sort because we can only increment. 
        nums.sort()

        total, res = 0, 0
        l, r = 0, 0
        while r < len(nums):
            total += nums[r]

            # invalid window, decrease size. 
            while nums[r] * (r - l + 1) > total + k:
                total -= nums[l]
                l += 1
            
            # valid window
            res = max(res, r - l + 1)
            r += 1
        
        return res
                

        
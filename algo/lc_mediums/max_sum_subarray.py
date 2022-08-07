# 1. Kadane's algo, linear runtime.
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        c = [nums[0]] + [0] * (len(nums) - 1)
        for i in range(1, len(nums)):
            c[i] = max(nums[i], c[i-1] + nums[i]) #idea is to find the max until that position 
            # which is the maximum between the number itself or number + max till previous.
        
        return max(c)
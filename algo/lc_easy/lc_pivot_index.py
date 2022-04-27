class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        ls = 0
        
        for i in range(0, len(nums)):
            if ls == total - ls - nums[i]:
                return i
            
            ls += nums[i]
            
        return -1 
        
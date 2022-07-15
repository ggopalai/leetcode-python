#naive approach, times out. 
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = list()
        while n:
            ind = 1
            for i in range(len(nums)):
                 if i != len(nums) - n:
                        ind *= nums[i]
            res.append(ind)
            n -= 1
        
        return res
                        
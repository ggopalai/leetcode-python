class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        l = 0
        r = len(nums) - 1
        
        res = [0] * len(nums)
        
        for i in range(len(nums)-1, -1, -1):
            if abs(nums[l]) > abs(nums[r]):
                res[i] = nums[l] * nums[l]
                l += 1
            else:
                res[i] = nums[r] * nums[r]
                r -= 1
        
        return res

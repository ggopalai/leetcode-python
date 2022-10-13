# 1,2,3,4,5 ; k = 2
# 5,4,3,2,1
# 4,5,1,2,3
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        
        def rev(nums, l, r):
            while l <= r:
                nums[l], nums[r] = nums[r], nums[l]
                l, r = l + 1, r - 1
        
        rev(nums, 0, len(nums) - 1)
        rev(nums, 0, k - 1)
        rev(nums, k, len(nums) - 1)
        
                
        
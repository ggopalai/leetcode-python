class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l = 0
        r = len(nums) - 1
        
        def bs(nums, l, r, leftbias):
            i = -1
            while l <= r:
                mid = (l + r) // 2
                #once you find the target, keep pushing to left or right to find the first/last index.
                if nums[mid] == target:
                    i = mid
                    if leftbias:
                        r = mid - 1
                    else:
                        l = mid + 1
                elif target > nums[mid]:
                    l = mid + 1
                else:
                    r = mid - 1
            
            return i
        
        a = bs(nums, l, r, True)
        b = bs(nums, l, r, False)
        
        return [a, b]
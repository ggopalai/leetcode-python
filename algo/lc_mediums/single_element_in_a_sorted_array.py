class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l + r) // 2

            if mid == len(nums) - 1 or mid == 0 or (nums[mid] != nums[mid - 1] and nums[mid] != nums[mid + 1]):
                return nums[mid]
            
            # second of the pair
            if nums[mid] == nums[mid - 1]:
                if mid % 2:
                    l = mid + 1
                else:
                    r = mid 
            #first of the pair
            else: 
                if mid % 2:
                    r = mid
                else:
                    l = mid + 1
            


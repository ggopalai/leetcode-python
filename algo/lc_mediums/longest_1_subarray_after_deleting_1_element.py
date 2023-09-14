class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        # edge cases
        # if sum of array = len, return len - 1
        if sum(nums) == len(nums):
            return sum(nums) - 1
        # no 1s
        if sum(nums) == 0:
            return 0
        
        res = 0
        l, r = 0, 1
        c = 1 if nums[l] == 0 else 0
        # sliding window
        while r < len(nums):
            if nums[r] == 0:
                c += 1
            # when you get the 2nd zero, move the left pointer
            while c > 1:
                if nums[l] == 0:
                    c -= 1
                l += 1
            res = max(res, r - l)
            r += 1


        return res
            

        

        

                
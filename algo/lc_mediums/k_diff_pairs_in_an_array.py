class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        nums.sort()

        l, r = 0, 1
        count = 0

        while l < len(nums) and r < len(nums):
            if (l == r) or nums[r] - nums[l] < k:
                r += 1
            elif nums[r] - nums[l] > k:
                l += 1
            else:
                count += 1
                l += 1
                r += 1
                while l < len(nums) and nums[l] == nums[l - 1] :
                    l += 1
        
        return count

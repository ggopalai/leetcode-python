class Solution:
    """
    Time - O(N ^ 2)
    """
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        n = len(nums)
        res = []
        
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] < k:
                    res.append(nums[i] + nums[j])
        
        if not res:
            return -1
        else:
            res.sort()
            return res[-1]

# n log n 
class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        n = len(nums)
        ans = -1
        nums.sort()
        
        for i in range(n - 1):
            j = bisect.bisect_left(nums, k - nums[i]) - 1
            if j > i:
                ans = max(ans, nums[i] + nums[j])
        
        return ans
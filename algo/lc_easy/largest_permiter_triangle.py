class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        s = sorted(nums, reverse=True)
        for i in range(0, len(nums) - 2):
            if s[i] < (s[i+1] + s[i+2]):
                return sum([s[i], s[i+1], s[i+2]])
            
        return 0
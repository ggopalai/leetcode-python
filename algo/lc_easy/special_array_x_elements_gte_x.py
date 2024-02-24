class Solution:
    def specialArray(self, nums: List[int]) -> int:
        import bisect
        nums.sort()
        l, r = 0, nums[-1]
        li = len(nums)

        for i in range(l, r + 1):
            idx = bisect.bisect_left(nums, i)
            if li - idx == i:
                return i
        
        return -1
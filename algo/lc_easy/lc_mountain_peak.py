# https://leetcode.com/problems/peak-index-in-a-mountain-array/

# Runtime: 64 ms, faster than 99.18% of Python3 online submissions for Peak Index in a Mountain Array.
# Memory Usage: 15.3 MB, less than 62.62% of Python3 online submissions for Peak Index in a Mountain Array.

class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        return arr.index(max(arr))
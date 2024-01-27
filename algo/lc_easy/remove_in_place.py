"""
Reader-writer concept for in place operations. 
Read everythig, but write selectively.
Time - O(N)
"""
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        reader, writer = 0, 0

        while reader < len(nums):
            if nums[reader] != val:
                nums[writer] = nums[reader] 
                writer += 1
            reader += 1
        
        return writer

# try to make each side lesser or greater.
# one way to to this - sort, place first half of array with a gap in
# between. fill up this spots with the second half. 
class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        nums.sort()
        l = len(nums)
        n = (l // 2) if l % 2 == 1 else (l // 2 - 1)
        
        fh = nums[: n + 1]
        sh = nums[n + 1:]
        
        j = 0
        for i in range(0, l, 2):
            nums[i] = fh[j]
            j += 1
        
        j = 0
        for i in range(1, l, 2):
            nums[i] = sh[j]
            j += 1              
        
        return nums
        
        
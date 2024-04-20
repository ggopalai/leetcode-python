class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        ml, count = 0, 0
        hm = {}
        hm[count] = -1

        for i, val in enumerate(nums):
            if val:
                count += 1
            else:
                count -= 1
            
            if count in hm:
                ml = max(ml, i - hm[count])
            else:
                hm[count] = i
        
        return ml




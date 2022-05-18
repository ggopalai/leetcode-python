# https://leetcode.com/problems/find-all-duplicates-in-an-array/
# o(n) and constant space 

from typing import List


class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        res = set()
        for i in nums:
            if nums[abs(i)-1] < 0: #negative imples number being visited already, so add. 
                res.add(abs(i))
            nums[abs(i)-1] *= -1 #first visit. 
            
        
        return res
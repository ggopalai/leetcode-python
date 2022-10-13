# 1. Linear time and space. 
from ast import Constant


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        d = {}
        
        for i in nums:
            if i not in d:
                d[i] = 1
            else:
                d[i] += 1
        
        for i in d.values():
            if i > 1:
                return True
        
        return False

# 2. Constant space but nlogn n time
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                return True
        
        return False
        
        

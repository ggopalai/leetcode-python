# https://leetcode.com/problems/single-number/


# naive solution - linear time and linear space. 
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        d = dict()
        
        for i in nums:
            if i not in d:
                d[i] = 1
            else:
                d[i] += 1
            
        for i in d.items():
            if i[1] == 1:
                return i[0]


# how to solve with constant space? 
# 
# have to use xor property for this. xor every number -> all duplicates will cancel each other out, leaving the single number.             
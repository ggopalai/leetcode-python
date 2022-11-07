# 1. nlogn solution - 
# Sort the array - keep checking for the next possible missing number. 

# But, if we know that (next line), then the need for sorting goes away.  
# The missing number must be in the range 1 to len(nums) + 1. 
# Test this out mathematically. If all numbers within 1 to len(A) are present, then the next element. 
# If not, it has be some element within the range itself. 
# 2. Linear time and space - 
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        m = set(nums)
        
        for i in range(1, len(nums) + 2):
            if i not in m:
                return i

# Linear time and constant space - 
# We somehow need to eleminate the extra set and utilize the input array itself as reference. 
# Notice also, that the negative numbers are pretty useless to this problem and can be reset to 0. 


        
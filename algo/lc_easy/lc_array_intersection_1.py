# https://leetcode.com/problems/intersection-of-two-arrays

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        a = set()
        
        for i in nums1:
            if i in nums2:
                a.add(i)
        
        return a 


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        a = set(nums1)
        b = set(nums2)
        
        return a.intersection(b) #or use a & b -> & is the intersection operator for sets. 
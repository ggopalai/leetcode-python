# https://leetcode.com/problems/two-out-of-three/

# Runtime: 176 ms, faster than 5.16% of Python3 online submissions for Two Out of Three.
# Memory Usage: 14.2 MB, less than 66.99% of Python3 online submissions for Two Out of Three.

class Solution:
    def linSearch(self, key: int, nums: List[int]):
        for i in nums:
            if i == key:
                return True
        return False

    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        a = set()
        
        for i in nums1:
            if self.linSearch(i, nums2) or self.linSearch(i, nums3):
                a.add(i)
        
        for i in nums2:
            if self.linSearch(i, nums1) or self.linSearch(i, nums3):
                a.add(i) 
        
        for i in nums3:
            if self.linSearch(i, nums2) or self.linSearch(i, nums1):
                a.add(i)
                
        return list(a)

# ^ Pretty slow. Use a dictionary to keep track of count. 


# Runtime: 68 ms, faster than 86.90% of Python3 online submissions for Two Out of Three.
# Memory Usage: 14.3 MB, less than 36.12% of Python3 online submissions for Two Out of Three.

def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        a = dict()
        b = list()
        
        for i in set(nums1):
            if i not in a:
                a[i] = 1
            else:
                a[i] += 1
        
        for i in set(nums2):
            if i not in a:
                a[i] = 1
            else:
                a[i] += 1
        
        for i in set(nums3):
            if i not in a:
                a[i] = 1
            else:
                a[i] += 1
                
        for i in a.items():
            if i[1] >= 2:
                b.append(i[0])
                
        return b
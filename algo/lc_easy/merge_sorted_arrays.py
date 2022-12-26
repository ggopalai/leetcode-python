# Naive, Quadratic
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        for i in range(m, m + n):
            nums1[i] = nums2[i - m]
        
        for i in range(m + n - 1):
            for j in range(m + n - i - 1):
                if nums1[j] > nums1[j + 1]:
                    nums1[j], nums1[j + 1] = nums1[j + 1], nums1[j] 

# Linear (m + n)
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        cop = nums1.copy()
        p1, p2, p = 0, 0, 0

        while p1 < m and p2 < n:
            if cop[p1] < nums2[p2]:
                nums1[p] = cop[p1]
                p1 += 1
            else:
                nums1[p] = nums2[p2]
                p2 += 1
            p += 1
        
        while p1 < m:
            nums1[p] = cop[p1]
            p += 1
            p1 += 1
        
        while p2 < n:
            nums1[p] = nums2[p2]
            p += 1
            p2 += 1
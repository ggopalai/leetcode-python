# 1. Brute force O(n log n) + linear space. (But passed LC)
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        a = sorted(nums1 + nums2)
        c = len(a)
        
        if c % 2:
            return a[ (c-1) // 2 ]
        else:
            i = c // 2
            j = i - 1
            return (a[i] + a[j]) / 2

# 2. O(log (min(m, n)))
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        
        #swapping so that we apply binary search on the smaller of the 2. This is also resolves does cause overflow which the other way does. 
        if len(A) > len(B):
            A, B = B, A
        
        total = len(A) + len(B)
        half = total // 2
        
        l, r = 0, len(A) - 1
        while True:
            i = (l + r) // 2
            j = half - i - 2
            
            #huge values if we go out of bounds
            aleft = A[i] if i >= 0 else float('-inf')
            aright = A[i+1] if (i+1) < len(A) else float('inf')
            bleft = B[j] if j >= 0 else float('-inf')
            bright = B[j+1] if (j+1) < len(B) else float('inf')
            
            if aleft <= bright and bleft <= aright:
                if total % 2:
                    return min(aright, bright)
                else:
                    return (max(aleft, bleft) + min(aright, bright)) / 2
            
            #not getting the intuition for these 2 cases. how to decide which side to move? -> move towards to the smaller element. 
            #moving mid to the right, we choose more from A and vice versa.
            elif aleft > bright:
                r = i - 1    
            else:
                l = i + 1
            
            
class Solution:
    """
    Time - O(n1) + O(n2) 
    Space - O(n2)
    """
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        # O(n2) space
        res = {nums2[i]:-1 for i in range(len(nums2))}
        
        # O(n2)
        stack = []

        # O(n2) time, each element gets pushed once and popped once at max. so 2 * O(n) time
        for i in range(len(nums2) - 1, -1, -1):
            while stack and stack[-1] < nums2[i]:
                stack.pop()
            
            if stack:
                res[nums2[i]] = stack[-1]
            
            stack.append(nums2[i])
        
        r = [res[i] for i in nums1]

        return r

        
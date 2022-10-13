class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        fn = float('inf')
        sn = float('inf')
        
        #the order of the first and second does not matter much, return true if we find a third bigger one.
        for i in nums:
            if i <= fn:
                fn = i
            elif i <= sn:
                sn = i
            else:
                return True
        
        return False
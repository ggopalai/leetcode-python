def missingNumber(self, nums: List[int]) -> int:
        a = b = 0
        l = len(nums)
        a = l * (l+1) // 2   
        b = sum(nums)
        
        return a-b
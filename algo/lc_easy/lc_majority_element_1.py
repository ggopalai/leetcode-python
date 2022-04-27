class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d = dict()
        for i in nums:
            if i not in d:
                d[i] = 1
            else:
                d[i] += 1
        
        for i in d.items():
            if i[1] > len(nums)//2:
                return i[0]
            
        

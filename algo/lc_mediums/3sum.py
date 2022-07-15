#this uses sort + two pointer method. (look at the no-sort solution also.)
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        
        for i, a in enumerate(nums):
            if i > 0 and a == nums[i-1]:  #avoids duplicate triplets
                continue
            l = i + 1
            r = len(nums) - 1
            while l < r:
                tsum = a + nums[l] + nums[r]
                if tsum == 0:
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l - 1] and l < r: #avoid duplications 
                        l += 1
                elif tsum > 0:
                    r -= 1
                else:
                    l += 1
                    
        return res
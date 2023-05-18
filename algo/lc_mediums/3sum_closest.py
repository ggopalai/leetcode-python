class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        diff = float('inf')
        
        for i in range(len(nums)):
            
            l = i + 1
            r = len(nums) - 1
            while l < r:
                tsum = nums[i] + nums[l] + nums[r]
                if abs(target - tsum) < abs(diff): # why abs for target - tsum? 
                    diff = target - tsum
                if tsum > target:
                    r -= 1
                else:
                    l += 1
            
            if diff == 0:
                break
        
        return target - diff # = sum
                    
                    
        
        
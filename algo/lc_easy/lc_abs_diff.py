# https://leetcode.com/problems/count-number-of-pairs-with-absolute-difference-k/

# quadratic solution. 
def countKDifference(self, nums: List[int], k: int) -> int:
        count = 0
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                if abs(nums[i] - nums[j]) == k:
                    count += 1
        
        return count 

#linear solution - similar to two sum. 
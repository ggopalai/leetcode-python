"""
Bruteforce - quadratic. 
"""
def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(0, len(nums)-1):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i,j]

"""
Linear solution - use a dictionary to keep track of already visited numbers and their indices. 
"""
def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = dict()
        for i in range(0, len(nums)):
            diff = target - nums[i]
            if diff in d.keys():
                return [i, d[diff]]
            else:
                d[nums[i]] = i
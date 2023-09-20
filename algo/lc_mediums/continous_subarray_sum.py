class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:

        d = {0: 0}
        ps = 0
        for i in range(len(nums)):
            ps += nums[i]
            rem = ps % k
            if rem in d and (i + 1) - d[rem] >= 2:
                return True
            else:
                if rem not in d:
                    d[rem] = i + 1

        return False

        
        
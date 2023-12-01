class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        
        # can i create enough subarrays with the mid as the largest?
        def canSplit(largest):
            count = 0
            curSum = 0
            
            # greedy
            for n in nums:
                curSum += n
                if curSum > largest:
                    count += 1
                    curSum = n
            
            return count + 1 <= k
        
        # why is r the max even though it breaks min subarray constraint?
        l, r = max(nums), sum(nums)
        res = r
        while l <= r:
            mid = (l + r) // 2
            # if i can, try to minizme the val (this is the objective)
            if canSplit(mid):
                r = mid - 1
                res = mid
            # if not, increase the largest value
            else:
                l = mid + 1
        
        return res
        
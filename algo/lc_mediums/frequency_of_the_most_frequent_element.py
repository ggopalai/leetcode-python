# brute force, TLE
class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        # sort in desc
        nums.sort(reverse=True)
        res = 1

        # check how many in the front cant be made equal to current element
        for i in range(len(nums) - 1):
            count = 1
            rem = k
            for j in range(i + 1, len(nums)):
                diff = nums[i] - nums[j]
                if diff <= rem:
                    rem -= diff
                    count += 1
                else:
                    break
            res = max(res, count)
        
        return res

# sliding window - n log n 
class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        # cur keeps track of the current sliding window's sum
        l, cur = 0, 0
        res = 1

        # find max length with nums[r] as the target
        for r in range(len(nums)):
            cur += nums[r]
            # update target
            target = nums[r]

            # dynamically find the longest possible window with all values == target
            while (r - l + 1) * target - cur > k:
                cur -= nums[l]
                l += 1
            
            res = max(res, r - l + 1) 
        
        return res
                    

                    
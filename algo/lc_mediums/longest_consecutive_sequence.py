class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        maxCount = 0
        for i in nums:
            count = 0
            # check if its the start of a sequence
            if i-1 not in s:
                count += 1
                n = i+1
                # if start of sequence, keep checking how many consecutive numbers are present. 
                while n in s:
                    count += 1
                    n += 1
                maxCount = max(count, maxCount)
        
        return maxCount
                    

#2. Neetcode
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0

        for n in nums:
            # check if its the start of a sequence
            if (n - 1) not in numSet:
                length = 1
                while (n + length) in numSet:
                    length += 1
                longest = max(length, longest)
        return longest
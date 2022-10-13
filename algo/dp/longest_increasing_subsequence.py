class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        #minimum len of lis is al teast the length of the number itself.
        lis = [1] * len(nums)
        
        for i in range(len(nums) - 2, -1, -1):
            m = []
            #for each index j to the right, if that value is greater, lis at i would be 1 + lis[j]
            for j in range(i+1, len(nums)):
                if nums[j] > nums[i]:
                    m.append(1 + lis[j])
                # if not, just the length of that index i
                else:
                    m.append(1)
            lis[i] = max(m)
        
        return max(lis)
            
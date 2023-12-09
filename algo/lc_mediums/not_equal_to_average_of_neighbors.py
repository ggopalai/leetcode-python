class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        nums.sort()
        n = len(nums)
        if n % 2:
          median = n // 2 + 1
        else:
          median = n // 2
        
        res = []

        fh = nums[:median]
        sh = nums[median: ]

        i, j = 0, 0
        while i < len(fh) and j < len(sh):
            res.append(fh[i])
            res.append(sh[j])
            i += 1
            j += 1
        while i < len(fh):
          res.append(fh[i])
          i += 1
        while j < len(sh):
          res.append(sh[i])
          j += 1
        
        return res

        
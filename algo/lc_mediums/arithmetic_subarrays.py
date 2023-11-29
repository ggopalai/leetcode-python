class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        """
        Time - m * n * log n
        """
        m = len(l)
        res = [True] * m
        
        # m times
        for i in range(m):
            
            # current subarray (len = n)
            cur = nums[l[i] : r[i] + 1]
            cur.sort() # o(n log n)

            for j in range(1, len(cur) - 1):
                if cur[j] - cur[j-1] != cur[j+1] - cur[j]:
                    res[i] = False
        
        return res

        
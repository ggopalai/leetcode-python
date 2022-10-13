# 1. Linear space approach
class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        res = []
        for i in arr:
            res.append(i)
            if not i:
                res.append(i)
        
        for i in range(len(arr)):
            arr[i] = res[i]

# 2. Constant space
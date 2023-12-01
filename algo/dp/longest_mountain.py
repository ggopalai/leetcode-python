# https://leetcode.com/problems/longest-mountain-in-array/ 

class Solution:
    """
    Time complexity - O(N)
    Space - O(1)
    """
    def longestMountain(self, arr: List[int]) -> int:
        n = len(arr)
        if n < 3:
            return 0
        
        res = 0
        for i in range(1, n - 1):
            
            # there is a mountain
            if arr[i] > arr[i - 1] and arr[i] > arr[i + 1]:
                count = 3

                # expand to left
                l = i - 1
                while l > 0 and arr[l] > arr[l - 1]:
                    count += 1
                    l -= 1

                r = i + 1
                # expand to right
                while r < n - 1 and arr[r] > arr[r + 1]:
                    count += 1
                    r += 1
            
                res = max(res, count)
        
        return res

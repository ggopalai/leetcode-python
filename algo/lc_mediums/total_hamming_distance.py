class Solution:
    """
    Time - O(32 * n)
    Space - O(1)
    """
    def totalHammingDistance(self, nums: List[int]) -> int:
        res = 0

        for i in range(32):
            c = 0
            for num in nums:
                c += num >> i & 1
            res += c * (len(nums) - c)
        
        return res



        
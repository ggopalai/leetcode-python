class Solution:
    def minOperations(self, nums: List[int]) -> int:
        from collections import Counter
        count = Counter(nums)
        res = 0
        for val in count.values():
            if val == 1:
                return -1
            elif val % 3 == 0:
                res += val // 3
            elif val % 3 == 2:
                res += (val // 3) + 1 
            else:
                byThree = (val // 3) - 1
                rem = val - (byThree * 3) # for 2 
                res += (byThree + rem // 2)

        return res
        